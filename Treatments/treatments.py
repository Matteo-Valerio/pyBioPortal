import requests
import pandas as pd
from pyBioGate.config import base_url

##############
# Treatments #
##############
def should_display_patient_level_treatments(self, study_ids, tier="Agent"):
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
    data = {"studyIds": study_ids}
    response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to check if patient level treatments should be displayed. Status code: {response.status_code}")
def should_display_sample_level_treatments(self, study_ids, tier="Agent"):
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
    data = {"studyIds": study_ids}
    response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to check if sample level treatments should be displayed. Status code: {response.status_code}")
def get_all_patient_level_treatments(self, study_view_filter, tier="Agent"):
    """
    Get all patient level treatments.
    :param study_view_filter: Study view filter.
    :type study_view_filter: dict
    :param tier: Tier for treatment (default: "Agent").
    :type tier: str
    :values tier: "Agent" - Display treatments by agent.
                 "AgentClass" - Display treatments by agent class.
                 "AgentTarget" - Display treatments by agent target.
    :return: List of patient treatment rows.
    :rtype: list of dict
    """
    endpoint = "/treatments/patient"
    params = {"tier": tier}
    data = {"studyViewFilter": study_view_filter}
    response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get all patient level treatments. Status code: {response.status_code}")
def get_all_sample_level_treatments(self, study_view_filter, tier="Agent"):
    """
    Get all sample level treatments.
    :param study_view_filter: Study view filter.
    :type study_view_filter: dict
    :param tier: Tier for treatment (default: "Agent").
    :type tier: str
    :values tier: "Agent" - Display treatments by agent.
                 "AgentClass" - Display treatments by agent class.
                 "AgentTarget" - Display treatments by agent target.
    :return: List of sample treatment rows.
    :rtype: list of dict
    """
    endpoint = "/treatments/sample"
    params = {"tier": tier}
    data = {"studyViewFilter": study_view_filter}
    response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get all sample level treatments. Status code: {response.status_code}")