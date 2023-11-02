import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

##################
# Molecular Data #
##################
def fetch_molecular_data(entrez_gene_ids=None, molecular_profile_ids=None, sample_molecular_identifiers=None, projection="SUMMARY"):
    """
    Fetch molecular data.
    :param entrez_gene_ids: List of Entrez Gene IDs, e.g., ["672", "675"]
    :type entrez_gene_ids: list of str
    :param molecular_profile_ids: List of MolecularProfile IDs, e.g., ["brca_tcga_mrna", "acc_tcga_rna_seq_v2_mrna"]
    :type molecular_profile_ids: list of str
    :param sample_molecular_identifiers: List of Molecular Profile ID and Sample ID pairs.
    :type sample_molecular_identifiers: list of dict
        Each dict should have the following format:
            sample_molecular_identifiers = [
                                           {"molecular_profile_id": "brca_tcga_mrna", 
                                            "sample_ids": ["TCGA-AR-A1AR-01","TCGA-BH-A1EO-01"]},
                                           {"molecular_profile_id": "acc_tcga_rna_seq_v2_mrna", 
                                            "sample_ids": ["TCGA-OR-A5J1-01","TCGA-OR-A5J2"]}
                                           ]
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing molecular data.
    :rtype: pandas.DataFrame
    """
    endpoint = "/molecular-data/fetch"
    params = {"projection": projection}

    molecular_data_filter = {}

    if entrez_gene_ids:
        molecular_data_filter['entrezGeneIds'] = entrez_gene_ids
    
    if molecular_profile_ids:
        molecular_data_filter['molecularProfileIds'] = molecular_profile_ids

    if sample_molecular_identifiers:
        molecular_data_filter['sampleMolecularIdentifiers'] = []

        for item in sample_molecular_identifiers:
            molec_prof_id = item["molecular_profile_id"]
            sample_ids = item["sample_ids"]

            for sample_id in sample_ids:
                identifier = {
                    "molecularProfileId": molec_prof_id,
                    "sampleId": sample_id
                }
                molecular_data_filter["sampleMolecularIdentifiers"].append(identifier)

    response = requests.post(f"{base_url}{endpoint}", json=molecular_data_filter, params=params)
    return check_response(response, "Failed to fetch molecular data.")
        
def get_all_molecular_data_in_molecular_profile(molecular_profile_id, sample_list_id, entrez_gene_id, projection="SUMMARY"):
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
    :returns: A DataFrame containing molecular data for the specified gene.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/molecular-data"
    params = {
        "entrezGeneId": entrez_gene_id,
        "projection": projection,
        "sampleListId": sample_list_id
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get molecular data in molecular profile.")

def fetch_all_molecular_data_in_molecular_profile(molecular_profile_id, entrez_gene_ids = None, sample_ids = None, sample_list_id = None, projection="SUMMARY"):
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
    :returns: A DataFrame containing molecular data for the specified genes.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/molecular-data/fetch"
    params = {
        "projection": projection,
    }

    molecular_data_filter = {}

    if entrez_gene_ids:
        molecular_data_filter['entrezGeneIds'] = entrez_gene_ids
    
    if sample_ids:
        molecular_data_filter['sampleIds'] = sample_ids

    if sample_list_id:
        molecular_data_filter['sampleListId'] = sample_list_id

    response = requests.post(f"{base_url}{endpoint}", json=molecular_data_filter, params=params)
    return check_response(response, "Failed to fetch molecular data in molecular profile.")