import requests
import pandas as pd
from config import base_url

########################
# Copy Number Segments #
########################
def fetch_copy_number_segments(sample_identifiers, chromosome=None, projection="SUMMARY"):
    """
    Fetch copy number segments from BioPortal by sample ID.
    :param sample_identifiers: List of sample identifiers.
    :type sample_identifiers: list of dict
        Each dictionary should have the following format:
        {
            "sampleId": "Sample ID",
            "studyId": "Study ID"
        }
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

    data = {"sampleIdentifiers": sample_identifiers}

    sample_identifiers = {
        "sampleId": [],
        "studyId": []
    }
    
    for item in entity_study_ids:
        study_id = item["study"]
        entity_ids = item["entity_ids"]
        
        for entity_id in entity_ids:
            identifier = {
                "entityId": entity_id,
                "studyId": study_id
            }
            sample_identifiers["identifiers"].append(identifier)

    response = requests.post(f"{base_url}{endpoint}", json=data, params=params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch copy number segments. Status code: {response.status_code}")

########################
# Copy Number Segments #
########################
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
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get copy number segments for the sample. Status code: {response.status_code}")