import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

####################################
# Discrete Copy Number Alterations #
####################################

def get_discrete_copy_numbers_in_molecular_profile(molecular_profile_id, sample_list_id, discrete_copy_number_event_type="HOMDEL_AND_AMP", projection="SUMMARY"):
    """
    Get discrete copy number alterations in a molecular profile by sample list ID.
    :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_gistic".
    :type molecular_profile_id: str
    :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
    :type sample_list_id: str
    :param discrete_copy_number_event_type: Type of the copy number event.
        - "ALL": All events.
        - "AMP": Amplification.
        - "DIPLOID": Diploid.
        - "GAIN": Gain.
        - "HETLOSS": Heterozygous loss.
        - "HOMDEL": Homozygous deletion.
        - "HOMDEL_AND_AMP": Homozygous deletion and amplification (default).
    :type discrete_copy_number_event_type: str, optional, default: "HOMDEL_AND_AMP"
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: List of discrete copy number alterations.
    :rtype: list[dict]
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/discrete-copy-number"
    params = {
        "discreteCopyNumberEventType": discrete_copy_number_event_type,
        "projection": projection,
        "sampleListId": sample_list_id
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get discrete copy numbers in molecular profile.")


def fetch_discrete_copy_numbers_in_molecular_profile(molecular_profile_id, entrez_gene_ids=None, sample_ids=None, sample_list_id=None, discrete_copy_number_event_type="HOMDEL_AND_AMP", projection="SUMMARY"):
    """
    Fetch discrete copy number alterations in a molecular profile by sample list ID.
    :param molecular_profile_id: Molecular Profile ID, e.g., "brca_tcga_gistic".
    :type molecular_profile_id: str
    :param entrez_gene_ids: List of Entrez Gene IDs, e.g., ["2023", "4853", "54940"].
    :type entrez_gene_ids: list of str
    :param sample_ids: List of Sample IDs, e.g., ["TCGA-AR-A1AR-01", "TCGA-E2-A1BC-01"] and sample_list_id is set to None.
    :type sample_ids: list of str
    :param sample_list_id: Sample List ID, e.g., "acc_tcga_all" and sample_ids is set to None.
    :type sample_list_id: str
    :param discrete_copy_number_event_type: Type of the copy number event.
        - "ALL": All events.
        - "AMP": Amplification.
        - "DIPLOID": Diploid.
        - "GAIN": Gain.
        - "HETLOSS": Heterozygous loss.
        - "HOMDEL": Homozygous deletion.
        - "HOMDEL_AND_AMP": Homozygous deletion and amplification (default).
    :type discrete_copy_number_event_type: str, optional, default: "HOMDEL_AND_AMP"
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :returns: List of discrete copy number alterations.
    :rtype: list[dict]
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/discrete-copy-number/fetch"
    params = {
        "discreteCopyNumberEventType": discrete_copy_number_event_type,
        "projection": projection
    }
    
    discreteCopyNumberFilter = {
            "entrezGeneIds": entrez_gene_ids,
            "sampleIds": sample_ids,
            "sampleListId": sample_list_id
           }

    response = requests.post(f"{base_url}{endpoint}", params=params, json=discreteCopyNumberFilter)
    return check_response(response, "Failed to fetch discrete copy numbers in molecular profile.")
