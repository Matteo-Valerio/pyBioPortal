import requests
import pandas as pd
from pyBioGate.config import base_url

######################
# Generic Assay Data #
######################
# Questa nuova funzione consente di ottenere dati di un assaggio generico in un profilo molecolare specifico da BioPortal.
def get_generic_assay_data_in_molecular_profile(self, molecular_profile_id, generic_assay_stable_id, projection="SUMMARY"):
    """
    Get generic assay data in a molecular profile from BioPortal.
    :param molecular_profile_id: Molecular Profile ID.
    :type molecular_profile_id: str
    :param generic_assay_stable_id: Generic Assay stable ID.
    :type generic_assay_stable_id: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the generic assay data in the specified molecular profile.
    :rtype: pandas.DataFrame
    """
    params = {"projection": projection}
    response = requests.get(f"{self.base_url}/generic-assay-data/{molecular_profile_id}/generic-assay/{generic_assay_stable_id}", params=params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to get generic assay data. Status code: {response.status_code}")

def fetch_generic_assay_data(self, generic_assay_data_multiple_study_filter, projection="SUMMARY"):
    """
    Fetch generic assay data from multiple molecular profiles in BioPortal.
    :param generic_assay_data_multiple_study_filter: List of Molecular Profile ID and Sample ID pairs
        or List of MolecularProfile IDs and Generic Assay IDs.
    :type generic_assay_data_multiple_study_filter: dict
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched generic assay data.
    :rtype: pandas.DataFrame
    """
    params = {"projection": projection}
    response = requests.post(f"{self.base_url}/generic_assay_data/fetch", json=generic_assay_data_multiple_study_filter, params=params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch generic assay data. Status code: {response.status_code}")
def fetch_generic_assay_data_in_molecular_profile(self, molecular_profile_id, generic_assay_data_filter, projection="SUMMARY"):
    """
    Fetch generic assay data in a specific molecular profile from BioPortal.
    :param molecular_profile_id: Molecular Profile ID.
    :type molecular_profile_id: str
    :param generic_assay_data_filter: List of Sample IDs/Sample List ID and Generic Assay IDs.
    :type generic_assay_data_filter: dict
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched generic assay data in the specified molecular profile.
    :rtype: pandas.DataFrame
    """
    params = {"projection": projection}
    response = requests.post(f"{self.base_url}/generic_assay_data/{molecular_profile_id}/fetch", json=generic_assay_data_filter, params=params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch generic assay data. Status code: {response.status_code}")