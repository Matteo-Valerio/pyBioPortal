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
    
def fetch_samples(sample_identifiers=None, sample_list_ids=None, unique_sample_keys=None, projection="SUMMARY"):
    """
    Fetch samples by ID.
    :param sample_identifiers: List of Sample ID / Study ID pairs.
    :type sample_identifiers: list of dict
        Each dict should have the following format:
            sample_identifiers=[
                               {"sample_ids": ['TCGA-AR-A1AR-01','TCGA-BH-A1EO-01','TCGA-BH-A1ES-01'], 
                                "study_id": "brca_tcga"},
                               {"sample_ids": ['TCGA-A2-A0T2-01','TCGA-A2-A04P-01'], 
                                "study_id": "brca_tcga_pub"}
                               ]
    :param sample_list_ids: List of Sample List IDs, e.g. ['brca_tcga_cna', 'brca_tcga_mrna', 'brca_tcga_pub_cna'].
    :type sample_list_ids: list of str
    :param unique_sample_keys: List of Unique Sample Keys, e.g. ['VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ',
                                                                 'VENHQS1CNi1BMElRLTAxOmJyY2FfdGNnYV9wdWI',
                                                                 'VENHQS1CSC1BMUZELTAxOmJyY2FfdGNnYQ'].
    :type unique_sample_keys: list of str
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

    sample_filter = {}

    if sample_identifiers:
        sample_filter['sampleIdentifiers'] = []

        for item in sample_identifiers:
            sample_ids = item["sample_ids"]
            study_id = item["study_id"]

            for sample_id in sample_ids:
                identifier = {
                    "sampleId": sample_id,
                    "studyId": study_id
                }
                sample_filter["sampleIdentifiers"].append(identifier)

    if sample_list_ids:
        sample_filter['sampleListIds'] = sample_list_ids
    
    if unique_sample_keys:
        sample_filter['uniqueSampleKeys'] = unique_sample_keys

    response = requests.post(f"{base_url}{endpoint}", params=params, json=sample_filter)
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