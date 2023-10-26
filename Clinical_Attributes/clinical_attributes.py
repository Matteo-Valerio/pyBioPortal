import requests
import pandas as pd
from config import base_url
import json

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
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection
    }
    if sortBy:
        params["sortBy"] = sortBy
    response = requests.get(f"{base_url}/clinical-attributes", params=params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to get clinical attributes. Status code: {response.status_code}")
    
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
    data = study_ids
    params = {"projection": projection}
    response = requests.post(f"{base_url}/clinical-attributes/fetch", json=data, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch clinical attributes. Status code: {response.status_code}")


#######################
# Clinical Attributes #
#######################
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
    :returns: List of clinical attributes in the specified study.
    :rtype: list[dict]
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
    
    if response.status_code == 200:
        if response.text:  # Check if the response body is not empty            
            try:
                data = response.json()
                return pd.DataFrame(data)
            except ValueError as e:
                print(f"Error decoding the JSON response: {e}")
        else:
            print("Response is empty. No data available.")
    else:
        raise Exception(f"Failed to get clinical attributes in the specified study. Status code: {response.status_code}")
    
def get_clinical_attribute_in_study(study_id, clinical_attribute_id):
    """
    Get the specified clinical attribute in the study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param clinical_attribute_id: Clinical Attribute ID, e.g., "CANCER_TYPE".
    :type clinical_attribute_id: str
    :returns: Information about the specified clinical attribute in the study.
    :rtype: dict
    """
    endpoint = f"/studies/{study_id}/clinical-attributes/{clinical_attribute_id}"
    response = requests.get(f"{base_url}{endpoint}")
    #if response.status_code == 200:
    #    data = response.json()
    #    return pd.DataFrame(data, index=[0])
    #else:
    #    raise Exception(f"Failed to get the specified clinical attribute in the study. Status code: {response.status_code}")
    
    if response.status_code == 200:
        if response.text and response.text != '[]':  # Check if the response body is not empty
            try:
                data = response.json()
                return pd.DataFrame(data, index=[0])
            except ValueError as e:
                print(f"Error decoding the JSON response: {e}")
        else:
            print("Response is empty. No data available.")
    else:
        raise Exception(f"Failed to get the specified clinical attribute in the study. Status code: {response.status_code}")
