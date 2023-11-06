import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

################
# Sample Lists #
################
def get_all_sample_lists(projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy="sampleListId"):
    """
    Get all sample lists.
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :param direction: Direction of the sort.
        - "ASC": Ascending.
        - "DESC": Descending.
    :type direction: str, optional, default: "ASC"
    :param pageNumber: Page number of the result list.
    :type pageNumber: int, optional, default: 0
    :param pageSize: Page size of the result list.
    :type pageSize: int, optional, default: 10000000
    :param sortBy: Name of the property that the result list is sorted by.
        Possible values:
        - "category"
        - "description"
        - "name"
        - "sampleListId"
        - "studyId"
    :type sortBy: str, optional, default: "sampleListId"
    :returns: A DataFrame containing sample lists.
    :rtype: pandas.DataFrame
    """
    endpoint = "/sample-lists"
    params = {
        "direction": direction,
        "projection": projection,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get all sample lists.")

def get_sample_list(sample_list_id):
    """
    Get sample list.
    :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
    :type sample_list_id: str
    :returns: A DataFrame containing sample list details.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/sample-lists/{sample_list_id}"

    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get sample list.")

def get_all_sample_ids_in_sample_list(sample_list_id):
    """
    Get all sample IDs in a sample list.
    :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
    :type sample_list_id: str
    :returns: A DataFrame containing sample IDs in the sample list.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/sample-lists/{sample_list_id}/sample-ids"
    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get all sample IDs in sample list.")
    
def fetch_sample_lists(sample_list_ids, projection="SUMMARY"):
    """
    Fetch sample lists by ID.
    :param sample_list_ids: List of sample list IDs.
    :type sample_list_ids: list[str]
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: A DataFrame containing sample lists.
    :rtype: pandas.DataFrame
    """
    endpoint = "/sample-lists/fetch"
    params = {
        "projection": projection
    }

    response = requests.post(f"{base_url}{endpoint}", json=sample_list_ids, params=params)
    return check_response(response, "Failed to fetch sample lists.")
        
def get_all_sample_lists_in_study(study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleListId"):
    """
    Get all sample lists in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
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
        - "category": Sort by category.
        - "description": Sort by description.
        - "name": Sort by name.
        - "sampleListId": Sort by sample list ID.
        - "studyId": Sort by study ID.
    :type sortBy: str, optional, default: "sampleListId"
    :returns: A DataFrame containing sample lists in the specified study.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}/sample-lists"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }
    
    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get sample lists in the study.")