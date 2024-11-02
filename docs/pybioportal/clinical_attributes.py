import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_all_clinical_attributes(direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all clinical attributes from cBioPortal. \n
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
            - "clinicalAttributeId": Sort by clinical attribute ID.
            - "datatype": Sort by datatype.
            - "description": Sort by description.
            - "displayName": Sort by display name.
            - "patientAttribute": Sort by patient attribute.
            - "priority": Sort by priority.
            - "studyId": Sort by study ID.
    :type sortBy: str \n
    :returns: A DataFrame containing the list of clinical attributes. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/clinical-attributes"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get clinical attributes.")
    
def fetch_clinical_attributes(study_ids, projection="SUMMARY"):
    """
    Fetch clinical attributes from cBioPortal for a list of study IDs. \n
    :param study_ids: List of Study IDs. \n
    :type study_ids: list of str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing the fetched clinical attributes. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/clinical-attributes/fetch"
    data = study_ids
    params = {"projection": projection}

    response = requests.post(f"{base_url}{endpoint}", json=data, params=params)
    return process_response(response, "Failed to fetch clinical attributes.")

def get_all_clinical_attributes_in_study(study_id, direction="ASC", pageNumber=0, pageSize=10000000, 
                                         projection="SUMMARY", sortBy=None):
    """
    Get all clinical attributes in the specified study.
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
            - "clinicalAttributeId"
            - "datatype"
            - "description"
            - "displayName"
            - "patientAttribute"
            - "priority"
            - "studyId"
    :type sortBy: str \n
    :returns: A DataFrame containing clinical attributes in the specified study. \n
    :rtype: pandas.DataFrame \n
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
    return process_response(response, "Failed to get clinical attributes in the specified study.")
    
def get_clinical_attribute_in_study(study_id, clinical_attribute_id):
    """
    Get the specified clinical attribute in the study. \n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
    :param clinical_attribute_id: Clinical Attribute ID (e.g., "CANCER_TYPE"). \n
    :type clinical_attribute_id: str \n
    :returns: A DataFrame containing information about the specified clinical attribute in the study. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/studies/{study_id}/clinical-attributes/{clinical_attribute_id}"
    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get the specified clinical attribute in the study.")
