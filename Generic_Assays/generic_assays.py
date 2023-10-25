import requests
import pandas as pd
from pyBioGate.config import base_url

##################
# Generic Assays #
##################
# Queste nuove funzioni consentono di recuperare i metadati per il generic assay da BioPortal, sia utilizzando l'ID del generic assay che il molecular profile ID
def get_generic_assay_meta_by_id(self, generic_assay_stable_id, projection="SUMMARY"):
    """
    Fetch meta data for a generic assay by its ID.
    :param generic_assay_stable_id: The stable ID of the generic assay.
    :type generic_assay_stable_id: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched meta data for the generic assay.
    :rtype: pandas.DataFrame
    """
    params = {"projection": projection}
    response = requests.get(f"{self.base_url}/generic-assay-meta/generic-assay/{generic_assay_stable_id}", params=params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch meta data for the generic assay. Status code: {response.status_code}")
def get_generic_assay_meta_by_molecular_profile_id(self, molecular_profile_id, projection="SUMMARY"):
    """
    Fetch meta data for a generic assay by molecular profile ID.
    :param molecular_profile_id: Molecular Profile ID.
    :type molecular_profile_id: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched meta data for the generic assay in the specified molecular profile.
    :rtype: pandas.DataFrame
    """
    params = {"projection": projection}
    response = requests.get(f"{self.base_url}/generic-assay-meta/{molecular_profile_id}", params=params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch meta data for the generic assay. Status code: {response.status_code}")
def fetch_generic_assay_meta(self, generic_assay_meta_filter, projection="SUMMARY"):
    """
    Fetch meta data for generic assays based on a filter.
    :param generic_assay_meta_filter: List of Molecular Profile ID or List of Stable ID.
    :type generic_assay_meta_filter: list[str]
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A list of meta data for the generic assays matching the filter criteria.
    :rtype: list[dict]
    """
    params = {"projection": projection}
    data = {"genericAssayMetaFilter": generic_assay_meta_filter}
    response = requests.post(f"{self.base_url}/generic_assay_meta/fetch", params=params, json=data)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch meta data for generic assays. Status code: {response.status_code}")