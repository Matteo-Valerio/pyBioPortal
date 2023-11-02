import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

######################
# Molecular Profiles #
######################
def get_all_molecular_profiles(direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="datatype"):
    """
    Get all molecular profiles.
    :param direction: Direction of the sort.
        - "ASC": Sort in ascending order (default).
        - "DESC": Sort in descending order.
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
        - "datatype": Sort by datatype.
        - "description": Sort by description.
        - "molecularAlterationType": Sort by molecular alteration type.
        - "molecularProfileId": Sort by molecular profile ID.
        - "name": Sort by name.
        - "showProfileInAnalysisTab": Sort by profile visibility.
    :type sortBy: str, optional, default: "datatype"
    :returns: A DataFrame containing molecular profiles.
    :rtype: pandas.DataFrame
    """
    endpoint = "/molecular-profiles"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get all molecular profiles.")

def get_molecular_profile(molecular_profile_id):
    """
    Get molecular profile.
    :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_mutations".
    :type molecular_profile_id: str
    :returns: A DataFrame containing molecular profile information.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}"

    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get molecular profile.")
    
def fetch_molecular_profiles(molecular_profile_ids = None, study_ids = None, projection="SUMMARY"):
    """
    Fetch molecular profiles.
    :param molecular_profile_ids: List of Molecular Profile IDs, e.g., ["brca_tcga_mrna", "acc_tcga_rna_seq_v2_mrna"]
    :type molecular_profile_ids: list of str
    :param study_ids: List of Study IDs, e.g., .["brca_tcga", "acc_tcga"]
    :type study_ids: list of str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: A DataFrame containing fetched molecular profiles.
    :rtype: pandas.DataFrame
    """
    endpoint = "/molecular-profiles/fetch"
    params = {"projection": projection}

    molecular_profile_filter = {}

    if molecular_profile_ids:
        molecular_profile_filter['molecularProfileIds'] = molecular_profile_ids

    if study_ids:
        molecular_profile_filter['studyIds'] = study_ids
    
    response = requests.post(f"{base_url}{endpoint}", json=molecular_profile_filter, params=params)
    return check_response(response, "Failed to fetch molecular profiles.")
    
def get_all_molecular_profiles_in_study(study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="datatype"):
    """
    Get all molecular profiles in a study.
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
    :param sortBy: Name of the property that the result dataframe is sorted by.
        Possible values:
        - "datatype" (default)
        - "description"
        - "molecularAlterationType"
        - "molecularProfileId"
        - "name"
        - "showProfileInAnalysisTab"
    :type sortBy: str, optional, default: "datatype"
    :returns: A DataFrame containing molecular profiles in the specified study.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/studies/{study_id}/molecular-profiles"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get molecular profiles in the specified study.")