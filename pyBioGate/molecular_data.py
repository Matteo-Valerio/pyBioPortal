import requests
from .__config import base_url
from .__aux_funcs import process_response

def fetch_molecular_data(entrez_gene_ids=None, molecular_profile_ids=None, sample_molecular_identifiers=None, projection="SUMMARY"):
    """
    Fetch molecular data. \n
    :param entrez_gene_ids: List of Entrez Gene IDs (e.g., ["672", "675"]). \n
    :type entrez_gene_ids: list of str \n
    :param molecular_profile_ids: List of MolecularProfile IDs (e.g., ["brca_tcga_mrna", "acc_tcga_rna_seq_v2_mrna"]). \n
    :type molecular_profile_ids: list of str \n
    :param sample_molecular_identifiers: List of Molecular Profile ID and Sample ID pairs. \n
    :type sample_molecular_identifiers: list of dict \n
        Each dict should have the following format: \n
            sample_molecular_identifiers = [
                                           {"molecular_profile_id": "brca_tcga_mrna", 
                                            "sample_ids": ["TCGA-AR-A1AR-01","TCGA-BH-A1EO-01"]},
                                           {"molecular_profile_id": "acc_tcga_rna_seq_v2_mrna", 
                                            "sample_ids": ["TCGA-OR-A5J1-01","TCGA-OR-A5J2"]}
                                           ]
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing molecular data. \n
    :rtype: pandas.DataFrame \n
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

    response = requests.post(f"{base_url}{endpoint}", params=params, json=molecular_data_filter)
    return process_response(response, "Failed to fetch molecular data.")
        
def get_all_molecular_data_in_molecular_profile(molecular_profile_id, sample_list_id, entrez_gene_id, projection="SUMMARY"):
    """
    Get all molecular data in a molecular profile for a specific gene. \n
    :param molecular_profile_id: Molecular Profile ID (e.g., "acc_tcga_rna_seq_v2_mrna"). \n
    :type molecular_profile_id: str \n
    :param sample_list_id: Sample List ID (e.g., "acc_tcga_all"). \n
    :type sample_list_id: str \n
    :param entrez_gene_id: Entrez Gene ID (e.g., "1"). \n
    :type entrez_gene_id: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing molecular data for the specified gene. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/molecular-data"
    params = {
        "entrezGeneId": entrez_gene_id,
        "projection": projection,
        "sampleListId": sample_list_id
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get molecular data in molecular profile.")

def fetch_all_molecular_data_in_molecular_profile(molecular_profile_id, entrez_gene_ids = None, sample_ids = None, 
                                                  sample_list_id = None, projection="SUMMARY"):
    """
    Fetch molecular data in a molecular profile for a list of genes. \n
    :param molecular_profile_id: Molecular Profile ID (e.g., "acc_tcga_rna_seq_v2_mrna"). \n
    :type molecular_profile_id: str \n
    :param entrez_gene_ids: List of Entrez Gene IDs (e.g., ["672","675"]). \n
    :type entrez_gene_ids: list of str \n
    :param sample_ids: List of Sample IDs (e.g., ["TCGA-AR-A1AR-01","TCGA-BH-A1EO-01"]). \n
    :type sample_ids: list of str \n
    :param sample_list_id: Sample List ID (e.g., "brca_tcga_all"). \n
    :type sample_list_id: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing molecular data for the specified genes. \n
    :rtype: pandas.DataFrame \n
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

    response = requests.post(f"{base_url}{endpoint}", params=params, json=molecular_data_filter)
    return process_response(response, "Failed to fetch molecular data in molecular profile.")