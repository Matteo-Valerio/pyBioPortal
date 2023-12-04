import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_all_sample_lists(projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Get all sample lists. \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
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
    :param sortBy: Name of the property that the result list is sorted by. \n
        Possible values: \n
            - "category"
            - "description"
            - "name"
            - "sampleListId"
            - "studyId"
    :type sortBy: str \n
    :returns: A DataFrame containing sample lists. \n
    :rtype: pandas.DataFrame \n
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
    return process_response(response, "Failed to get all sample lists.")

def get_sample_list(sample_list_id):
    """
    Get sample list. \n
    :param sample_list_id: Sample List ID (e.g., "acc_tcga_all"). \n
    :type sample_list_id: str \n
    :returns: A DataFrame containing sample list details. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/sample-lists/{sample_list_id}"

    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get sample list.")

def get_all_sample_ids_in_sample_list(sample_list_id):
    """
    Get all sample IDs in a sample list. \n
    :param sample_list_id: Sample List ID (e.g., "acc_tcga_all"). \n
    :type sample_list_id: str \n
    :returns: A DataFrame containing sample IDs in the sample list. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/sample-lists/{sample_list_id}/sample-ids"

    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get all sample IDs in sample list.")
    
def fetch_sample_lists(sample_list_ids, projection="SUMMARY"):
    """
    Fetch sample lists by ID. \n
    :param sample_list_ids: List of sample list IDs. \n
    :type sample_list_ids: list of str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing sample lists. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/sample-lists/fetch"
    params = {
        "projection": projection
    }

    response = requests.post(f"{base_url}{endpoint}", params=params, json=sample_list_ids)
    return process_response(response, "Failed to fetch sample lists.")
        
def get_all_sample_lists_in_study(study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all sample lists in a study. \n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
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
            - "category": Sort by category.
            - "description": Sort by description.
            - "name": Sort by name.
            - "sampleListId": Sort by sample list ID.
            - "studyId": Sort by study ID.
    :type sortBy: str \n
    :returns: A DataFrame containing sample lists in the specified study. \n
    :rtype: pandas.DataFrame \n
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
    return process_response(response, "Failed to get sample lists in the study.")