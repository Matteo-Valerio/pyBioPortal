
import requests
import pandas as pd
from pyBioGate.config import base_url

#########
# Genes #
#########
# Queste nuove funzioni consentono di ottenere informazioni sui geni, inclusi filtri per la ricerca di geni in base a diversi criteri come alias, direzione di ordinamento e parole chiave
def get_all_genes(self, alias=None, direction="ASC", keyword=None, pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="hugoGeneSymbol"):
    """
    Get all genes based on filter criteria.
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
    :returns: A list of genes based on the specified filter criteria.
    :rtype: list[dict]
    """
    params = {
        "alias": alias,
        "direction": direction,
        "keyword": keyword,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }
    response = requests.get(f"{self.base_url}/genes", params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get genes. Status code: {response.status_code}")
def fetch_genes(self, gene_ids, gene_id_type="ENTREZ_GENE_ID", projection="SUMMARY"):
    """
    Fetch genes by Entrez Gene IDs or Hugo Gene Symbols.
    :param gene_ids: List of Entrez Gene IDs or Hugo Gene Symbols.
    :type gene_ids: list[str]
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
    :returns: A list of genes based on the specified Entrez Gene IDs or Hugo Gene Symbols.
    :rtype: list[dict]
    """
    params = {"geneIdType": gene_id_type, "projection": projection}
    data = {"geneIds": gene_ids}
    response = requests.post(f"{self.base_url}/genes/fetch", params=params, json=data)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch genes. Status code: {response.status_code}")
def get_gene(self, gene_id):
    """
    Get gene information by Entrez Gene ID or Hugo Gene Symbol.
    :param gene_id: Entrez Gene ID or Hugo Gene Symbol (e.g., 1 or A1BG).
    :type gene_id: str
    :returns: Information about the specified gene.
    :rtype: dict
    """
    response = requests.get(f"{self.base_url}/genes/{gene_id}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get gene information. Status code: {response.status_code}")
def get_aliases_of_gene(self, gene_id):
    """
    Get aliases of a gene by Entrez Gene ID or Hugo Gene Symbol.
    :param gene_id: Entrez Gene ID or Hugo Gene Symbol (e.g., 1 or A1BG).
    :type gene_id: str
    :returns: A list of aliases for the specified gene.
    :rtype: list[str]
    """
    response = requests.get(f"{self.base_url}/genes/{gene_id}/aliases")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to get aliases of the gene. Status code: {response.status_code}")
    

        
