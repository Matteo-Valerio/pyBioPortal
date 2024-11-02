import requests
from .__config import base_url
from .__aux_funcs import process_response

def fetch_clinical_data(attribute_ids, entity_study_ids, clinical_data_type="SAMPLE", projection="SUMMARY", ret_format="WIDE"):
    """
    Fetch clinical data by patient IDs or sample IDs (all studies) from cBioPortal. \n
    :param attribute_ids: List of attribute IDs. \n
            - e.g. for PATIENT data type: \n
                    ["SEX", "RACE"] \n
            - e.g. for SAMPLE data type: \n
                    ["ORGAN_SYSTEM", "SUBTYPE"] \n
    :type attribute_ids: list of str \n
    :param entity_study_ids: List of patient or sample identifiers and study IDs. \n
        Each list should have the following format: \n
            - e.g. for PATIENT data type: \n
                 entity_study_ids = [
                                    {"entity_ids": ["P-0000004", "P-0000950"], 
                                     "study": "msk_met_2021"},
                                    {"entity_ids": ["TCGA-5T-A9QA", "TCGA-A1-A0SB"], 
                                     "study": "brca_tcga"}
                                    ] \n                                    
            - e.g. for SAMPLE data type: \n
                 entity_study_ids = [
                                    {"entity_ids": ["P-0000004-T01-IM3", "P-0000950-T01-IM3"], 
                                     "study": "msk_met_2021"},
                                    {"entity_ids": ["TCGA-5T-A9QA-01", "TCGA-A1-A0SB-01"], 
                                     "study": "brca_tcga"}
                                    ] \n
    :type entity_study_ids: list of dict \n
    :param clinical_data_type: Type of the clinical data. \n
        Possible values: \n
            - "PATIENT": Clinical data for patients.
            - "SAMPLE": Clinical data for samples (default).
    :type clinical_data_type: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :param ret_format: Return format of the dataframe. \n
        Possible values: \n
            - "LONG": Long dataframe with repeated record for patient/sample.
            - "WIDE": Wide dataframe with distinct record for patient/sample (default).
    :type ret_format: str \n
    :returns: A DataFrame containing the fetched clinical data. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/clinical-data/fetch"
    params = {
        "clinicalDataType": clinical_data_type,
        "projection": projection
    }

    clinical_data_filter = {
        "attributeIds": attribute_ids,
        "identifiers": []
    }
    
    for item in entity_study_ids:
        study_id = item["study"]
        entity_ids = item["entity_ids"]
        
        for entity_id in entity_ids:
            identifier = {
                "entityId": entity_id,
                "studyId": study_id
            }
            clinical_data_filter["identifiers"].append(identifier)

    response = requests.post(f"{base_url}{endpoint}", params=params, json=clinical_data_filter,)
    return process_response(response, "Failed to fetch clinical data.", ret_format, attribute_ids)

def get_all_clinical_data_in_study(study_id, attribute_id=None, clinical_data_type="SAMPLE", direction="ASC", 
                                   pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all clinical data in a study. n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
    :param attribute_id: Attribute ID (e.g., "CANCER_TYPE"). \n
    :type attribute_id: str \n
    :param clinical_data_type: Type of clinical data. \n
        Possible values: \n
            - "PATIENT": Clinical data for patients.
            - "SAMPLE": Clinical data for samples (default).
    :type clinical_data_type: str \n
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
            - "value"
    :type sortBy: str \n
    :returns: A DataFrame containing clinical data in the specified study. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/studies/{study_id}/clinical-data"
    params = {
        "clinicalDataType": clinical_data_type,
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    if attribute_id:
        params["attributeId"] = attribute_id
    
    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get clinical data in the specified study.")    
    
def fetch_all_clinical_data_in_study(study_id, attribute_ids=[], ids=[], clinical_data_type="SAMPLE", projection="SUMMARY", ret_format="WIDE"):
    """
    Fetch clinical data by patient IDs or sample IDs in a specific study. \n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
    :param attribute_ids: List of attribute IDs. \n
    :type attribute_ids: list of str \n
    :param ids: List of patient or sample IDs. \n
    :type ids: list of str \n
    :param clinical_data_type: Type of clinical data. \n
        Possible values: \n
            - "PATIENT": Clinical data for patients.
            - "SAMPLE": Clinical data for samples (default).
    :type clinical_data_type: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :param ret_format: Return format of the dataframe. \n
        Possible values: \n
            - "LONG": Long dataframe with repeated record for patient/sample.
            - "WIDE": Wide dataframe with distinct record for patient/sample (default).
    :type ret_format: str \n
    :returns: A DataFrame containing clinical data in the specified study based on the provided filter. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/studies/{study_id}/clinical-data/fetch"
    params = {
        "clinicalDataType": clinical_data_type,
        "projection": projection
    }
    
    clinical_data_filter = {}

    if attribute_ids:
        clinical_data_filter["attributeIds"] = attribute_ids
    
    if ids:
        clinical_data_filter["ids"] = ids
    
    response = requests.post(f"{base_url}{endpoint}", params=params, json=clinical_data_filter)
    return process_response(response, "Failed to fetch clinical data in the specified study.", ret_format, attribute_ids)
    
def get_all_clinical_data_of_patient_in_study(study_id, patient_id, attributeId=None, direction="ASC", 
                                              pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all clinical data of a patient in a study. \n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
    :param patient_id: Patient ID (e.g., "TCGA-OR-A5J2"). \n
    :type patient_id: str \n
    :param attributeId: Attribute ID (e.g., "AGE"). \n
    :type attributeId: str \n
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
            - "value"
    :type sortBy: str \n
    :returns: A DataFrame containing clinical data of the specified patient in the study. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/studies/{study_id}/patients/{patient_id}/clinical-data"
    params = {
        "attributeId": attributeId,
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get clinical data of the specified patient in the study.")

def get_all_clinical_data_of_sample_in_study(study_id, sample_id, attribute_id=None, direction="ASC", pageNumber=0, 
                                             pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all clinical data of a sample in a study. \n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
    :param sample_id: Sample ID (e.g., "TCGA-OR-A5J2-01"). \n
    :type sample_id: str \n
    :param attributeId: Attribute ID (e.g., "CANCER_TYPE"). \n
    :type attributeId: str \n
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
            - "value"
    :type sortBy: str \n
    :returns: A DataFrame containing clinical data for the specified sample in the study. \n
    :rtype: pandas.DataFrame  \n
    """
    endpoint = f"/studies/{study_id}/samples/{sample_id}/clinical-data"
    params = {
        "attributeId": attribute_id,
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get clinical data for the sample.")