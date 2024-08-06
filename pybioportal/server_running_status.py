import requests
from .__config import base_url,get_headers
from .__aux_funcs import process_response

def get_server_status():
    """
    Get the running status of the server. \n
    :returns: A DataFrame containing the status of the server. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/health"
    
    headers = get_headers()
    response = requests.get(f"{base_url}{endpoint}",headers=headers)
    return process_response(response, "Failed to get server status.")