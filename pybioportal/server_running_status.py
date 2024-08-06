import requests
<<<<<<< HEAD
from .__config import base_url,get_headers
=======
from .__config import base_url
>>>>>>> origin/master
from .__aux_funcs import process_response

def get_server_status():
    """
    Get the running status of the server. \n
    :returns: A DataFrame containing the status of the server. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/health"
<<<<<<< HEAD
    
    headers = get_headers()
    response = requests.get(f"{base_url}{endpoint}",headers=headers)
=======
    response = requests.get(f"{base_url}{endpoint}")
>>>>>>> origin/master
    return process_response(response, "Failed to get server status.")