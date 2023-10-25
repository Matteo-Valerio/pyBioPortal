import requests
import pandas as pd
from pyBioGate.config import base_url

########
# Info #
########
def get_info(self):
    """
    Get information about the running instance.
    :returns: Information about the running instance.
    :rtype: dict
    """
    response = requests.get(f"{self.base_url}/info")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get information. Status code: {response.status_code}")