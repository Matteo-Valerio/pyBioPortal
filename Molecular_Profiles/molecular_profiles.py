import requests
import pandas as pd
from pyBioGate.config import base_url

######################
# Molecular Profiles #
######################
def get_all_molecular_profiles(self, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="datatype"):
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
    :returns: List of molecular profiles.
    :rtype: list[dict]
    """
    endpoint = "/molecular-profiles"
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
        raise Exception(f"Failed to get all molecular profiles. Status code: {response.status_code}")
def fetch_molecular_profiles(self, molecular_profile_filter, projection="SUMMARY"):
    """
    Fetch molecular profiles.
    :param molecular_profile_filter: List of Molecular Profile IDs or List of Study IDs.
    :type molecular_profile_filter: list[str]
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: List of fetched molecular profiles.
    :rtype: list[dict]
    """
    endpoint = "/molecular-profiles/fetch"
    params = {"projection": projection}
    response = requests.post(f"{self.base_url}{endpoint}", json=molecular_profile_filter, params=params, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch molecular profiles. Status code: {response.status_code}")
def get_molecular_profile(self, molecular_profile_id):
    """
    Get molecular profile.
    :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_mutations".
    :type molecular_profile_id: str
    :returns: Molecular profile information.
    :rtype: dict
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}"
    response = requests.get(f"{self.base_url}{endpoint}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get molecular profile. Status code: {response.status_code}")
        
######################
# Molecular Profiles #
######################
def get_all_molecular_profiles_in_study(self, study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="datatype"):
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
    :param sortBy: Name of the property that the result list is sorted by.
        Possible values:
        - "datatype"
        - "description"
        - "molecularAlterationType"
        - "molecularProfileId"
        - "name"
        - "showProfileInAnalysisTab"
    :type sortBy: str, optional, default: "datatype"
    :returns: List of molecular profiles in the specified study.
    :rtype: list[dict]
    """
    endpoint = f"/studies/{study_id}/molecular-profiles"
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
        raise Exception(f"Failed to get molecular profiles in the specified study. Status code: {response.status_code}")