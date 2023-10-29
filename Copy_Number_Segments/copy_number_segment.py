import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

########################
# Copy Number Segments #
########################
def fetch_copy_number_segments(sample_study_ids, chromosome=None, projection="SUMMARY"):
    """
    Fetch copy number segments from BioPortal by sample ID.
    :param sample_study_ids: List of sample identifiers.
    :type sample_study_ids: list of dict
        Each list should have the following format:
        e.g. for PATIENT data type:
            entity_study_ids = [
                               {"entity_ids": ["P-0000004", "P-0000950"], 
                                "study": "msk_met_2021"},
                               {"entity_ids": ["TCGA-5T-A9QA", "TCGA-A1-A0SB"], 
                                "study": "brca_tcga"}
                               ]
        e.g. for SAMPLE data type:
            entity_study_ids = [
                               {"entity_ids": ["P-0000004-T01-IM3", "P-0000950-T01-IM3"], 
                                "study": "msk_met_2021"},
                               {"entity_ids": ["TCGA-5T-A9QA-01", "TCGA-A1-A0SB-01"], 
                                "study": "brca_tcga"}
                               ]
    :param chromosome: Chromosome (optional).
    :type chromosome: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched copy number segments.
    :rtype: pandas.DataFrame
    """
    endpoint = "/copy-number-segments/fetch"
    params = {"projection": projection}
    if chromosome:
        params["chromosome"] = chromosome

    sample_identifiers = []
    
    for item in sample_study_ids:
        sample_ids = item["sample_ids"]
        study_id = item["study_id"]
        
        for sample_id in sample_ids:
            identifier = {
                "sampleId": sample_id,
                "studyId": study_id
            }
            sample_identifiers.append(identifier)

    response = requests.post(f"{base_url}{endpoint}", json=sample_identifiers, params=params)
    return check_response(response, "Failed to fetch copy number segments.")

def get_copy_number_segments_in_sample_in_study(study_id, sample_id, chromosome=None, direction="ASC", pageNumber=0, pageSize=20000, projection="SUMMARY", sortBy="chromosome"):
    """
    Get copy number segments in a sample in a study.
    :param study_id: Study ID, e.g., "acc_tcga".
    :type study_id: str
    :param sample_id: Sample ID, e.g., "TCGA-OR-A5J2-01".
    :type sample_id: str
    :param chromosome: Chromosome, e.g., "1".
    :type chromosome: str, optional
    :param direction: Direction of the sort.
        - "ASC": Ascending.
        - "DESC": Descending.
    :type direction: str, optional, default: "ASC"
    :param pageNumber: Page number of the result list.
    :type pageNumber: int, optional, default: 0
    :param pageSize: Page size of the result list.
    :type pageSize: int, optional, default: 20000
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :param sortBy: Name of the property that the result list is sorted by.
        - "chromosome": Sort by chromosome.
        - "end": Sort by end position.
        - "numberOfProbes": Sort by the number of probes.
        - "segmentMean": Sort by segment mean.
        - "start": Sort by start position.
    :type sortBy: str, optional, default: "chromosome"
    :returns: List of copy number segments for the specified sample in the study.
    :rtype: list[dict]
    """
    endpoint = f"/studies/{study_id}/samples/{sample_id}/copy-number-segments"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
    }
    if chromosome:
        params["chromosome"] = chromosome
    if sortBy:
        params["sortBy"] = sortBy

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get copy number segments for the sample.")