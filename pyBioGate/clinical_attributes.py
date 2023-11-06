import requests
import pandas as pd
from .config import base_url
from .aux_funcs import check_response

#######################
# Clinical Attributes #
#######################
def get_all_clinical_attributes(direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all clinical attributes from BioPortal.
    :param direction: Direction of the sort.
        - "ASC": Ascending order (default).
        - "DESC": Descending order.
    :type direction: str
    :param pageNumber: Page number of the result list.
        Minimum value is 0.
    :type pageNumber: int
    :param pageSize: Page size of the result list.
        Minimum value is 1, maximum value is 10000000.
    :type pageSize: int
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :param sortBy: Name of the property that the result list is sorted by.
        Possible values:
        - "clinicalAttributeId": Sort by clinical attribute ID.
        - "datatype": Sort by datatype.
        - "description": Sort by description.
        - "displayName": Sort by display name.
        - "patientAttribute": Sort by patient attribute.
        - "priority": Sort by priority.
        - "studyId": Sort by study ID.
    :type sortBy: str
    :returns: A DataFrame containing the list of clinical attributes.
    :rtype: pandas.DataFrame
    """
    endpoint = "/clinical-attributes"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection
    }
    if sortBy:
        params["sortBy"] = sortBy

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get clinical attributes.")
    
def fetch_clinical_attributes(study_ids, projection="SUMMARY"):
    """
    Fetch clinical attributes from BioPortal for a list of study IDs.
    :param study_ids: List of Study IDs.
    :type study_ids: list of str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched clinical attributes.
    :rtype: pandas.DataFrame
    """
    endpoint = "/clinical-attributes/fetch"
    data = study_ids
    params = {"projection": projection}

    response = requests.post(f"{base_url}{endpoint}", json=data, params=params)
    return check_response(response, "Failed to fetch clinical attributes.")

def get_all_clinical_attributes_in_study(study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="clinicalAttributeId"):
    """
    Get all clinical attributes in the specified study.
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
        Possible values:
        - "clinicalAttributeId"
        - "datatype"
        - "description"
        - "displayName"
        - "patientAttribute"
        - "priority"
        - "studyId"
    :type sortBy: str, optional, default: "clinicalAttributeId"
    :returns: A DataFrame containing clinical attributes in the specified study.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}/clinical-attributes"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get clinical attributes in the specified study.")
    
def get_clinical_attribute_in_study(study_id, clinical_attribute_id):
    """
    Get the specified clinical attribute in the study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param clinical_attribute_id: Clinical Attribute ID, e.g., "CANCER_TYPE".
    :type clinical_attribute_id: str
    :returns: A DataFrame containing information about the specified clinical attribute in the study.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}/clinical-attributes/{clinical_attribute_id}"
    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get the specified clinical attribute in the study.")
