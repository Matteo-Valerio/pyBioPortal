
import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response

#########
# Genes #
#########
def get_all_genes(alias=None, direction="ASC", keyword=None, pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="hugoGeneSymbol"):
    """
    Get all genes based on filter criteria (alias or keyword).
    :param alias: Alias of the gene.
    :type alias: str
    :param direction: Direction of the sort.
        - "ASC": Ascending order.
        - "DESC": Descending order (default).
    :type direction: str
    :param keyword: Search keyword that applies to hugo gene symbol of the genes.
    :type keyword: str
    :param pageNumber: Page number of the result list.
    :type pageNumber: int
    :param pageSize: Page size of the result list.
    :type pageSize: int
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :param sortBy: Name of the property that the result list is sorted by.
        - "cytoband"
        - "entrezGeneId"
        - "hugoGeneSymbol" (default)
        - "length"
        - "type"
    :type sortBy: str
    :returns: A DataFrame containing genes based on the specified filter criteria.
    :rtype: pandas.DataFrame
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
    return check_response(response, "Failed to get genes.")

def get_gene(gene_id):
    """
    Get gene information by Entrez Gene ID or Hugo Gene Symbol.
    :param gene_id: Entrez Gene ID or Hugo Gene Symbol (e.g., 1 or A1BG).
    :type gene_id: str
    :returns: A DataFrame containing information about the specified gene.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/genes/{gene_id}"
    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get gene information.")

def get_aliases_of_gene(gene_id):
    """
    Get aliases of a gene by Entrez Gene ID or Hugo Gene Symbol.
    :param gene_id: Entrez Gene ID or Hugo Gene Symbol (e.g., 1 or A1BG).
    :type gene_id: str
    :returns: A DataFrame containing aliases for the specified gene.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/genes/{gene_id}/aliases"
    response = requests.get(f"{base_url}{endpoint}")
    return check_response(response, "Failed to get aliases of the gene.")

def fetch_genes(gene_ids, gene_id_type="ENTREZ_GENE_ID", projection="SUMMARY"):
    """
    Fetch genes by Entrez Gene IDs or Hugo Gene Symbols.
    :param gene_ids: List of Entrez Gene IDs or Hugo Gene Symbols.
    :type gene_ids: list of str
    :param gene_id_type: Type of gene ID.
        - "ENTREZ_GENE_ID" (default): Entrez Gene IDs.
        - "HUGO_GENE_SYMBOL": Hugo Gene Symbols.
    :type gene_id_type: str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing genes based on the specified Entrez Gene IDs or Hugo Gene Symbols.
    :rtype: pandas.DataFrame
    """
    endpoint = "/genes/fetch"
    params = {"geneIdType": gene_id_type, "projection": projection}

    response = requests.post(f"{base_url}{endpoint}", params=params, json=gene_ids)
    return check_response(response, "Failed to fetch genes.")    