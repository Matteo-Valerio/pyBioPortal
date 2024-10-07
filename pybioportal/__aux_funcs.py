# Auxiliary functions
import requests 
import pandas as pd
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from .__config import base_url, API_TOKEN

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the console handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)


def get_session():  
    """
    Create a requests session with the Authorization header for API token authentication.
    """
    session = requests.Session()
    if API_TOKEN:
        session.headers.update({'Authorization': f'Bearer {API_TOKEN}'})
    return session

def make_request(endpoint, method="GET", params=None, data=None, headers=None, timeout=10):
    """
    Make an HTTP request using the specified method and parameters.

    :param endpoint: API endpoint (e.g., "/genes").
    :type endpoint: str
    :param method: HTTP method (e.g., "GET", "POST"). Defaults to "GET".
    :type method: str
    :param params: Query parameters for the request.
    :type params: dict
    :param data: JSON payload for POST requests.
    :type data: dict
    :param headers: Additional HTTP headers.
    :type headers: dict
    :param timeout: Request timeout in seconds.
    :type timeout: int
    :return: Response object.
    :rtype: requests.Response
    :raises: requests.exceptions.RequestException on failure.
    """
    url = f"{base_url}{endpoint}"
    
    # Initialize headers if not provided
    if headers is None:
        headers = {}
    
    # Add the API token to headers
    if API_TOKEN:
        headers['Authorization'] = f"Bearer {API_TOKEN}"
    
    # Set up retries for transient errors
    session = get_session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    try:
        logger.info(f"Making {method} request to {url} with params={params} and data={data}")
        response = session.request(method, url, params=params, json=data, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        logger.info(f"Received response with status code {response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {method} {url} - {e}")
        raise

def process_response(response, fail_msg, ret_format=None, attribute_ids=None):
    if response.status_code == 200:
        if response.text and response.text != '[]':  # Check if the response body is not empty
            try:
                data = response.json()
                if ret_format is None and attribute_ids is None:
                    if isinstance(data, list):
                        df = pd.DataFrame(data)
                        df = flatten_dict_columns(df)
                        df = flatten_dict_list_columns(df)
                        return df
                    elif isinstance(data, dict):  # Handle single-row dictionary
                        df = pd.DataFrame({key: [value] for key, value in data.items()})
                        df = flatten_dict_columns(df)
                        df = flatten_dict_list_columns(df)
                        return df
                else:
                    df = pd.DataFrame(data)
                    if ret_format == 'WIDE':
                        cols_to_group = df.columns[:-2]
                        df = df.pivot(index=cols_to_group, columns='clinicalAttributeId', values='value')              
                        df.reset_index(inplace=True)
                        # Check if all attributes have been retrieved
                        miss_attr = [col for col in attribute_ids if col not in df.columns]
                        if miss_attr:
                            logger.warning("Attributes not present: " + ", ".join(map(str, miss_attr)))
                    elif ret_format == 'LONG':
                        miss_attr = [attr for attr in attribute_ids if attr not in df['clinicalAttributeId'].unique()]
                        if miss_attr:
                            logger.warning("Attributes not present: " + ", ".join(map(str, miss_attr)))
                    else: 
                        raise ValueError("Error: ret_format must be 'LONG' or 'WIDE'")
                    return df
            except ValueError as e:
                logger.error(f"Error decoding the JSON response: {e}")
                raise ValueError(f"{fail_msg} Error decoding JSON: {e}")
        else:
            logger.warning("Response is empty. No data available.")
            return pd.DataFrame()  # Return an empty DataFrame
    else:
        error_message = f"{fail_msg} Status code: {response.status_code}"
    
        if response.text:
            try:
                error_json = response.json() 
                error_message += f"\nError message: {error_json.get('message', 'No message provided.')}"
            except ValueError:
                error_message += f"\nError message: {response.text}"
    
        # Attach the response to the exception for better traceback
        http_error = requests.exceptions.HTTPError(error_message, response=response)
        logger.error(f"HTTPError: {error_message}")
        raise http_error

def flatten_dict_columns(df):
    def flatten_dict(d, parent_key=''):
        items = {}
        for key, value in d.items():
            new_key = parent_key + '_' + key if parent_key else key
            if isinstance(value, dict):
                items[new_key] = flatten_dict(value)
            else:
                items[new_key] = value
        return items

    new_data = []
    for _, row in df.iterrows():
        flattened_dict = {}
        for column, value in row.items():
            if isinstance(value, dict):
                flattened_dict.update(flatten_dict(value, column))
            else:
                flattened_dict[column] = value
        new_data.append(flattened_dict)

    new_df = pd.DataFrame(new_data)
    return new_df

def flatten_dict_list_columns(df):
    list_columns = []

    # Identify columns that contain lists of dict
    for column in df.columns:
        if df[column].apply(lambda x: isinstance(x, list) and all(isinstance(item, dict) for item in x)).all():
            list_columns.append(column)

    if not list_columns:
        return df

    new_data = []
    for _, row in df.iterrows():
        flattened_dicts = []
        for column in list_columns:
            list_of_dicts = row[column]
            for d in list_of_dicts:
                flattened_dict = {k: v for k, v in row.items() if k not in list_columns}
                flattened_dict.update(d)
                flattened_dicts.append(flattened_dict)
        if not flattened_dicts:
            flattened_dicts = [row.to_dict()]
        new_data.extend(flattened_dicts)

    new_df = pd.DataFrame(new_data)
    return new_df