import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_all_molecular_profiles(direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all molecular profiles. \n
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
            - "datatype": Sort by datatype.
            - "description": Sort by description.
            - "molecularAlterationType": Sort by molecular alteration type.
            - "molecularProfileId": Sort by molecular profile ID.
            - "name": Sort by name.
            - "showProfileInAnalysisTab": Sort by profile visibility.
    :type sortBy: str \n
    :returns: A DataFrame containing molecular profiles. \n
    :rtype: pandas.DataFrame \n
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
    return process_response(response, "Failed to get all molecular profiles.")

def get_molecular_profile(molecular_profile_id):
    """
    Get molecular profile. \n
    :param molecular_profile_id: Molecular Profile ID (e.g., "acc_tcga_mutations"). \n
    :type molecular_profile_id: str \n
    :returns: A DataFrame containing molecular profile information. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}"

    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get molecular profile.")
    
def fetch_molecular_profiles(molecular_profile_ids = None, study_ids = None, projection="SUMMARY"):
    """
    Fetch molecular profiles. \n
    :param molecular_profile_ids: List of Molecular Profile IDs (e.g., ["brca_tcga_mrna", "acc_tcga_rna_seq_v2_mrna"]). \n
    :type molecular_profile_ids: list of str \n
    :param study_ids: List of Study IDs (e.g., .["brca_tcga", "acc_tcga"]). \n
    :type study_ids: list of str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing fetched molecular profiles. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/molecular-profiles/fetch"
    params = {"projection": projection}

    molecular_profile_filter = {}

    if molecular_profile_ids:
        molecular_profile_filter['molecularProfileIds'] = molecular_profile_ids

    if study_ids:
        molecular_profile_filter['studyIds'] = study_ids
    
    response = requests.post(f"{base_url}{endpoint}", params=params, json=molecular_profile_filter)
    return process_response(response, "Failed to fetch molecular profiles.")
    
def get_all_molecular_profiles_in_study(study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all molecular profiles in a study. \n
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
    :param sortBy: Name of the property that the result dataframe is sorted by. \n
        Possible values: \n
            - "datatype": Sort by datatype.
            - "description": Sort by description.
            - "molecularAlterationType": Sort by molecular alteration type.
            - "molecularProfileId": Sort by molecular profile ID.
            - "name": Sort by name.
            - "showProfileInAnalysisTab": Sort by profile visibility.
    :type sortBy: str \n
    :returns: A DataFrame containing molecular profiles in the specified study. \n
    :rtype: pandas.DataFrame \n
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
    return process_response(response, "Failed to get molecular profiles in the specified study.")