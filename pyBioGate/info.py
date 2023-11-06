import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

########
# Info #
########
def get_info():
    """
    Get information about the running instance.
    :returns: A DataFrame containing information about the running instance.
    :rtype: pandas.DataFrame
    """
    endpoint = "/info"
    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get information.")
