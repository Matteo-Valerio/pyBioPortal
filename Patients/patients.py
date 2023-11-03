import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

############
# Patients #
############
def get_all_patients(projection="SUMMARY", direction="ASC", keyword=None, pageNumber=0, pageSize=10000000, sortBy="patientId"):
    """
    Get all patients.
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
    :param keyword: Search keyword that applies to ID of the patients.
    :type keyword: str, optional
    :param pageNumber: Page number of the result list.
    :type pageNumber: int, optional, default: 0
    :param pageSize: Page size of the result list.
    :type pageSize: int, optional, default: 10000000
    :param sortBy: Name of the property that the result list is sorted by.
        Possible values:
        - "patientId"
    :type sortBy: str, optional, default: "patientId"
    :returns: A DataFrame containing list of patients.
    :rtype: pandas.DataFrame
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
    return check_response(response, "Failed to get all patients.")

def fetch_patients(patient_identifiers=None, unique_patient_keys=None, projection="SUMMARY"):
    """
    Fetch patients.
    :param patient_filter: List of patient identifiers.
    :type patient_filter: dict
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: A DataFrame containing list of patients.
    :rtype: pandas.DataFrame
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

    response = requests.post(f"{base_url}{endpoint}", json=patient_filter, params=params)
    return check_response(response, "Failed to fetch patients.")

def get_all_patients_in_study(study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="patientId"):
    """
    Get all patients in a study.
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
        - "patientId": Sort by patient ID.
    :type sortBy: str, optional, default: "patientId"
    :returns: A DataFrame containing list of patients in the specified study.
    :rtype: pandas.DataFrame
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
    return check_response(response, "Failed to get patients in the specified study.")

def get_patient_in_study(study_id, patient_id):
    """
    Get a patient in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param patient_id: Patient ID, e.g., "TCGA-OR-A5J2".
    :type patient_id: str
    :returns: A DataFrame containing details of the specified patient in the study.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}/patients/{patient_id}"

    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get the specified patient in the study.")