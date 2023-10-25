import requests
import pandas as pd
from pyBioGate.config import base_url

###################
# Gene Panel Data #
###################
# Queste nuove funzioni consentono di ottenere dati relativi ai pannelli genetici da BioPortal. Le docstring contengono dettagli sui parametri, inclusi i possibili valori e il significato dei parametri. Puoi utilizzare queste funzioni per accedere ai dati sui pannelli genetici da BioPortal.
def fetch_gene_panel_data(gene_panel_data_filter):
    """
    Fetch gene panel data from BioPortal.
    :param gene_panel_data_filter: Gene panel data filter object.
    :type gene_panel_data_filter: dict
        Example format:
        {
            "filterProperty1": "value1",
            "filterProperty2": "value2",
            ...
        }
    :returns: A DataFrame containing the fetched gene panel data.
    :rtype: pandas.DataFrame
    """
    data = gene_panel_data_filter
    response = requests.post(f"{base_url}/gene-panel-data/fetch", json=data)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch gene panel data. Status code: {response.status_code}")

###################
# Gene Panel Data #
###################
def get_gene_panel_data(molecular_profile_id, gene_panel_data_filter):
    """
    Get gene panel data for a specific molecular profile.
    :param molecular_profile_id: Molecular Profile ID, e.g., "nsclc_unito_2016_mutations".
    :type molecular_profile_id: str
    :param gene_panel_data_filter: List of Sample IDs/Sample List ID and Entrez Gene IDs.
    :type gene_panel_data_filter: dict
    :returns: Gene panel data.
    :rtype: list[dict]
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/gene-panel-data/fetch"
    response = requests.post(f"{base_url}{endpoint}", json=gene_panel_data_filter)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get gene panel data. Status code: {response.status_code}")