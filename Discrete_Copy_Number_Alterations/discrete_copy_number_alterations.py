import requests
import pandas as pd
from pyBioGate.config import base_url

####################################
# Discrete Copy Number Alterations #
####################################

def get_discrete_copy_numbers_in_molecular_profile(self, molecular_profile_id, sample_list_id, discrete_copy_number_event_type="HOMDEL_AND_AMP", projection="SUMMARY"):
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
    response = requests.get(f"{self.base_url}{endpoint}", params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get discrete copy numbers in molecular profile. Status code: {response.status_code}")
def fetch_discrete_copy_numbers_in_molecular_profile(self, molecular_profile_id, sample_list_id, discrete_copy_number_event_type="HOMDEL_AND_AMP", projection="SUMMARY"):
    """
    Fetch discrete copy number alterations in a molecular profile by sample list ID.
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
    endpoint = f"/molecular-profiles/{molecular_profile_id}/discrete-copy-number/fetch"
    params = {
        "discreteCopyNumberEventType": discrete_copy_number_event_type,
        "projection": projection
    }
    data = {
        "discreteCopyNumberFilter": {
            "sampleIds": [sample_list_id],
            "geneIds": []
        }
    }
    response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch discrete copy numbers in molecular profile. Status code: {response.status_code}")