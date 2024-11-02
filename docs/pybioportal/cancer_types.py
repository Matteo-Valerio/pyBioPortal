import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_all_cancer_types(direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all cancer types from cBioPortal. \n
    :param direction: Direction of the sort. \n
        Possible values: \n
            - "ASC": Ascending (default).
            - "DESC": Descending.
    :type direction: str \n
    :param pageNumber: Page number of the result list. \n
            - Minimum value is 0.
    :type pageNumber: int \n
    :param pageSize: Page size of the result list. \n
            - Minimum value is 1, maximum value is 10000000. 
    :type pageSize: int \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :param sortBy: Name of the property that the result list is sorted by. \n
    :type sortBy: str \n
        Possible values: \n
            - "cancerTypeId": Sort by cancer type ID.
            - "dedicatedColor": Sort by dedicated color.
            - "name": Sort by name.
            - "parent": Sort by parent.
            - "shortName": Sort by short name.
    :returns: A DataFrame containing the list of cancer types. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/cancer-types"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }
    
    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get cancer types.")

def get_cancer_type(cancer_type_id):
    """
    Get a specific cancer type from cBioPortal. \n
    :param cancer_type_id: Cancer Type ID (e.g., "acc"). \n
    :type cancer_type_id: str \n
    :returns: A DataFrame containing information about the specific cancer type. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/cancer-types/{cancer_type_id}"
    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, f"Failed to get cancer type {cancer_type_id}.")