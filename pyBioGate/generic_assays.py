import requests
from .__config import base_url
from .__aux_funcs import process_response

def fetch_generic_assay_meta(generic_assay_stable_ids=None, molecular_profile_ids=None, projection="SUMMARY"):
    """
    Fetch meta data for generic assays based on a filter. \n
    :param generic_assay_stable_ids: List of Stable IDs (e.g., ["TULP4_pS563", "TEP1_pS397", "ALAD_214_215_1_1_S215"]). \n
    :type generic_assay_stable_ids: list of str \n
    :param molecular_profile_ids: List of Molecular Profile IDs (e.g., ["brca_tcga_phosphoprotein_quantification","brain_cptac_2020_phosphoprotein"]). \n
    :type molecular_profile_ids: list of str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing meta data for the generic assays matching the filter criteria. \n
    :rtype: pandas.DataFrame \n
    """
    params = {"projection": projection}

    generic_assay_meta_filter = {}

    if generic_assay_stable_ids:
        generic_assay_meta_filter["genericAssayStableIds"] = generic_assay_stable_ids

    if molecular_profile_ids:
        generic_assay_meta_filter["molecularProfileIds"] = molecular_profile_ids

    response = requests.post(f"{base_url}/generic_assay_meta/fetch", params=params, json=generic_assay_meta_filter)
    return process_response(response, "Failed to fetch meta data for generic assays.")

def get_generic_assay_meta_by_id(generic_assay_stable_id, projection="SUMMARY"):
    """
    Fetch meta data for a generic assay by its ID. \n
    :param generic_assay_stable_id: The stable ID of the generic assay. \n
    :type generic_assay_stable_id: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing the fetched meta data for the generic assay. \n
    :rtype: pandas.DataFrame \n
    """
    params = {"projection": projection}

    response = requests.get(f"{base_url}/generic-assay-meta/generic-assay/{generic_assay_stable_id}", params=params)
    return process_response(response, "Failed to fetch meta data for the generic assay.")

def get_generic_assay_meta_by_molecular_profile_id(molecular_profile_id, projection="SUMMARY"):
    """
    Fetch meta data for a generic assay by molecular profile ID. \n
    :param molecular_profile_id: Molecular Profile ID. \n
    :type molecular_profile_id: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing the fetched meta data for the generic assay in the specified molecular profile. \n
    :rtype: pandas.DataFrame \n
    """
    params = {"projection": projection}

    response = requests.get(f"{base_url}/generic-assay-meta/{molecular_profile_id}", params=params)
    return process_response(response, "Failed to fetch meta data for the generic assay.")