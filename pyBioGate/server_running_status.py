import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

#########################
# Server running status #
#########################
def get_server_status():
    """
    Get the running status of the server.
    :returns: A DataFrame containing the status of the server.
    :rtype: pandas.DataFrame
    """
    endpoint = "/health"
    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get server status.")