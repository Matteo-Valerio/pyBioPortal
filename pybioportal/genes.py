import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_all_genes(alias=None, direction="ASC", keyword=None, pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="hugoGeneSymbol"):
    """
    Get all genes based on filter criteria (alias or keyword). \n
    :param alias: Alias of the gene. \n
    :type alias: str \n
    :param direction: Direction of the sort. \n
        Possible values: \n
            - "ASC": Ascending (default)
            - "DESC": Descending
    :type direction: str \n
    :param keyword: Search keyword that applies to hugo gene symbol of the genes. \n
    :type keyword: str \n
    :param pageNumber: Page number of the result list. \n
            - Minimum value is 0.
    :type pageNumber: int \n
    :param pageSize: Page size of the result list. \n
            - Minimum value is 1, maximum value is 10000000.
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
            - "cytoband"
            - "entrezGeneId"
            - "hugoGeneSymbol" (default)
            - "length"
            - "type"
    :type sortBy: str \n
    :returns: A DataFrame containing genes based on the specified filter criteria. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/genes"
    params = {
        "alias": alias,
        "direction": direction,
        "keyword": keyword,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get genes.")

def get_gene(gene_id):
    """
    Get gene information by Entrez Gene ID or Hugo Gene Symbol. \n
    :param gene_id: Entrez Gene ID or Hugo Gene Symbol (e.g., "1" or "A1BG"). \n
    :type gene_id: str \n
    :returns: A DataFrame containing information about the specified gene. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/genes/{gene_id}"

    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get gene information.")

def get_aliases_of_gene(gene_id):
    """
    Get aliases of a gene by Entrez Gene ID or Hugo Gene Symbol. \n
    :param gene_id: Entrez Gene ID or Hugo Gene Symbol (e.g., "1" or "A1BG"). \n
    :type gene_id: str \n
    :returns: A DataFrame containing aliases for the specified gene. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/genes/{gene_id}/aliases"

    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get aliases of the gene.")

def fetch_genes(gene_ids, gene_id_type="ENTREZ_GENE_ID", projection="SUMMARY"):
    """
    Fetch genes by Entrez Gene IDs or Hugo Gene Symbols. \n
    :param gene_ids: List of Entrez Gene IDs or Hugo Gene Symbols (e.g., ["BRCA1","BRCA2"]). \n
    :type gene_ids: list of str \n
    :param gene_id_type: Type of gene ID. \n
        Possible values: \n
            - "ENTREZ_GENE_ID" (default): Entrez Gene IDs.
            - "HUGO_GENE_SYMBOL": Hugo Gene Symbols.
    :type gene_id_type: str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing genes based on the specified Entrez Gene IDs or Hugo Gene Symbols. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/genes/fetch"
    params = {"geneIdType": gene_id_type, "projection": projection}

    response = requests.post(f"{base_url}{endpoint}", params=params, json=gene_ids)
    return process_response(response, "Failed to fetch genes.")    