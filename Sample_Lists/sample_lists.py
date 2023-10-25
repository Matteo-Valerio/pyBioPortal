import requests
import pandas as pd
from pyBioGate.config import base_url

################
# Sample Lists #
################
def get_all_sample_lists(self, projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy="sampleListId"):
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
    :returns: List of sample lists.
    :rtype: list[dict]
    """
    endpoint = "/sample-lists"
    params = {
        "direction": direction,
        "projection": projection,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "sortBy": sortBy
    }
    response = requests.get(f"{self.base_url}{endpoint}", params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get all sample lists. Status code: {response.status_code}")
def fetch_sample_lists(self, sample_list_ids, projection="SUMMARY"):
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
    :returns: List of sample lists.
    :rtype: list[dict]
    """
    endpoint = "/sample-lists/fetch"
    params = {
        "projection": projection
    }
    response = requests.post(f"{self.base_url}{endpoint}", json=sample_list_ids, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch sample lists. Status code: {response.status_code}")
def get_sample_list(self, sample_list_id):
    """
    Get sample list.
    :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
    :type sample_list_id: str
    :returns: Sample list details.
    :rtype: dict
    """
    endpoint = f"/sample-lists/{sample_list_id}"
    response = requests.get(f"{self.base_url}{endpoint}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get sample list. Status code: {response.status_code}")
def get_all_sample_ids_in_sample_list(self, sample_list_id):
    """
    Get all sample IDs in a sample list.
    :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
    :type sample_list_id: str
    :returns: List of sample IDs in the sample list.
    :rtype: list[str]
    """
    endpoint = f"/sample-lists/{sample_list_id}/sample-ids"
    response = requests.get(f"{self.base_url}{endpoint}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get all sample IDs in sample list. Status code: {response.status_code}")
        
################
# Sample Lists #
################
def get_all_sample_lists_in_study(self, study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleListId"):
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
    :returns: List of sample lists in the specified study.
    :rtype: list[dict]
    """
    endpoint = f"/studies/{study_id}/sample-lists"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }
    response = requests.get(f"{self.base_url}{endpoint}", params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get sample lists in the study. Status code: {response.status_code}")