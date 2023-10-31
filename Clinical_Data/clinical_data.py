import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

# Auxiliary function
def process_response(response, ret_format, attribute_ids):
    if response.text and response.text != '[]':  # Check if the response body is not empty
        try:
            data = response.json()
            df = pd.DataFrame(data)
            if ret_format == 'WIDE':
                cols_to_group = df.columns[:-2]
                df = df.pivot(index=cols_to_group, columns='clinicalAttributeId', values='value')              
                df.reset_index(inplace=True)
                # check if all attributes has been retrieved
                miss_attr = [col for col in attribute_ids if col not in df.columns]
                if miss_attr != []:
                    print("Attributes not present: " + ", ".join(map(str, miss_attr)))
            else:
                miss_attr = [attr for attr in attribute_ids if attr not in set(df.clinicalAttributeId)]
                if miss_attr != []:
                    print("Attributes not present: " + ", ".join(map(str, miss_attr)))
            return df
        except ValueError as e:
            print(f"Error decoding the JSON response: {e}")
    else:
        print("Response is empty. No data available.")

#################
# Clinical Data #
#################
def fetch_clinical_data(attribute_ids, entity_study_ids, clinical_data_type="SAMPLE", projection="SUMMARY", ret_format="WIDE"):
    """
    Fetch clinical data by patient IDs or sample IDs (all studies) from BioPortal.
    :param attribute_ids: List of attribute IDs        
    :type attribute_ids: list of str
        e.g. for PATIENT data type ["SEX", "RACE"]
        e.g. for SAMPLE data type ["ORGAN_SYSTEM", "SUBTYPE"]
    :param entity_study_ids: List of patient or sample identifiers and study IDs        
    :type entity_study_ids: list of dict
        Each list should have the following format:
        e.g. for PATIENT data type:
            entity_study_ids = [
                               {"entity_ids": ["P-0000004", "P-0000950"], 
                                "study": "msk_met_2021"},
                               {"entity_ids": ["TCGA-5T-A9QA", "TCGA-A1-A0SB"], 
                                "study": "brca_tcga"}
                               ]
        e.g. for SAMPLE data type:
            entity_study_ids = [
                               {"entity_ids": ["P-0000004-T01-IM3", "P-0000950-T01-IM3"], 
                                "study": "msk_met_2021"},
                               {"entity_ids": ["TCGA-5T-A9QA-01", "TCGA-A1-A0SB-01"], 
                                "study": "brca_tcga"}
                               ]
    :param clinical_data_type: Type of the clinical data.
        - "PATIENT": Clinical data for patients.
        - "SAMPLE": Clinical data for samples (default).
    :type clinical_data_type: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :param ret_format: Return format of the dataframe.
        - "LONG": Long dataframe with repeated record for patient/sample.
        - "WIDE": Wide dataframe with distinct record for patient/sample (default).
    :type ret_format: str
    :returns: A DataFrame containing the fetched clinical data.
    :rtype: pandas.DataFrame
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

    response = requests.post(f"{base_url}{endpoint}", json=clinical_data_filter, params=params)    
    
    if response.status_code == 200:
        return process_response(response, ret_format, attribute_ids)
    else:
        raise Exception(f"Failed to fetch clinical data. Status code: {response.status_code}")

#################
# Clinical Data #
#################
def get_all_clinical_data_in_study(study_id, attribute_id=None, clinical_data_type="SAMPLE", direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="clinicalAttributeId"):
    """
    Get all clinical data in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param attribute_id: Attribute ID, e.g., "CANCER_TYPE".
    :type attribute_id: str, optional
    :param clinical_data_type: Type of clinical data.
        - "PATIENT": Clinical data for patients.
        - "SAMPLE": Clinical data for samples (default).
    :type clinical_data_type: str, optional, default: "SAMPLE"
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
        - "value"
    :type sortBy: str, optional, default: "clinicalAttributeId"
    :returns: List of clinical data in the specified study.
    :rtype: list[dict]
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
    return check_response(response, "Failed to get clinical data in the specified study.")    
    
