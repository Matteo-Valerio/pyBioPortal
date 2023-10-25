import requests
import pandas as pd
from pyBioGate.config import base_url

#############
# Mutations #
#############
def get_mutations_in_molecular_profile_by_sample_list_id(self, molecular_profile_id, sample_list_id, projection="SUMMARY", entrez_gene_id=None, direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
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
    :returns: List of mutations in the molecular profile.
    :rtype: list[dict]
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
    response = requests.get(f"{self.base_url}{endpoint}", params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get mutations in molecular profile. Status code: {response.status_code}")
def fetch_mutations_in_molecular_profile(self, molecular_profile_id, mutation_filter, projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Fetch mutations in a molecular profile.
    :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_mutations".
    :type molecular_profile_id: str
    :param mutation_filter: List of Sample IDs/Sample List ID and Entrez Gene IDs.
    :type mutation_filter: dict
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
    :returns: List of mutations in the molecular profile.
    :rtype: list[dict]
    """
    endpoint = f"/molecular-profiles/{molecular_profile_id}/mutations/fetch"
    params = {
        "direction": direction,
        "projection": projection,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "sortBy": sortBy
    }
    response = requests.post(f"{self.base_url}{endpoint}", json=mutation_filter, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch mutations in molecular profile. Status code: {response.status_code}")
def fetch_mutations_in_multiple_molecular_profiles(self, mutation_multiple_study_filter, projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Fetch mutations in multiple molecular profiles by sample IDs.
    :param mutation_multiple_study_filter: List of Molecular Profile IDs or List of Molecular Profile ID / Sample ID pairs, and List of Entrez Gene IDs.
    :type mutation_multiple_study_filter: dict
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
    :returns: List of mutations in the specified molecular profiles.
    :rtype: list[dict]
    """
    endpoint = "/mutations/fetch"
    params = {
        "direction": direction,
        "projection": projection,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "sortBy": sortBy
    }
    response = requests.post(f"{self.base_url}{endpoint}", json=mutation_multiple_study_filter, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch mutations in multiple molecular profiles. Status code: {response.status_code}")