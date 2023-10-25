import requests
import pandas as pd
from pyBioGate.config import base_url

#########################
# Server running status #
#########################
def get_server_status(self):
    """
    Get the running status of the server.
    :returns: The status of the server.
    :rtype: dict
    """
    response = requests.get(f"{self.base_url}/health")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get server status. Status code: {response.status_code}")