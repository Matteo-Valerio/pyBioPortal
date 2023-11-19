import requests
from .__config import base_url
from .__aux_funcs import process_response

def fetch_status_display_patient_trts(study_ids, tier="Agent"):
    """
    Check if patient level treatments should be displayed. \n
    :param study_ids: List of Study IDs. \n
    :type study_ids: list of str \n
    :param tier: Tier for treatment. \n
        Possible values: \n
            - "Agent": Display treatments by agent (default).
            - "AgentClass": Display treatments by agent class.
            - "AgentTarget": Display treatments by agent target.
    :type tier: str \n
    :return: True if patient level treatments should be displayed, False otherwise. \n
    :rtype: bool \n
    """
    endpoint = "/treatments/display-patient"
    params = {"tier": tier}

    response = requests.post(f"{base_url}{endpoint}", params=params, json=study_ids)
    return response.json()
    
def fetch_status_display_sample_trts(study_ids, tier="Agent"):
    """
    Check if sample level treatments should be displayed. \n
    :param study_ids: List of Study IDs. \n
    :type study_ids: list of str \n
    :param tier: Tier for treatment. \n
        Possible values: \n
            - "Agent": Display treatments by agent (default).
            - "AgentClass": Display treatments by agent class.
            - "AgentTarget": Display treatments by agent target.
    :type tier: str \n
    :return: True if sample level treatments should be displayed, False otherwise. \n
    :rtype: bool \n
    """
    endpoint = "/treatments/display-sample"
    params = {"tier": tier}

    response = requests.post(f"{base_url}{endpoint}", params=params, json=study_ids)
    return response.json()
    
def fetch_all_patient_level_treatments(study_view_filter, tier="Agent"):
    """
    Fetch all patient level treatments. \n
    :param study_view_filter: Study view filter. \n
    :type study_view_filter: dict \n
        For the structure of the dictionary see the json file 
        StudyViewFilter_Dictionary_Structure on GitHub \n
    :param tier: Tier for treatment. \n
        Possible values: \n
            - "Agent": Display treatments by agent (default).
            - "AgentClass": Display treatments by agent class.
            - "AgentTarget": Display treatments by agent target.
    :type tier: str \n
    :return: A DataFrame containing patient treatment rows. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/treatments/patient"
    params = {"tier": tier}
    
    response = requests.post(f"{base_url}{endpoint}", params=params, json=study_view_filter)
    return process_response(response, "Failed to get all patient level treatments.")
    
def fetch_all_sample_level_treatments(study_view_filter, tier="Agent"):
    """
    Fetch all sample level treatments. \n
    :param study_view_filter: Study view filter. \n
    :type study_view_filter: dict  \n
        For the structure of the dictionary see the json file 
        StudyViewFilter_Dictionary_Structure on GitHub \n
    :param tier: Tier for treatment. \n
        Possible values: \n
            - "Agent": Display treatments by agent (default).
            - "AgentClass": Display treatments by agent class.
            - "AgentTarget": Display treatments by agent target.
    :type tier: str \n
    :return: A DataFrame containing sample treatment rows. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/treatments/sample"
    params = {"tier": tier}

    response = requests.post(f"{base_url}{endpoint}", params=params, json=study_view_filter)
    return process_response(response, "Failed to get all sample level treatments.")