import requests
import pandas as pd
from config import base_url

################
# Cancer Types #
################
#Puoi utilizzare queste funzioni per ottenere dati sui tipi di cancro da BioPortal.
def get_all_cancer_types(direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all cancer types from BioPortal.
    :param direction: Direction of the sort.
        - "ASC": Ascending order (default).
        - "DESC": Descending order.
    :type direction: str
    :param pageNumber: Page number of the result list.
        Minimum value is 0.
    :type pageNumber: int
    :param pageSize: Page size of the result list.
        Minimum value is 1, maximum value is 10000000.
    :type pageSize: int
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :param sortBy: Name of the property that the result list is sorted by.
    :type sortBy: str
        Possible values:
            - "cancerTypeId": Sort by cancer type ID.
            - "dedicatedColor": Sort by dedicated color.
            - "name": Sort by name.
            - "parent": Sort by parent.
            - "shortName": Sort by short name.
    :returns: A DataFrame containing the list of cancer types.
    :rtype: pandas.DataFrame
    """
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection
    }
    if sortBy:
        params["sortBy"] = sortBy
    response = requests.get(f"{base_url}/cancer-types", params=params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to get cancer types. Status code: {response.status_code}")

def get_cancer_type(cancer_type_id):
    """
    Get a specific cancer type from BioPortal.
    :param cancer_type_id: Cancer Type ID (e.g., "acc").
    :type cancer_type_id: str
    :returns: A DataFrame containing information about the specific cancer type.
    :rtype: pandas.DataFrame
    """
    response = requests.get(f"{base_url}/cancer-types/{cancer_type_id}")
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data, index=[0])
    else:
        raise Exception(f"Failed to get cancer type {cancer_type_id}. Status code: {response.status_code}")