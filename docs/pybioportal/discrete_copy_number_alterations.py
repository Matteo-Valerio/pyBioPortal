import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_discrete_copy_numbers_in_molecular_profile(molecular_profile_id, sample_list_id, discrete_cn_evt_type="HOMDEL_AND_AMP", projection="SUMMARY"):
    """
    Get discrete copy number alterations in a molecular profile by sample list ID. \n
    :param molecular_profile_id: Molecular Profile ID (e.g., "acc_tcga_gistic"). \n
    :type molecular_profile_id: str \n
    :param sample_list_id: Sample List ID (e.g., "acc_tcga_all"). \n
    :type sample_list_id: str \n
    :param discrete_cn_evt_type: Type of the copy number event. \n
        Possible values: \n
            - "ALL": All events.
            - "AMP": Amplification.
            - "DIPLOID": Diploid.
            - "GAIN": Gain.
            - "HETLOSS": Heterozygous loss.
            - "HOMDEL": Homozygous deletion.
            - "HOMDEL_AND_AMP": Homozygous deletion and amplification (default).
    :type discrete_cn_evt_type: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing discrete copy number alterations. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/discrete-copy-number"
    params = {
        "discreteCopyNumberEventType": discrete_cn_evt_type,
        "projection": projection,
        "sampleListId": sample_list_id
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get discrete copy numbers in molecular profile.")


def fetch_discrete_copy_numbers_in_molecular_profile(molecular_profile_id, entrez_gene_ids=None, sample_ids=None, sample_list_id=None, 
                                                     discrete_cn_evt_type="HOMDEL_AND_AMP", projection="SUMMARY"):
    """
    Fetch discrete copy number alterations in a molecular profile by sample list ID. \n
    :param molecular_profile_id: Molecular Profile ID (e.g., "brca_tcga_gistic"). \n
    :type molecular_profile_id: str \n
    :param entrez_gene_ids: List of Entrez Gene IDs (e.g., ["2023", "4853", "54940"]). \n
    :type entrez_gene_ids: list of str \n
    :param sample_ids: List of Sample IDs (e.g., ["TCGA-AR-A1AR-01", "TCGA-E2-A1BC-01"] and sample_list_id set to None). \n
    :type sample_ids: list of str \n
    :param sample_list_id: Sample List ID (e.g., "acc_tcga_all" and sample_ids set to None). \n
    :type sample_list_id: str \n
    :param discrete_cn_evt_type: Type of the copy number event. \n
        Possible values: \n
            - "ALL": All events.
            - "AMP": Amplification.
            - "DIPLOID": Diploid.
            - "GAIN": Gain.
            - "HETLOSS": Heterozygous loss.
            - "HOMDEL": Homozygous deletion.
            - "HOMDEL_AND_AMP": Homozygous deletion and amplification (default).
    :type discrete_cn_evt_type: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing discrete copy number alterations. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/discrete-copy-number/fetch"
    params = {
        "discreteCopyNumberEventType": discrete_cn_evt_type,
        "projection": projection
    }
    
    discreteCopyNumberFilter = {
            "entrezGeneIds": entrez_gene_ids,
            "sampleIds": sample_ids,
            "sampleListId": sample_list_id
           }

    response = requests.post(f"{base_url}{endpoint}", params=params, json=discreteCopyNumberFilter)
    return process_response(response, "Failed to fetch discrete copy numbers in molecular profile.")
