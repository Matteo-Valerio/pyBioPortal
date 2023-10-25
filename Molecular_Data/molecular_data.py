import requests
import pandas as pd
from pyBioGate.config import base_url

##################
# Molecular Data #
##################
def fetch_molecular_data(self, molecular_data_filter, projection="SUMMARY"):
    """
    Fetch molecular data.
    :param molecular_data_filter: List of Molecular Profile ID and Sample ID pairs or
                                  List of MolecularProfile IDs and Entrez Gene IDs.
    :type molecular_data_filter: list[dict]
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: Molecular data.
    :rtype: list[dict]
    """
    endpoint = "/molecular-data/fetch"
    params = {"projection": projection}
    response = requests.post(f"{self.base_url}{endpoint}", json=molecular_data_filter, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch molecular data. Status code: {response.status_code}")
        
##################
# Molecular Data #
##################
def get_all_molecular_data_in_molecular_profile(self, molecular_profile_id, sample_list_id, entrez_gene_id, projection="SUMMARY"):
    """
    Get all molecular data in a molecular profile for a specific gene.
    :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_rna_seq_v2_mrna".
    :type molecular_profile_id: str
    :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
    :type sample_list_id: str
    :param entrez_gene_id: Entrez Gene ID, e.g., 1.
    :type entrez_gene_id: int
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: List of molecular data for the specified gene.
    :rtype: list[dict]
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/molecular-data"
    params = {
        "entrezGeneId": entrez_gene_id,
        "projection": projection,
        "sampleListId": sample_list_id
    }
    response = requests.get(f"{self.base_url}{endpoint}", params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get molecular data in molecular profile. Status code: {response.status_code}")

def fetch_all_molecular_data_in_molecular_profile(self, molecular_profile_id, molecular_data_filter, projection="SUMMARY"):
    """
    Fetch molecular data in a molecular profile for a list of genes.
    :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_rna_seq_v2_mrna".
    :type molecular_profile_id: str
    :param molecular_data_filter: List of Sample IDs/Sample List ID and Entrez Gene IDs.
    :type molecular_data_filter: dict
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: List of molecular data for the specified genes.
    :rtype: list[dict]
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/molecular-data/fetch"
    response = requests.post(f"{self.base_url}{endpoint}", json=molecular_data_filter)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch molecular data in molecular profile. Status code: {response.status_code}")