def fetch_all_clinical_data_in_study(study_id, attribute_ids=[], ids=[], clinical_data_type="SAMPLE", projection="SUMMARY", ret_format="WIDE"):
    """
    Fetch clinical data by patient IDs or sample IDs in a specific study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param attribute_ids: List of patient or sample IDs.
    :type attribute_ids: list[str]
    :param ids: List of attribute IDs.
    :type ids: list[str]
    :param clinical_data_type: Type of clinical data.
        - "PATIENT": Clinical data for patients.
        - "SAMPLE": Clinical data for samples (default).
    :type clinical_data_type: str, optional, default: "SAMPLE"
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :param ret_format: Return format of the dataframe.
        - "LONG": Long dataframe with repeated record for patient/sample.
        - "WIDE": Wide dataframe with distinct record for patient/sample (default).
    :type ret_format: str
    :returns: List of clinical data in the specified study based on the provided filter.
    :rtype: list[dict]
    """
    endpoint = f"/studies/{study_id}/clinical-data/fetch"
    params = {
        "clinicalDataType": clinical_data_type,
        "projection": projection
    }
    
    clinical_data_filter = {
        "attributeIds": attribute_ids,
        "ids": ids
    }

    if attribute_ids == [] or ids == []:
        print('attribute_ids or ids list is empty')
        return
    
    response = requests.post(f"{base_url}{endpoint}", params=params, json=clinical_data_filter)
    if response.status_code == 200:
        return process_response(response, ret_format, attribute_ids)
    else:
        raise Exception(f"Failed to fetch clinical data in the specified study. Status code: {response.status_code}")

#################
# Clinical Data #
#################
def get_all_clinical_data_of_patient_in_study(study_id, patient_id, attributeId=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="clinicalAttributeId"):
    """
    Get all clinical data of a patient in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param patient_id: Patient ID, e.g., "TCGA-OR-A5J2".
    :type patient_id: str
    :param attributeId: Attribute ID, e.g., "AGE".
    :type attributeId: str, optional
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
        - "clinicalAttributeId": Sort by clinical attribute ID.
        - "value": Sort by clinical data value.
    :type sortBy: str, optional, default: "clinicalAttributeId"
    :returns: List of clinical data of the specified patient in the study.
    :rtype: list[dict]
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
    return check_response(response, "Failed to get clinical data of the specified patient in the study.")

    #if response.status_code == 200:
    #    if response.text and response.text != '[]':  # Check if the response body is not empty
    #        try:
    #            data = response.json()
    #            return pd.DataFrame(data)
    #        except ValueError as e:
    #            print(f"Error decoding the JSON response: {e}")
    #    else:
    #        print("Response is empty. No data available.")
    #else:
    #    raise Exception(f"Failed to get clinical data of the specified patient in the study. Status code: {response.status_code}")

#################
# Clinical Data #
#################
def get_all_clinical_data_of_sample_in_study(study_id, sample_id, attributeId=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="clinicalAttributeId"):
    """
    Get all clinical data of a sample in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param sample_id: Sample ID, e.g., "TCGA-OR-A5J2-01".
    :type sample_id: str
    :param attributeId: Attribute ID, e.g., "CANCER_TYPE".
    :type attributeId: str, optional
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
        - "clinicalAttributeId": Sort by clinical attribute ID.
        - "value": Sort by clinical data value.
    :type sortBy: str, optional, default: "clinicalAttributeId"
    :returns: List of clinical data for the specified sample in the study.
    :rtype: list[dict]
    """
    endpoint = f"/studies/{study_id}/samples/{sample_id}/clinical-data"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
    }
    if attributeId:
        params["attributeId"] = attributeId
    if sortBy:
        params["sortBy"] = sortBy

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get clinical data for the sample.")

    #if response.status_code == 200:
    #    if response.text and response.text != '[]':  # Check if the response body is not empty
    #        try:
    #            data = response.json()
    #            return pd.DataFrame(data)
    #        except ValueError as e:
    #            print(f"Error decoding the JSON response: {e}")
    #    else:
    #        print("Response is empty. No data available.")
    #else:
    #    raise Exception(f"Failed to get clinical data for the sample. Status code: {response.status_code}")
