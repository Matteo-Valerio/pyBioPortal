import requests
import pandas as pd
from config import base_url
from aux_funcs import check_response, flatten_dict_columns, flatten_dict_list_columns

###############
# Gene Panels #
###############
def get_all_gene_panels(direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all gene panels from BioPortal.
    :param direction: Direction of the sort.
        - "ASC": Ascending order (default).
        - "DESC": Descending order.
    :type direction: str
    :param pageNumber: Page number of the result list.
        Minimum value is 0.
    :type pageNumber: int
    :param pageSize: Page size of the result list.
        Minimum value is 1, maximum value is 10000000.
    :type pageSize: int
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :param sortBy: Name of the property that the result list is sorted by.
    :type sortBy: str
        Possible values:
            - "description": Sort by description.
            - "genePanelId": Sort by gene panel ID.
    :returns: A DataFrame containing the list of gene panels.
    :rtype: pandas.DataFrame
    """
    endpoint = "/gene-panels"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection
    }

    if sortBy:
        params["sortBy"] = sortBy

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return check_response(response, "Failed to get gene panels.")


def get_gene_panel(gene_panel_id):
    """
    Get a specific gene panel from BioPortal.
    :param gene_panel_id: Gene Panel ID (e.g., "NSCLC_UNITO_2016_PANEL").
    :type gene_panel_id: str
    :returns: A DataFrame containing information about the specific gene panel.
    :rtype: pandas.DataFrame
    """
    endpoint = f"/gene-panels/{gene_panel_id}"
    
    response = requests.get(f"{base_url}{endpoint}")
    df = check_response(response, f"Failed to get gene panel {gene_panel_id}.")
    return flatten_dict_columns(df)
    

def fetch_gene_panels(gene_panel_ids, projection="SUMMARY"):
    """
    Fetch gene panels from BioPortal by Gene Panel IDs.
    :param gene_panel_ids: List of Gene Panel IDs.
    :type gene_panel_ids: list of str
    :param projection: Level of detail of the response.
        - "DETAILED": Detailed information.
        - "ID": Information with only IDs.
        - "META": Metadata information.
        - "SUMMARY": Summary information (default).
    :type projection: str
    :returns: A DataFrame containing the fetched gene panels.
    :rtype: pandas.DataFrame
    """
    endpoint = "/gene-panels/fetch"
    params = {"projection": projection}
    
    response = requests.post(f"{base_url}{endpoint}", json=gene_panel_ids, params=params)
    df = check_response(response, "Failed to fetch gene panels.")
    return flatten_dict_list_columns(df)
    


