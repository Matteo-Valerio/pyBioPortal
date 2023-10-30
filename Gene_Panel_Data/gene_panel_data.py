import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

###################
# Gene Panel Data #
###################
def fetch_gene_panel_data(molecular_profile_ids=None, molecular_prof_sample_ids=None):
    """
    Fetch gene panel data from BioPortal.
    :param molecular_profile_ids: List of Molecular Profile IDs, e.g., ["brca_tcga_gistic", "brca_tcga_mutations", "acc_tcga_gistic"].
    :type molecular_profile_ids: list of str
    :param molecular_prof_sample_ids: List of Molecular Profile IDs, e.g., ["brca_tcga_gistic", "brca_tcga_mutations", "acc_tcga_gistic"].
    :type molecular_prof_sample_ids: list of dict
        Each dict should have the following format:
            molecular_prof_sample_ids = [
                                        {"molecular_profile_id": "brca_tcga_gistic",  
                                         "sample_ids": ["TCGA-AR-A1AR-01", "TCGA-E2-A1BC-01"]},
                                        {"molecular_profile_id": "brca_tcga_mutations", 
                                         "sample_ids": ["TCGA-AR-A1AR-01", "TCGA-E2-A1BC-01"]},
                                        {"molecular_profile_id": "msk_met_2021_mutations", 
                                         "sample_ids": ["P-0000004-T01-IM3", "P-0000950-T01-IM3"]}
                                        ]
    :returns: A DataFrame containing the fetched gene panel data.
    :rtype: pandas.DataFrame
    """
    endpoint = "/gene-panel-data/fetch"

    gene_panel_data_filter = {}

    if molecular_profile_ids:
        gene_panel_data_filter['molecularProfileIds'] = molecular_profile_ids
    
    if molecular_prof_sample_ids:
        gene_panel_data_filter['sampleMolecularIdentifiers'] = []
    
        for item in molecular_prof_sample_ids:
            molec_prof_id = item["molecular_profile_id"]
            sample_ids = item["sample_ids"]

            for sample_id in sample_ids:
                identifier = {
                    "molecularProfileId": molec_prof_id,
                    "sampleId": sample_id
                }
                gene_panel_data_filter["sampleMolecularIdentifiers"].append(identifier)

    response = requests.post(f"{base_url}{endpoint}", json=gene_panel_data_filter)
    return check_response(response, "Failed to fetch gene panel data.")

def get_gene_panel_data(molecular_profile_id, sample_ids=None, sample_list_id=None):
    """
    Get gene panel data for a specific molecular profile.
    :param molecular_profile_id: Molecular Profile ID, e.g., "brca_tcga_mutations".
    :type molecular_profile_id: str
    :param sample_ids: List of Sample IDs, e.g., ["TCGA-AR-A1AR-01", "TCGA-E2-A1BC-01"] and sample_list_id set to None. #and Entrez Gene IDs.
    :type sample_ids: list of str
    :param sample_list_id: Sample List ID, e.g., "brca_tcga_all" and sample_ids set to None.
    :type sample_list_id: str
    :returns: A DataFrame containing the fetched gene panel data.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/gene-panel-data/fetch"

    gene_panel_data_filter = {
            "sampleIds": sample_ids,
            "sampleListId": sample_list_id
           }

    response = requests.post(f"{base_url}{endpoint}", json=gene_panel_data_filter)
    return check_response(response, "Failed to get gene panel data.")