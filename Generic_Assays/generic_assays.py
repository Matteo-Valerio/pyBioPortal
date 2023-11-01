import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response, flatten_dict_columns

##################
# Generic Assays #
##################

def fetch_generic_assay_meta(generic_assay_stable_ids=None, molecular_profile_ids=None, projection="SUMMARY"):
    """
    Fetch meta data for generic assays based on List of Molecular Profile ID or List of Stable ID.
    :param generic_assay_stable_ids: List of Stable ID and molecular_profile_ids set to None.
    :type generic_assay_stable_ids: list of str
    :param molecular_profile_ids: List of Molecular Profile IDs and generic_assay_stable_ids set to None.
    :type molecular_profile_ids: list of str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A list of meta data for the generic assays matching the filter criteria.
    :rtype: list[dict]
    """
    params = {"projection": projection}

    genericAssayMetaFilter = {}

    if generic_assay_stable_ids:
        genericAssayMetaFilter['genericAssayStableIds'] = generic_assay_stable_ids
    
    if molecular_profile_ids:
        genericAssayMetaFilter['molecularProfileIds'] = molecular_profile_ids

    response = requests.post(f"{base_url}/generic_assay_meta/fetch", params=params, json=genericAssayMetaFilter)
    df = check_response(response, "Failed to fetch meta data for generic assays.")
    return flatten_dict_columns(df)


def get_generic_assay_meta_by_id(generic_assay_stable_id, projection="SUMMARY"):
    """
    Fetch meta data for a generic assay by its ID.
    :param generic_assay_stable_id: The stable ID of the generic assay.
    :type generic_assay_stable_id: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched meta data for the generic assay.
    :rtype: pandas.DataFrame
    """
    params = {"projection": projection}

    response = requests.get(f"{base_url}/generic-assay-meta/generic-assay/{generic_assay_stable_id}", params=params)
    return check_response(response, "Failed to fetch meta data for the generic assay.")

def get_generic_assay_meta_by_molecular_profile_id(molecular_profile_id, projection="SUMMARY"):
    """
    Fetch meta data for a generic assay by molecular profile ID.
    :param molecular_profile_id: Molecular Profile ID.
    :type molecular_profile_id: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched meta data for the generic assay in the specified molecular profile.
    :rtype: pandas.DataFrame
    """
    params = {"projection": projection}

    response = requests.get(f"{base_url}/generic-assay-meta/{molecular_profile_id}", params=params)
    return check_response(response, "Failed to fetch meta data for the generic assay.")

