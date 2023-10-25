import requests
import pandas as pd
from pyBioGate.config import base_url

############
# Patients #
############
def get_all_patients_in_study(self, study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="patientId"):
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
    :returns: List of patients in the specified study.
    :rtype: list[dict]
    """
    endpoint = f"/studies/{study_id}/patients"
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
        raise Exception(f"Failed to get patients in the specified study. Status code: {response.status_code}")
def get_patient_in_study(self, study_id, patient_id):
    """
    Get a patient in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param patient_id: Patient ID, e.g., "TCGA-OR-A5J2".
    :type patient_id: str
    :returns: Details of the specified patient in the study.
    :rtype: dict
    """
    endpoint = f"/studies/{study_id}/patients/{patient_id}"
    response = requests.get(f"{self.base_url}{endpoint}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get the specified patient in the study. Status code: {response.status_code}")
        
############
# Patients #
############
def get_all_patients(self, projection="SUMMARY", direction="ASC", keyword=None, pageNumber=0, pageSize=10000000, sortBy="patientId"):
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
    :returns: List of patients.
    :rtype: list[dict]
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
    response = requests.get(f"{self.base_url}{endpoint}", params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get all patients. Status code: {response.status_code}")
def fetch_patients(self, patient_filter, projection="SUMMARY"):
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
    :returns: List of patients.
    :rtype: list[dict]
    """
    endpoint = "/patients/fetch"
    params = {
        "projection": projection
    }
    response = requests.post(f"{self.base_url}{endpoint}", json=patient_filter, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch patients. Status code: {response.status_code}")