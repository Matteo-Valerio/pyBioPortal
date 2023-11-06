import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

##############
# Treatments #
##############
def should_display_patient_level_treatments(study_ids, tier="Agent"):
    """
    Check if patient level treatments should be displayed.
    :param study_ids: List of Study IDs.
    :type study_ids: list of str
    :param tier: Tier for treatment (default: "Agent").
    :type tier: str
    :values tier: "Agent" - Display treatments by agent.
                  "AgentClass" - Display treatments by agent class.
                  "AgentTarget" - Display treatments by agent target.
    :return: True if patient level treatments should be displayed, False otherwise.
    :rtype: bool
    """
    endpoint = "/treatments/display-patient"
    params = {"tier": tier}

    response = requests.post(f"{base_url}{endpoint}", params=params, json=study_ids)
    return response.json()
    
def should_display_sample_level_treatments(study_ids, tier="Agent"):
    """
    Check if sample level treatments should be displayed.
    :param study_ids: List of Study IDs.
    :type study_ids: list of str
    :param tier: Tier for treatment (default: "Agent").
    :type tier: str
    :values tier: "Agent" - Display treatments by agent.
                 "AgentClass" - Display treatments by agent class.
                 "AgentTarget" - Display treatments by agent target.
    :return: True if sample level treatments should be displayed, False otherwise.
    :rtype: bool
    """
    endpoint = "/treatments/display-sample"
    params = {"tier": tier}

    response = requests.post(f"{base_url}{endpoint}", params=params, json=study_ids)
    return response.json()
    
def fetch_all_patient_level_treatments(study_view_filter, tier="Agent"):
    """
    Fetch all patient level treatments.
    :param study_view_filter: Study view filter.
    :type study_view_filter: dict
        For the structure of the dictionary see the json file 
        StudyViewFilter_Dictionary_Structure on GitHub
    :param tier: Tier for treatment (default: "Agent").
    :type tier: str
    :values tier: "Agent" - Display treatments by agent.
                 "AgentClass" - Display treatments by agent class.
                 "AgentTarget" - Display treatments by agent target.
    :return: A DataFrame containing patient treatment rows.
    :rtype: pandas.DataFrame
    """
    endpoint = "/treatments/patient"
    params = {"tier": tier}
    
    response = requests.post(f"{base_url}{endpoint}", params=params, json=study_view_filter)
    return check_response(response, "Failed to get all patient level treatments.")
    
def fetch_all_sample_level_treatments(study_view_filter, tier="Agent"):
    """
    Fetch all sample level treatments.
    :param study_view_filter: Study view filter.
    :type study_view_filter: dict 
        For the structure of the dictionary see the json file 
        StudyViewFilter_Dictionary_Structure on GitHub
    :param tier: Tier for treatment (default: "Agent").
    :type tier: str
    :values tier: "Agent" - Display treatments by agent.
                 "AgentClass" - Display treatments by agent class.
                 "AgentTarget" - Display treatments by agent target.
    :return: A DataFrame containing sample treatment rows.
    :rtype: pandas.DataFrame
    """
    endpoint = "/treatments/sample"
    params = {"tier": tier}

    response = requests.post(f"{base_url}{endpoint}", params=params, json=study_view_filter)
    return check_response(response, "Failed to get all sample level treatments.")