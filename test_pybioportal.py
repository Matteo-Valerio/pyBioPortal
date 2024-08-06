import json
import logging
import os
from pybioportal import initialize
from pybioportal import studies, treatments, samples, patients, mutations, molecular_profiles

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to read token from environment variable
def get_api_token():
    return os.getenv('CBIOPORTAL_API_TOKEN')

# Initialize the library with the user's API token
API_TOKEN = get_api_token()
initialize(API_TOKEN)

# Use a valid study ID from the get_all_studies output
valid_study_id = "brca_tcga"  # Example valid study ID

def run_tests():
    # Test get_all_studies
    logger.info("Testing get_all_studies:")
    try:
        all_studies = studies.get_all_studies()
        assert not all_studies.empty, "No studies found."
        logger.info("Success: Retrieved %d studies", len(all_studies))
    except Exception as e:
        logger.error("Failed: %s", e)

    # Test fetch_status_display_patient_trts
    logger.info("Testing fetch_status_display_patient_trts:")
    try:
        patient_trts = treatments.fetch_status_display_patient_trts([valid_study_id])
        if patient_trts:
            logger.info("Success: %s", patient_trts)
        else:
            logger.info("No patient treatments found.")
    except Exception as e:
        logger.error("Failed: %s", e)

    # Test get_samples
    logger.info("Testing get_samples:")
    try:
        samples_data = samples.get_samples(valid_study_id)
        assert not samples_data.empty, "No samples found."
        logger.info("Success: Retrieved %d samples", len(samples_data))
    except Exception as e:
        logger.error("Failed: %s", e)

    # List all patients in the study
    logger.info("Listing all patients in the study:")
    try:
        all_patients = patients.get_all_patients_in_study(valid_study_id)
        assert not all_patients.empty, "No patients found."
        logger.info("Success: Retrieved %d patients", len(all_patients))
        valid_patient_id = all_patients.iloc[0]['patientId']  # Use the first patient ID for testing
    except Exception as e:
        logger.error("Failed to list patients: %s", e)
        valid_patient_id = None

    # Test get_patient
    if valid_patient_id:
        logger.info("Testing get_patient:")
        try:
            patient_data = patients.get_patient(valid_study_id, valid_patient_id)
            assert not patient_data.empty, "No patient data found."
            logger.info("Success: %s", patient_data)
        except Exception as e:
            logger.error("Failed: %s", e)

    # List all molecular profiles in the study
    logger.info("Listing all molecular profiles in the study:")
    try:
        all_molecular_profiles = molecular_profiles.get_all_molecular_profiles_in_study(valid_study_id)
        assert not all_molecular_profiles.empty, "No molecular profiles found."
        logger.info("Success: Retrieved %d molecular profiles", len(all_molecular_profiles))
        # Choose a valid molecular profile and corresponding sample list ID
        for idx, row in all_molecular_profiles.iterrows():
            if "mutation" in row['molecularProfileId'].lower():
                valid_molecular_profile_id = row['molecularProfileId']
                break
        else:
            valid_molecular_profile_id = all_molecular_profiles.iloc[0]['molecularProfileId']
        sample_list_id = f"{valid_study_id}_all"  # Assuming a default sample list ID format
    except Exception as e:
        logger.error("Failed to list molecular profiles: %s", e)
        valid_molecular_profile_id = None

    # Test get_mutations
    if valid_molecular_profile_id:
        logger.info(f"Testing get_mutations for molecular profile: {valid_molecular_profile_id}")
        try:
            mutations_data = mutations.get_muts_in_mol_prof_by_sample_list_id(valid_molecular_profile_id, sample_list_id)
            assert not mutations_data.empty, "No mutations data found."
            logger.info("Success: Retrieved %d mutations", len(mutations_data))
        except Exception as e:
            logger.error("Failed: %s", e)

    # Test get_molecular_profiles
    logger.info("Testing get_molecular_profiles:")
    try:
        molecular_profiles_data = molecular_profiles.get_all_molecular_profiles_in_study(valid_study_id)
        assert not molecular_profiles_data.empty, "No molecular profiles data found."
        logger.info("Success: %s", molecular_profiles_data)
    except Exception as e:
        logger.error("Failed: %s", e)

def test_invalid_study_id():
    invalid_study_id = "invalid_study_id"
    logger.info("Testing invalid study ID:")
    try:
        samples_data = samples.get_samples(invalid_study_id)
        assert samples_data.empty, "Expected no data for an invalid study ID."
        logger.info("Success: No data retrieved for invalid study ID as expected.")
    except Exception as e:
        logger.error("Failed: %s", e)

# Run the tests
run_tests()
test_invalid_study_id()
