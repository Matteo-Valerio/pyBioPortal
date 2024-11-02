import requests
from .__config import base_url
from .__aux_funcs import process_response

def fetch_copy_number_segments(sample_study_ids, chromosome=None, projection="SUMMARY"):
    """
    Fetch copy number segments from cBioPortal by sample ID. \n
    :param sample_study_ids: List of sample identifiers. \n
        Each list should have the following format: \n
            sample_study_ids = [
                               {"sample_ids": ["P-0000004-T01-IM3", "P-0000950-T01-IM3"], 
                                "study_id": "msk_met_2021"},
                               {"sample_ids": ["TCGA-5T-A9QA-01", "TCGA-A1-A0SB-01"], 
                                "study_id": "brca_tcga"}
                               ]
    :type sample_study_ids: list of dict \n        
    :param chromosome: Chromosome (e.g., "1"). \n
    :type chromosome: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing the fetched copy number segments. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/copy-number-segments/fetch"
    params = {"projection": projection,
              "chromosome": chromosome}
    # if chromosome:
    #     params["chromosome"] = chromosome

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

    response = requests.post(f"{base_url}{endpoint}", params=params, json=sample_identifiers,)
    return process_response(response, "Failed to fetch copy number segments.")

def get_copy_number_segments_in_sample_in_study(study_id, sample_id, chromosome=None, direction="ASC", 
                                                pageNumber=0, pageSize=20000, projection="SUMMARY", sortBy="chromosome"):
    """
    Get copy number segments in a sample in a study. \n
    :param study_id: Study ID (e.g., "acc_tcga"). \n
    :type study_id: str \n
    :param sample_id: Sample ID (e.g., "TCGA-OR-A5J2-01"). \n
    :type sample_id: str \n
    :param chromosome: Chromosome (e.g., "1"). \n
    :type chromosome: str \n
    :param direction: Direction of the sort. \n
        Possible values: \n
            - "ASC": Ascending (default).
            - "DESC": Descending.
    :type direction: str \n
    :param pageNumber: Page number of the result list. \n
            - Minimum value is 0.
    :type pageNumber: int \n
    :param pageSize: Page size of the result list. \n
            - Minimum value is 1, maximum value is 20000.
    :type pageSize: int \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :param sortBy: Name of the property that the result list is sorted by. \n
        Possible values: \n
            - "chromosome": Sort by chromosome (default).
            - "end": Sort by end position.
            - "numberOfProbes": Sort by the number of probes.
            - "segmentMean": Sort by segment mean.
            - "start": Sort by start position.
    :type sortBy: str \n
    :returns: A DataFrame containing copy number segments for the specified sample in the study. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/studies/{study_id}/samples/{sample_id}/copy-number-segments"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "chromosome": chromosome,
        "sortBy": sortBy 
    }
    # if chromosome:
    #     params["chromosome"] = chromosome
    # if sortBy:
    #     params["sortBy"] = sortBy

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get copy number segments for the sample.")