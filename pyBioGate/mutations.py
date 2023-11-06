import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

#############
# Mutations #
#############
def get_mutations_in_molecular_profile_by_sample_list_id(molecular_profile_id, sample_list_id, projection="SUMMARY", entrez_gene_id=None, direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Get mutations in a molecular profile by Sample List ID.
    :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_mutations".
    :type molecular_profile_id: str
    :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
    :type sample_list_id: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :param entrez_gene_id: Entrez Gene ID, e.g., 1.
    :type entrez_gene_id: int, optional
    :param direction: Direction of the sort.
        - "ASC": Ascending.
        - "DESC": Descending.
    :type direction: str, optional, default: "ASC"
    :param pageNumber: Page number of the result list.
    :type pageNumber: int, optional, default: 0
    :param pageSize: Page size of the result list.
    :type pageSize: int, optional, default: 10000000
    :param sortBy: Name of the property that the result list is sorted by.
        Possible values:
        - "aminoAcidChange"
        - "center"
        - "endPosition"
        - "entrezGeneId"
        - "keyword"
        - "mutationStatus"
        - "mutationType"
        - "ncbiBuild"
        - "normalAltCount"
        - "normalRefCount"
        - "proteinChange"
        - "proteinPosEnd"
        - "proteinPosStart"
        - "referenceAllele"
        - "refseqMrnaId"
        - "startPosition"
        - "tumorAltCount"
        - "tumorRefCount"
        - "validationStatus"
        - "variantAllele"
        - "variantType"
    :type sortBy: str, optional
    :returns: A DataFrame containing mutations in the molecular profile.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/mutations"
    params = {
        "direction": direction,
        "entrezGeneId": entrez_gene_id,
        "projection": projection,
        "sampleListId": sample_list_id,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "sortBy": sortBy
    }
    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get mutations in molecular profile.")

def fetch_mutations_in_molecular_profile(molecular_profile_id, entrez_gene_ids=None, sample_ids=None, sample_list_id=None, projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Fetch mutations in a molecular profile.
    :param molecular_profile_id: Molecular Profile ID, e.g., "brca_tcga_mutations".
    :type molecular_profile_id: str
    :param entrez_gene_ids: List ID and Entrez Gene IDs, e.g., ["TCGA-AR-A1AR-01","TCGA-BH-A1EO-01"]
    :type entrez_gene_ids: List of str
    :param sample_ids: List of Sample IDs, e.g., ["1005", "1020"].
    :type sample_ids: List of str
    :param sample_list_id: Sample List ID, e.g., "brca_tcga_all".
    :type sample_list_id: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :param direction: Direction of the sort.
        - "ASC": Ascending.
        - "DESC": Descending.
    :type direction: str, optional, default: "ASC"
    :param pageNumber: Page number of the result list.
    :type pageNumber: int, optional, default: 0
    :param pageSize: Page size of the result list.
    :type pageSize: int, optional, default: 10000000
    :param sortBy: Name of the property that the result list is sorted by.
        Possible values:
        - "aminoAcidChange"
        - "center"
        - "endPosition"
        - "entrezGeneId"
        - "keyword"
        - "mutationStatus"
        - "mutationType"
        - "ncbiBuild"
        - "normalAltCount"
        - "normalRefCount"
        - "proteinChange"
        - "proteinPosEnd"
        - "proteinPosStart"
        - "referenceAllele"
        - "refseqMrnaId"
        - "startPosition"
        - "tumorAltCount"
        - "tumorRefCount"
        - "validationStatus"
        - "variantAllele"
        - "variantType"
    :type sortBy: str, optional
    :returns: A DataFrame containing mutations in the molecular profile.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/mutations/fetch"
    params = {
        "direction": direction,
        "projection": projection,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "sortBy": sortBy
    }

    mutation_filter = {}

    if entrez_gene_ids:
        mutation_filter['entrezGeneIds'] = entrez_gene_ids

    if sample_ids:
        mutation_filter['sampleIds'] = sample_ids

    if sample_list_id:
        mutation_filter['sampleListId'] = sample_list_id

    response = requests.post(f"{base_url}{endpoint}", json=mutation_filter, params=params)
    return check_response(response, "Failed to fetch mutations in molecular profile.")

def fetch_mutations_in_multiple_molecular_profiles(entrez_gene_ids=None, molecular_profile_ids=None, sample_molecular_identifiers=None, projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Fetch mutations in multiple molecular profiles by sample IDs.
    :param entrez_gene_ids: List of Entrez Gene IDs, e.g. ["672","675"].
    :type entrez_gene_ids: list of str
    :param molecular_profile_ids: List of Molecular Profile IDs, e.g. ["brca_tcga_mutations", "acc_tcga_mutations"].
    :type molecular_profile_ids: list of str
    :param sample_molecular_identifiers: List of Molecular Profile ID / Sample ID pairs.
    :type sample_molecular_identifiers: list of dict
        Each dict should have the following format:
            sample_molecular_identifiers=[
                                         {"molecular_profile_id": "brca_tcga_mutations", 
                                          "sample_ids": ["TCGA-A2-A4S0-01","TCGA-E2-A1L9-01"]},
                                         {"molecular_profile_id": "acc_tcga_mutations", 
                                          "sample_ids": ["TCGA-OR-A5LE-01"]}
                                         ]  
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str, optional, default: "SUMMARY"
    :param direction: Direction of the sort.
        - "ASC": Ascending.
        - "DESC": Descending.
    :type direction: str, optional, default: "ASC"
    :param pageNumber: Page number of the result list.
    :type pageNumber: int, optional, default: 0
    :param pageSize: Page size of the result list.
    :type pageSize: int, optional, default: 10000000
    :param sortBy: Name of the property that the result list is sorted by.
        Possible values:
        - "aminoAcidChange"
        - "center"
        - "endPosition"
        - "entrezGeneId"
        - "keyword"
        - "mutationStatus"
        - "mutationType"
        - "ncbiBuild"
        - "normalAltCount"
        - "normalRefCount"
        - "proteinChange"
        - "proteinPosEnd"
        - "proteinPosStart"
        - "referenceAllele"
        - "refseqMrnaId"
        - "startPosition"
        - "tumorAltCount"
        - "tumorRefCount"
        - "validationStatus"
        - "variantAllele"
        - "variantType"
    :type sortBy: str, optional
    :returns: A DataFrame containing mutations in the specified molecular profiles.
    :rtype: pandas.DataFrame
    """
    endpoint = "/mutations/fetch"
    params = {
        "direction": direction,
        "projection": projection,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "sortBy": sortBy
    }

    mutation_multiple_study_filter = {}

    if entrez_gene_ids:
        mutation_multiple_study_filter['entrezGeneIds'] = entrez_gene_ids
    
    if molecular_profile_ids:
        mutation_multiple_study_filter['molecularProfileIds'] = molecular_profile_ids

    if sample_molecular_identifiers:
        mutation_multiple_study_filter['sampleMolecularIdentifiers'] = []

        for item in sample_molecular_identifiers:
            molec_prof_id = item["molecular_profile_id"]
            sample_ids = item["sample_ids"]

            for sample_id in sample_ids:
                identifier = {
                    "molecularProfileId": molec_prof_id,
                    "sampleId": sample_id
                }
                mutation_multiple_study_filter["sampleMolecularIdentifiers"].append(identifier)

    response = requests.post(f"{base_url}{endpoint}", json=mutation_multiple_study_filter, params=params)
    return check_response(response, "Failed to fetch mutations in multiple molecular profiles.")
