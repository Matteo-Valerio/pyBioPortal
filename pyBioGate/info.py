import requests
from .config import base_url
from .aux_funcs import process_response

########
# Info #
########
def get_info():
    """
    Get information about the running instance. \n
    :returns: A DataFrame containing information about the running instance. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/info"
    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get information.")
