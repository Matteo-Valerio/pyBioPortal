import requests
import pandas as pd
from pyBioGate.config import base_url

###########
# Samples #
###########
def get_samples_by_keyword(self, keyword=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleId"):
    """
    Get all samples matching a keyword.
    :param keyword: Search keyword that applies to the study ID.
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
        - "sampleId"
        - "sampleType"
    :type sortBy: str, optional, default: "sampleId"
    :returns: List of samples matching the keyword.
    :rtype: list[dict]
    """
    endpoint = "/samples"
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
        raise Exception(f"Failed to get samples by keyword. Status code: {response.status_code}")
def fetch_samples(self, sample_ids, projection="SUMMARY"):
    """
    Fetch samples by ID.
    :param sample_ids: List of sample identifiers.
    :type sample_ids: list[str]
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: List of samples by ID.
    :rtype: list[dict]
    """
    endpoint = "/samples/fetch"
    params = {
        "projection": projection
    }
    response = requests.post(f"{self.base_url}{endpoint}", json=sample_ids, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch samples by ID. Status code: {response.status_code}")
        
###########
# Samples #
###########

def get_all_samples_of_patient_in_study(self, study_id, patient_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleId"):
    """
    Get all samples of a patient in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param patient_id: Patient ID, e.g., "TCGA-OR-A5J2".
    :type patient_id: str
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
        - "sampleId": Sort by sample ID.
        - "sampleType": Sort by sample type.
    :type sortBy: str, optional, default: "sampleId"
    :returns: List of samples of the specified patient in the study.
    :rtype: list[dict]
    """
    endpoint = f"/studies/{study_id}/patients/{patient_id}/samples"
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
        raise Exception(f"Failed to get samples of the specified patient in the study. Status code: {response.status_code}")
    
###########
# Samples #
###########
def get_all_samples_in_study(self, study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleId"):
    """
    Get all samples in a study.
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
        - "sampleId": Sort by sample ID.
        - "sampleType": Sort by sample type.
    :type sortBy: str, optional, default: "sampleId"
    :returns: List of samples in the specified study.
    :rtype: list[dict]
    """
    endpoint = f"/studies/{study_id}/samples"
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
        raise Exception(f"Failed to get samples in the study. Status code: {response.status_code}")
def get_sample_in_study(self, study_id, sample_id):
    """
    Get information about a specific sample in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param sample_id: Sample ID, e.g., "TCGA-OR-A5J2-01".
    :type sample_id: str
    :returns: Information about the specified sample.
    :rtype: dict
    """
    endpoint = f"/studies/{study_id}/samples/{sample_id}"
    response = requests.get(f"{self.base_url}{endpoint}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get sample information. Status code: {response.status_code}")