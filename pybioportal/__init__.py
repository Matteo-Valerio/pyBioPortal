# Import necessary functions from other modules
from .samples import (
    get_samples,
    get_samples_by_keyword,
    fetch_samples,
    get_all_samples_of_patient_in_study,
    get_all_samples_in_study,
    get_sample_in_study
)

from .patients import (
    get_patient,
    get_all_patients,
    fetch_patients,
    get_all_patients_in_study,
    get_patient_in_study
)

from .mutations import (
    get_mutations,
    get_muts_in_mol_prof_by_sample_list_id,
    fetch_muts_in_mol_prof,
    fetch_muts_in_multiple_mol_profs
)

from .molecular_profiles import (
    get_molecular_profiles,
    get_all_molecular_profiles,
    get_molecular_profile,
    fetch_molecular_profiles,
    get_all_molecular_profiles_in_study
)

from .__config import configure_base_url, set_api_token

def initialize(api_token, new_base_url=None):
    """
    Initialize the library with the API token and optionally a new base URL.
    
    :param api_token: The API token for authentication.
    :param new_base_url: The base URL of the cBioPortal instance.
    """
    set_api_token(api_token)
    if new_base_url:
        configure_base_url(new_base_url)
