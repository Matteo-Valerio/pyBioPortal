import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_muts_in_mol_prof_by_sample_list_id(molecular_profile_id, sample_list_id, entrez_gene_id=None, 
                                           projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Get mutations in a molecular profile by Sample List ID. \n
    :param molecular_profile_id: Molecular Profile ID (e.g., "acc_tcga_mutations"). \n
    :type molecular_profile_id: str \n
    :param sample_list_id: Sample List ID (e.g., "acc_tcga_all"). \n
    :type sample_list_id: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :param entrez_gene_id: Entrez Gene ID (e.g., "1"). \n
    :type entrez_gene_id: str \n
    :param direction: Direction of the sort. \n
        Possible values: \n
            - "ASC": Ascending (default).
            - "DESC": Descending.
    :type direction: str \n
    :param pageNumber: Page number of the result list. \n
            - Minimum value is 0.
    :type pageNumber: int \n
    :param pageSize: Page size of the result list. \n
            - Minimum value is 1, maximum value is 10000000.
    :type pageSize: int \n
    :param sortBy: Name of the property that the result list is sorted by. \n
        Possible values: \n
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
    :type sortBy: str \n
    :returns: A DataFrame containing mutations in the molecular profile. \n
    :rtype: pandas.DataFrame \n
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
    return process_response(response, "Failed to get mutations in molecular profile.")

def fetch_muts_in_mol_prof(molecular_profile_id, entrez_gene_ids=None, sample_ids=None, sample_list_id=None, 
                           projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Fetch mutations in a molecular profile. \n
    :param molecular_profile_id: Molecular Profile ID (e.g., "brca_tcga_mutations"). \n
    :type molecular_profile_id: str \n
    :param entrez_gene_ids: List ID and Entrez Gene IDs (e.g., ["TCGA-AR-A1AR-01","TCGA-BH-A1EO-01"]). \n
    :type entrez_gene_ids: List of str \n
    :param sample_ids: List of Sample IDs (e.g., ["1005", "1020"]). \n
    :type sample_ids: List of str \n
    :param sample_list_id: Sample List ID (e.g., "brca_tcga_all"). \n
    :type sample_list_id: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :param direction: Direction of the sort. \n
        Possible values: \n
            - "ASC": Ascending (default).
            - "DESC": Descending.
    :type direction: str \n
    :param pageNumber: Page number of the result list. \n
            - Minimum value is 0.
    :type pageNumber: int \n
    :param pageSize: Page size of the result list. \n
            - Minimum value is 1, maximum value is 10000000.
    :type pageSize: int \n
    :param sortBy: Name of the property that the result list is sorted by. \n
        Possible values: \n
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
    :type sortBy: str \n
    :returns: A DataFrame containing mutations in the molecular profile. \n
    :rtype: pandas.DataFrame \n
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

    response = requests.post(f"{base_url}{endpoint}", params=params, json=mutation_filter)
    return process_response(response, "Failed to fetch mutations in molecular profile.")

def fetch_muts_in_multiple_mol_profs(entrez_gene_ids=None, molecular_profile_ids=None, sample_molecular_identifiers=None, 
                                     projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy=None):
    """
    Fetch mutations in multiple molecular profiles by sample IDs. \n
    :param entrez_gene_ids: List of Entrez Gene IDs (e.g. ["672","675"]). \n
    :type entrez_gene_ids: list of str \n
    :param molecular_profile_ids: List of Molecular Profile IDs (e.g. ["brca_tcga_mutations", "acc_tcga_mutations"]). \n
    :type molecular_profile_ids: list of str \n
    :param sample_molecular_identifiers: List of Molecular Profile ID / Sample ID pairs. \n
    :type sample_molecular_identifiers: list of dict \n
        Each dict should have the following format: \n
            sample_molecular_identifiers=[
                                         {"molecular_profile_id": "brca_tcga_mutations", 
                                          "sample_ids": ["TCGA-A2-A4S0-01","TCGA-E2-A1L9-01"]},
                                         {"molecular_profile_id": "acc_tcga_mutations", 
                                          "sample_ids": ["TCGA-OR-A5LE-01"]}
                                         ] \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :param direction: Direction of the sort. \n
        Possible values: \n
            - "ASC": Ascending (default).
            - "DESC": Descending.
    :type direction: str \n
    :param pageNumber: Page number of the result list. \n
            - Minimum value is 0.
    :type pageNumber: int \n
    :param pageSize: Page size of the result list. \n
            - Minimum value is 1, maximum value is 10000000.
    :type pageSize: int \n
    :param sortBy: Name of the property that the result list is sorted by. \n
        Possible values: \n
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
    :type sortBy: str \n
    :returns: A DataFrame containing mutations in the specified molecular profiles. \n
    :rtype: pandas.DataFrame \n
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

    response = requests.post(f"{base_url}{endpoint}", params=params, json=mutation_multiple_study_filter)
    return process_response(response, "Failed to fetch mutations in multiple molecular profiles.")
