import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

######################
# Generic Assay Data #
######################

def fetch_generic_assay_data_in_molecular_profile(molecular_profile_id, generic_assay_stable_ids=None, sample_ids=None, sample_list_id=None, projection="SUMMARY"):
    """
    Fetch generic assay data in a specific molecular profile from BioPortal.
    :param molecular_profile_id: Molecular Profile ID, e.g., "brca_tcga_phosphoprotein_quantification".
    :type molecular_profile_id: str
    :param generic_assay_stable_ids: List of Generic Assays IDs, e.g., ["TULP4_pS563", "TEP1_pS397"].
    :type generic_assay_stable_ids: List of str
    :param sample_ids: List of Sample IDs, e.g., ["TCGA-C8-A130-01", "TCGA-C8-A134-01"] and sample_list_id set to None.
    :type sample_ids: List of str
    :param sample_list_id: Sample List ID, e.g., "brca_tcga_all" and sample_ids set to None.
    :type sample_list_id: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched generic assay data in the specified molecular profile.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/generic_assay_data/{molecular_profile_id}/fetch"
    params = {"projection": projection}

    generic_assay_data_filter = {}

    if generic_assay_stable_ids:
        generic_assay_data_filter['genericAssayStableIds'] = generic_assay_stable_ids
    
    if sample_ids:
        generic_assay_data_filter['sampleIds'] = sample_ids

    if sample_list_id:
        generic_assay_data_filter['sampleListId'] = sample_list_id

    response = requests.post(f"{base_url}{endpoint}", json=generic_assay_data_filter, params=params)
    return check_response(response, "Failed to fetch generic assay data.")

def fetch_generic_assay_data(generic_assay_stable_ids=None, molecular_profile_ids=None, sample_molecular_identifiers=None, projection="SUMMARY"):
    """
    Fetch generic assay data from multiple molecular profiles in BioPortal providing 
    List of Molecular Profile ID and Sample ID pairs or List of Molecular Profile IDs and Generic Assay IDs.
    :param generic_assay_stable_ids: List of Generic Assay IDs, e.g. ["TULP4_pS563", "TEP1_pS397"]
    :type generic_assay_stable_ids: list of str
    :param molecular_profile_ids: List of Molecular Profile IDs, e.g. ["brca_tcga_phosphoprotein_quantification","brain_cptac_2020_phosphoprotein"]
    :type molecular_profile_ids: list of str
    :param sample_molecular_identifiers: List of Molecular Profile ID and Sample IDs pairs. 
    :type sample_molecular_identifiers: list of dict
        Each dict should have the following format:
            molecular_prof_sample_ids = [
                                        {"molecular_profile_id": "brca_tcga_phosphoprotein_quantification",  
                                         "sample_ids": ["TCGA-C8-A130-01", "TCGA-C8-A134-01"]},
                                        {"molecular_profile_id": "brain_cptac_2020_phosphoprotein", 
                                         "sample_ids": ["7316-101", "7316-109"]}
                                        ]

    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched generic assay data.
    :rtype: pandas.DataFrame
    """
    endpoint = "/generic_assay_data/fetch"
    params = {"projection": projection}

    generic_assay_data_multiple_study_filter = {}

    if generic_assay_stable_ids:
        generic_assay_data_multiple_study_filter['genericAssayStableIds'] = generic_assay_stable_ids
    
    if molecular_profile_ids:
        generic_assay_data_multiple_study_filter['molecularProfileIds'] = molecular_profile_ids

    if sample_molecular_identifiers:
        generic_assay_data_multiple_study_filter['sampleMolecularIdentifiers'] = []

        for item in sample_molecular_identifiers:
            molec_prof_id = item["molecular_profile_id"]
            sample_ids = item["sample_ids"]

            for sample_id in sample_ids:
                identifier = {
                    "molecularProfileId": molec_prof_id,
                    "sampleId": sample_id
                }
                generic_assay_data_multiple_study_filter["sampleMolecularIdentifiers"].append(identifier)


    response = requests.post(f"{base_url}{endpoint}", json=generic_assay_data_multiple_study_filter, params=params)
    return check_response(response, "Failed to fetch generic assay data.")

def get_generic_assay_data_in_molecular_profile(molecular_profile_id, generic_assay_stable_id, projection="SUMMARY"):
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
    endpoint = f"/generic-assay-data/{molecular_profile_id}/generic-assay/{generic_assay_stable_id}"
    params = {"projection": projection}

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get generic assay data.")