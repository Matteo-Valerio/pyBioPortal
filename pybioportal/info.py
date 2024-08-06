import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_info():
    """
    Get information about the running instance.
    
    :returns: A DataFrame containing information about the running instance.
    :rtype: pandas.DataFrame
    """
    endpoint = "/info"
    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get information.")
