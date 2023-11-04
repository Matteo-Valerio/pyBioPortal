import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

###########
# Samples #
###########
def get_samples_by_keyword(keyword=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
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
    :returns: A DataFrame containing samples matching the keyword.
    :rtype: pandas.DataFrame
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

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get samples by keyword.")
    
def fetch_samples(sample_ids, projection="SUMMARY"):
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
    :returns: A DataFrame containing samples by ID.
    :rtype: pandas.DataFrame
    """
    endpoint = "/samples/fetch"
    params = {
        "projection": projection
    }

    response = requests.post(f"{base_url}{endpoint}", json=sample_ids, params=params)
    return check_response(response, "Failed to fetch samples by ID.")

def get_all_samples_of_patient_in_study(study_id, patient_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleId"):
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
    :returns: A DataFrame containing samples of the specified patient in the study.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}/patients/{patient_id}/samples"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get samples of the specified patient in the study.")

def get_all_samples_in_study(study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleId"):
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
    :returns: A DataFrame containing samples in the specified study.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}/samples"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get samples in the study.")
    
def get_sample_in_study(study_id, sample_id):
    """
    Get information about a specific sample in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param sample_id: Sample ID, e.g., "TCGA-OR-A5J2-01".
    :type sample_id: str
    :returns: A DataFrame containing information about the specified sample.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}/samples/{sample_id}"

    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get sample information.")