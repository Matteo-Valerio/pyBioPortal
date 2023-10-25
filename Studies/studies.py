import requests
import pandas as pd
from pyBioGate.config import base_url

###########
# Studies #
###########
def get_all_studies(self, keyword=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="studyId"):
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
    :returns: List of studies.
    :rtype: list[dict]
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
    response = requests.get(f"{self.base_url}{endpoint}", params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get all studies. Status code: {response.status_code}")
def fetch_studies(self, study_ids, projection="SUMMARY"):
    """
    Fetch studies by IDs.
    :param study_ids: List of study identifiers.
    :type study_ids: list[str]
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: List of studies by IDs.
    :rtype: list[dict]
    """
    endpoint = "/studies/fetch"
    params = {
        "projection": projection
    }
    response = requests.post(f"{self.base_url}{endpoint}", json=study_ids, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch studies by IDs. Status code: {response.status_code}")
def get_tags_for_multiple_studies(self, study_ids):
    """
    Get the study tags by IDs.
    :param study_ids: List of study identifiers.
    :type study_ids: list[str]
    :returns: Study tags for multiple studies.
    :rtype: list[dict]
    """
    endpoint = "/studies/tags/fetch"
    response = requests.post(f"{self.base_url}{endpoint}", json=study_ids)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get study tags for multiple studies. Status code: {response.status_code}")
def get_study(self, study_id):
    """
    Get a study by ID.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :returns: Information about the study.
    :rtype: dict
    """
    endpoint = f"/studies/{study_id}"
    response = requests.get(f"{self.base_url}{endpoint}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get the study by ID. Status code: {response.status_code}")
        
###########
# Studies #
###########
def get_tags_of_study(self, study_id):
    """
    Get the tags of a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :return: Dictionary of tags associated with the study.
    :rtype: dict
    """
    endpoint = f"/studies/{study_id}/tags"
    response = requests.get(f"{self.base_url}{endpoint}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get tags for the study. Status code: {response.status_code}")