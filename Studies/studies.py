import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

###########
# Studies #
###########
def get_all_studies(keyword=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="studyId"):
    """
    Get all studies.
    :param keyword: Search keyword that applies to name and cancer type of the studies.
    :type keyword: str, optional
    :param direction: Direction of the sort.
        - "ASC": Ascending.
        - "DESC": Descending.
    :type direction: str, optional, default: "ASC"
    :param pageNumber: Page number of the result list.
    :type pageNumber: int, optional, default: 0
    :param pageSize: Page size of the result list.
    :type pageSize: int, optional, default: 10000000
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :param sortBy: Name of the property that the result list is sorted by.
        Possible values:
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
    :type sortBy: str, optional, default: "studyId"
    :returns: A DataFrame containing list of studies.
    :rtype: pandas.DataFrame
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
    return check_response(response, "Failed to get all studies.")

def get_study(study_id):
    """
    Get a study by ID.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :returns: A DataFrame containing information about the study.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}"
    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get the study by ID.")
        
def get_tags_of_study(study_id):
    """
    Get the tags of a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :return: A DataFrame containing tags associated with the study.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}/tags"
    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get tags for the study.")
    
def fetch_studies(study_ids = [], projection="SUMMARY"):
    """
    Fetch studies by IDs.
    :param study_ids: List of study identifiers.
    :type study_ids: list of str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: A DataFrame containing list of studies by IDs.
    :rtype: pandas.DataFrame
    """
    endpoint = "/studies/fetch"
    params = {
        "projection": projection
    }

    response = requests.post(f"{base_url}{endpoint}", json=study_ids, params=params)
    return check_response(response, "Failed to fetch studies by IDs.")
    
def fetch_tags_for_studies(study_ids= []):
    """
    Get the study tags by IDs.
    :param study_ids: List of study identifiers.
    :type study_ids: list of str
    :returns: A DataFrame containing study tags for multiple studies.
    :rtype: pandas.DataFrame
    """
    endpoint = "/studies/tags/fetch"
    response = requests.post(f"{base_url}{endpoint}", json=study_ids)
    return check_response(response, "Failed to fetch study tags for multiple studies.")
    
