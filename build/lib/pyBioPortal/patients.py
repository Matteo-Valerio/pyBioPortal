import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_all_patients(projection="SUMMARY", direction="ASC", keyword=None, pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Get all patients. \n
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
    :param keyword: Search keyword that applies to ID of the patients. \n
    :type keyword: str \n
    :param pageNumber: Page number of the result list. \n
            - Minimum value is 0.
    :type pageNumber: int \n
    :param pageSize: Page size of the result list. \n
            - Minimum value is 1, maximum value is 10000000.
    :type pageSize: int \n
    :param sortBy: Name of the property that the result list is sorted by. \n
        Possible values: \n
            - "patientId"
    :type sortBy: str \n
    :returns: A DataFrame containing list of patients. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/patients"
    params = {
        "direction": direction,
        "keyword": keyword,
        "projection": projection,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get all patients.")

def fetch_patients(patient_identifiers=None, unique_patient_keys=None, projection="SUMMARY"):
    """
    Fetch patients. \n
    :param patient_identifiers: List of Patient ID / Study ID pairs. \n
        Each dict should have the following format: \n
            patient_identifiers=[
                                {"patient_ids": ['TCGA-3C-AAAU','TCGA-3C-AALI'], 
                                 "study_id": "brca_tcga"},
                                {"patient_ids": ['TCGA-A1-A0SB','TCGA-A1-A0SD'], 
                                 "study_id": "brca_tcga_pub"}
                                ] \n
    :type patient_identifiers: list of dict \n
    :param unique_patient_keys: List of Unique Patient Keys, e.g. ['VENHQS0zQy1BQUFVOmJyY2FfdGNnYQ', 
                                                                  'VENHQS1BMS1BMFNEOmJyY2FfdGNnYV9wdWI']. \n
    \:type unique_patient_keys: list of str \n
    \:param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing list of patients. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/patients/fetch"
    params = {
        "projection": projection
    }

    patient_filter = {}

    if patient_identifiers:
        patient_filter['patientIdentifiers'] = []

        for item in patient_identifiers:
            patient_ids = item["patient_ids"]
            study_id = item["study_id"]

            for patient_id in patient_ids:
                identifier = {
                    "patientId": patient_id,
                    "studyId": study_id
                }
                patient_filter["patientIdentifiers"].append(identifier)

    if unique_patient_keys:
        patient_filter['uniquePatientKeys'] = unique_patient_keys

    response = requests.post(f"{base_url}{endpoint}", params=params, json=patient_filter)
    return process_response(response, "Failed to fetch patients.")

def get_all_patients_in_study(study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all patients in a study. \n
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
            - "patientId": Sort by patient ID.
    :type sortBy: str \n
    :returns: A DataFrame containing list of patients in the specified study. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/studies/{study_id}/patients"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get patients in the specified study.")

def get_patient_in_study(study_id, patient_id):
    """
    Get a patient in a study. \n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
    :param patient_id: Patient ID (e.g., "TCGA-OR-A5J2"). \n
    :type patient_id: str \n
    :returns: A DataFrame containing details of the specified patient in the study. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/studies/{study_id}/patients/{patient_id}"

    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get the specified patient in the study.")