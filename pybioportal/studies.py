import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_all_studies(keyword=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all studies. \n
    :param keyword: Search keyword that applies to name and cancer type of the studies. \n
    :type keyword: str \n
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
        Possible values: \n
            - "cancerTypeId"
            - "citation"
            - "description"
            - "groups"
            - "importDate"
            - "name"
            - "pmid"
            - "publicStudy"
            - "status"
            - "studyId"
    :type sortBy: str \n
    :returns: A DataFrame containing list of studies. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/studies"
    params = {
        "keyword": keyword,
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get all studies.")

def get_study(study_id):
    """
    Get a study by ID. \n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
    :returns: A DataFrame containing information about the study. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/studies/{study_id}"
    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get the study by ID.")
        
def get_tags_of_study(study_id):
    """
    Get the tags of a study. \n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
    :return: A DataFrame containing tags associated with the study. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/studies/{study_id}/tags"

    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get tags for the study.")
    
def fetch_studies(study_ids = [], projection="SUMMARY"):
    """
    Fetch studies by IDs. \n
    :param study_ids: List of study identifiers (e.g., ["brca_tcga","acc_tcga"]). \n
    :type study_ids: list of str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing list of studies by IDs. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/studies/fetch"
    params = {
        "projection": projection
    }

    response = requests.post(f"{base_url}{endpoint}", params=params, json=study_ids)
    return process_response(response, "Failed to fetch studies by IDs.")
    
def fetch_tags_for_studies(study_ids= []):
    """
    Get the study tags by IDs. \n
    :param study_ids: List of study identifiers. \n
    :type study_ids: list of str \n
    :returns: A DataFrame containing study tags for multiple studies. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/studies/tags/fetch"
    
    response = requests.post(f"{base_url}{endpoint}", json=study_ids)
    return process_response(response, "Failed to fetch study tags for multiple studies.")
    
