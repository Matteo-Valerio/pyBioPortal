import requests
from .__config import base_url
from .__aux_funcs import process_response

def get_all_gene_panels(direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
    """
    Get all gene panels from cBioPortal. \n
    :param direction: Direction of the sort. \n
        Possible values: \n
            - "ASC": Ascending (default).
            - "DESC": Descending
    :type direction: str \n
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
    :type sortBy: str \n
        Possible values: \n
            - "description": Sort by description.
            - "genePanelId": Sort by gene panel ID.
    :returns: A DataFrame containing the list of gene panels. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/gene-panels"
    params = {
        "direction": direction,
        "pageNumber": pageNumber,
        "pageSize": pageSize,
        "projection": projection,
        "sortBy": sortBy
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)
    return process_response(response, "Failed to get gene panels.")

def get_gene_panel(gene_panel_id):
    """
    Get a specific gene panel from cBioPortal. \n
    :param gene_panel_id: Gene Panel ID (e.g., "NSCLC_UNITO_2016_PANEL"). \n
    :type gene_panel_id: str \n
    :returns: A DataFrame containing information about the specific gene panel. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = f"/gene-panels/{gene_panel_id}"
    
    response = requests.get(f"{base_url}{endpoint}")
    return process_response(response, "Failed to get gene panels.")
    # df = process_response(response, f"Failed to get gene panel {gene_panel_id}.")
    # return flatten_dict_columns(df)
    

def fetch_gene_panels(gene_panel_ids, projection="SUMMARY"):
    """
    Fetch gene panels from cBioPortal by Gene Panel IDs. \n
    :param gene_panel_ids: List of Gene Panel IDs. \n
    :type gene_panel_ids: list of str \n
    :param projection: Level of detail of the response. \n
        Possible values: \n
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
    :type projection: str \n
    :returns: A DataFrame containing the fetched gene panels. \n
    :rtype: pandas.DataFrame \n
    """
    endpoint = "/gene-panels/fetch"
    params = {"projection": projection}
    
    response = requests.post(f"{base_url}{endpoint}", json=gene_panel_ids, params=params)
    return process_response(response, "Failed to get gene panels.")
    # df = check_response(response, "Failed to fetch gene panels.")
    # return flatten_dict_list_columns(df)