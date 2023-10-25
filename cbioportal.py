import requests
import pandas as pd

class BioPortalClient:
    def __init__(self, base_url):
        self.base_url = base_url


    ################
    # Cancer Types #
    ################

    #Puoi utilizzare queste funzioni per ottenere dati sui tipi di cancro da BioPortal.

    def get_all_cancer_types(self, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
        """
        Get all cancer types from BioPortal.

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
                - "cancerTypeId": Sort by cancer type ID.
                - "dedicatedColor": Sort by dedicated color.
                - "name": Sort by name.
                - "parent": Sort by parent.
                - "shortName": Sort by short name.

        :returns: A DataFrame containing the list of cancer types.
        :rtype: pandas.DataFrame
        """
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection
        }
        if sortBy:
            params["sortBy"] = sortBy

        response = requests.get(f"{self.base_url}/cancer-types", params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to get cancer types. Status code: {response.status_code}")

    def get_cancer_type(self, cancer_type_id):
        """
        Get a specific cancer type from BioPortal.

        :param cancer_type_id: Cancer Type ID (e.g., "acc").
        :type cancer_type_id: str

        :returns: A DataFrame containing information about the specific cancer type.
        :rtype: pandas.DataFrame
        """
        response = requests.get(f"{self.base_url}/cancer-types/{cancer_type_id}")

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to get cancer type {cancer_type_id}. Status code: {response.status_code}")

    #######################
    # Clinical Attributes #
    #######################

    def get_all_clinical_attributes(self, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
        """
        Get all clinical attributes from BioPortal.

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
            Possible values:
            - "clinicalAttributeId": Sort by clinical attribute ID.
            - "datatype": Sort by datatype.
            - "description": Sort by description.
            - "displayName": Sort by display name.
            - "patientAttribute": Sort by patient attribute.
            - "priority": Sort by priority.
            - "studyId": Sort by study ID.
        :type sortBy: str

        :returns: A DataFrame containing the list of clinical attributes.
        :rtype: pandas.DataFrame
        """
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection
        }
        if sortBy:
            params["sortBy"] = sortBy

        response = requests.get(f"{self.base_url}/clinical-attributes", params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to get clinical attributes. Status code: {response.status_code}")

    def fetch_clinical_attributes(self, study_ids, projection="SUMMARY"):
        """
        Fetch clinical attributes from BioPortal for a list of study IDs.

        :param study_ids: List of Study IDs.
        :type study_ids: list of str
        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str

        :returns: A DataFrame containing the fetched clinical attributes.
        :rtype: pandas.DataFrame
        """
        data = {"studyIds": study_ids}
        params = {"projection": projection}
        response = requests.post(f"{self.base_url}/clinical-attributes/fetch", json=data, params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to fetch clinical attributes. Status code: {response.status_code}")
        
    #################
    # Clinical Data #
    #################

    def fetch_clinical_data(self, clinical_data_filter, clinical_data_type="SAMPLE", projection="SUMMARY"):
        """
        Fetch clinical data by patient IDs or sample IDs (all studies) from BioPortal.

        :param clinical_data_filter: List of patient or sample identifiers and attribute IDs.
        :type clinical_data_filter: dict
        :param clinical_data_type: Type of the clinical data.
            - "PATIENT": Clinical data for patients.
            - "SAMPLE": Clinical data for samples (default).
        :type clinical_data_type: str
        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str

        :returns: A DataFrame containing the fetched clinical data.
        :rtype: pandas.DataFrame
        """
        params = {
            "clinicalDataType": clinical_data_type,
            "projection": projection
        }
        response = requests.post(f"{self.base_url}/clinical-data/fetch", json=clinical_data_filter, params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to fetch clinical data. Status code: {response.status_code}")
        
    ########################
    # Copy Number Segments #
    ########################

    # Puoi utilizzare questa funzione per ottenere dati sui segmenti di copia da BioPortal, specificando i campioni desiderati e il cromosoma (se necessario).

    def fetch_copy_number_segments(self, sample_identifiers, chromosome=None, projection="SUMMARY"):
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
        data = {"sampleIdentifiers": sample_identifiers}
        params = {"projection": projection}
        if chromosome:
            params["chromosome"] = chromosome

        response = requests.post(f"{self.base_url}/copy-number-segments/fetch", json=data, params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to fetch copy number segments. Status code: {response.status_code}")

    ###################
    # Gene Panel Data #
    ###################

    # Queste nuove funzioni consentono di ottenere dati relativi ai pannelli genetici da BioPortal. Le docstring contengono dettagli sui parametri, inclusi i possibili valori e il significato dei parametri. Puoi utilizzare queste funzioni per accedere ai dati sui pannelli genetici da BioPortal.

    def fetch_gene_panel_data(self, gene_panel_data_filter):
        """
        Fetch gene panel data from BioPortal.

        :param gene_panel_data_filter: Gene panel data filter object.
        :type gene_panel_data_filter: dict
            Example format:
            {
                "filterProperty1": "value1",
                "filterProperty2": "value2",
                ...
            }

        :returns: A DataFrame containing the fetched gene panel data.
        :rtype: pandas.DataFrame
        """
        data = gene_panel_data_filter
        response = requests.post(f"{self.base_url}/gene-panel-data/fetch", json=data)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to fetch gene panel data. Status code: {response.status_code}")
        
    ###############
    # Gene Panels #
    ###############

    def get_all_gene_panels(self, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy=None):
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
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection
        }
        if sortBy:
            params["sortBy"] = sortBy

        response = requests.get(f"{self.base_url}/gene-panels", params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to get gene panels. Status code: {response.status_code}")

    def fetch_gene_panels(self, gene_panel_ids, projection="SUMMARY"):
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
        data = gene_panel_ids
        params = {"projection": projection}

        response = requests.post(f"{self.base_url}/gene-panels/fetch", json=data, params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to fetch gene panels. Status code: {response.status_code}")

    def get_gene_panel(self, gene_panel_id):
        """
        Get a specific gene panel from BioPortal.

        :param gene_panel_id: Gene Panel ID (e.g., "NSCLC_UNITO_2016_PANEL").
        :type gene_panel_id: str

        :returns: A DataFrame containing information about the specific gene panel.
        :rtype: pandas.DataFrame
        """
        response = requests.get(f"{self.base_url}/gene-panels/{gene_panel_id}")

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to get gene panel {gene_panel_id}. Status code: {response.status_code}")

    ######################
    # Generic Assay Data #
    ######################

    # Questa nuova funzione consente di ottenere dati di un assaggio generico in un profilo molecolare specifico da BioPortal.

    def get_generic_assay_data_in_molecular_profile(self, molecular_profile_id, generic_assay_stable_id, projection="SUMMARY"):
        """
        Get generic assay data in a molecular profile from BioPortal.

        :param molecular_profile_id: Molecular Profile ID.
        :type molecular_profile_id: str
        :param generic_assay_stable_id: Generic Assay stable ID.
        :type generic_assay_stable_id: str
        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str

        :returns: A DataFrame containing the generic assay data in the specified molecular profile.
        :rtype: pandas.DataFrame
        """
        params = {"projection": projection}
        response = requests.get(f"{self.base_url}/generic-assay-data/{molecular_profile_id}/generic-assay/{generic_assay_stable_id}", params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to get generic assay data. Status code: {response.status_code}")
    
    def fetch_generic_assay_data(self, generic_assay_data_multiple_study_filter, projection="SUMMARY"):
        """
        Fetch generic assay data from multiple molecular profiles in BioPortal.

        :param generic_assay_data_multiple_study_filter: List of Molecular Profile ID and Sample ID pairs
            or List of MolecularProfile IDs and Generic Assay IDs.
        :type generic_assay_data_multiple_study_filter: dict
        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str

        :returns: A DataFrame containing the fetched generic assay data.
        :rtype: pandas.DataFrame
        """
        params = {"projection": projection}
        response = requests.post(f"{self.base_url}/generic_assay_data/fetch", json=generic_assay_data_multiple_study_filter, params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to fetch generic assay data. Status code: {response.status_code}")

    def fetch_generic_assay_data_in_molecular_profile(self, molecular_profile_id, generic_assay_data_filter, projection="SUMMARY"):
        """
        Fetch generic assay data in a specific molecular profile from BioPortal.

        :param molecular_profile_id: Molecular Profile ID.
        :type molecular_profile_id: str
        :param generic_assay_data_filter: List of Sample IDs/Sample List ID and Generic Assay IDs.
        :type generic_assay_data_filter: dict
        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str

        :returns: A DataFrame containing the fetched generic assay data in the specified molecular profile.
        :rtype: pandas.DataFrame
        """
        params = {"projection": projection}
        response = requests.post(f"{self.base_url}/generic_assay_data/{molecular_profile_id}/fetch", json=generic_assay_data_filter, params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to fetch generic assay data. Status code: {response.status_code}")

    ##################
    # Generic Assays #
    ##################

    # Queste nuove funzioni consentono di recuperare i metadati per il generic assay da BioPortal, sia utilizzando l'ID del generic assay che il molecular profile ID

    def get_generic_assay_meta_by_id(self, generic_assay_stable_id, projection="SUMMARY"):
        """
        Fetch meta data for a generic assay by its ID.

        :param generic_assay_stable_id: The stable ID of the generic assay.
        :type generic_assay_stable_id: str
        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str

        :returns: A DataFrame containing the fetched meta data for the generic assay.
        :rtype: pandas.DataFrame
        """
        params = {"projection": projection}
        response = requests.get(f"{self.base_url}/generic-assay-meta/generic-assay/{generic_assay_stable_id}", params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to fetch meta data for the generic assay. Status code: {response.status_code}")

    def get_generic_assay_meta_by_molecular_profile_id(self, molecular_profile_id, projection="SUMMARY"):
        """
        Fetch meta data for a generic assay by molecular profile ID.

        :param molecular_profile_id: Molecular Profile ID.
        :type molecular_profile_id: str
        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str

        :returns: A DataFrame containing the fetched meta data for the generic assay in the specified molecular profile.
        :rtype: pandas.DataFrame
        """
        params = {"projection": projection}
        response = requests.get(f"{self.base_url}/generic-assay-meta/{molecular_profile_id}", params=params)

        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            raise Exception(f"Failed to fetch meta data for the generic assay. Status code: {response.status_code}")

    def fetch_generic_assay_meta(self, generic_assay_meta_filter, projection="SUMMARY"):
        """
        Fetch meta data for generic assays based on a filter.

        :param generic_assay_meta_filter: List of Molecular Profile ID or List of Stable ID.
        :type generic_assay_meta_filter: list[str]
        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str

        :returns: A list of meta data for the generic assays matching the filter criteria.
        :rtype: list[dict]
        """
        params = {"projection": projection}
        data = {"genericAssayMetaFilter": generic_assay_meta_filter}
        response = requests.post(f"{self.base_url}/generic_assay_meta/fetch", params=params, json=data)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch meta data for generic assays. Status code: {response.status_code}")

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

    #########################
    # Server running status #
    #########################

    def get_server_status(self):
        """
        Get the running status of the server.

        :returns: The status of the server.
        :rtype: dict
        """
        response = requests.get(f"{self.base_url}/health")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get server status. Status code: {response.status_code}")


    ########
    # Info #
    ########

    def get_info(self):
        """
        Get information about the running instance.

        :returns: Information about the running instance.
        :rtype: dict
        """
        response = requests.get(f"{self.base_url}/info")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get information. Status code: {response.status_code}")

    ##################
    # Molecular Data #
    ##################

    def fetch_molecular_data(self, molecular_data_filter, projection="SUMMARY"):
        """
        Fetch molecular data.

        :param molecular_data_filter: List of Molecular Profile ID and Sample ID pairs or
                                      List of MolecularProfile IDs and Entrez Gene IDs.
        :type molecular_data_filter: list[dict]
        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str

        :returns: Molecular data.
        :rtype: list[dict]
        """
        endpoint = "/molecular-data/fetch"
        params = {"projection": projection}
        response = requests.post(f"{self.base_url}{endpoint}", json=molecular_data_filter, params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch molecular data. Status code: {response.status_code}")

    ######################
    # Molecular Profiles #
    ######################

    def get_all_molecular_profiles(self, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="datatype"):
        """
        Get all molecular profiles.

        :param direction: Direction of the sort.
            - "ASC": Sort in ascending order (default).
            - "DESC": Sort in descending order.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            - "datatype": Sort by datatype.
            - "description": Sort by description.
            - "molecularAlterationType": Sort by molecular alteration type.
            - "molecularProfileId": Sort by molecular profile ID.
            - "name": Sort by name.
            - "showProfileInAnalysisTab": Sort by profile visibility.
        :type sortBy: str, optional, default: "datatype"

        :returns: List of molecular profiles.
        :rtype: list[dict]
        """
        endpoint = "/molecular-profiles"
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }
        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get all molecular profiles. Status code: {response.status_code}")

    def fetch_molecular_profiles(self, molecular_profile_filter, projection="SUMMARY"):
        """
        Fetch molecular profiles.

        :param molecular_profile_filter: List of Molecular Profile IDs or List of Study IDs.
        :type molecular_profile_filter: list[str]

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of fetched molecular profiles.
        :rtype: list[dict]
        """
        endpoint = "/molecular-profiles/fetch"
        params = {"projection": projection}
        response = requests.post(f"{self.base_url}{endpoint}", json=molecular_profile_filter, params=params, headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch molecular profiles. Status code: {response.status_code}")

    def get_molecular_profile(self, molecular_profile_id):
        """
        Get molecular profile.

        :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_mutations".
        :type molecular_profile_id: str

        :returns: Molecular profile information.
        :rtype: dict
        """
        endpoint = f"/molecular-profiles/{molecular_profile_id}"
        response = requests.get(f"{self.base_url}{endpoint}")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get molecular profile. Status code: {response.status_code}")

    ####################################
    # Discrete Copy Number Alterations #
    ####################################

    
    def get_discrete_copy_numbers_in_molecular_profile(self, molecular_profile_id, sample_list_id, discrete_copy_number_event_type="HOMDEL_AND_AMP", projection="SUMMARY"):
        """
        Get discrete copy number alterations in a molecular profile by sample list ID.

        :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_gistic".
        :type molecular_profile_id: str

        :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
        :type sample_list_id: str

        :param discrete_copy_number_event_type: Type of the copy number event.
            - "ALL": All events.
            - "AMP": Amplification.
            - "DIPLOID": Diploid.
            - "GAIN": Gain.
            - "HETLOSS": Heterozygous loss.
            - "HOMDEL": Homozygous deletion.
            - "HOMDEL_AND_AMP": Homozygous deletion and amplification (default).
        :type discrete_copy_number_event_type: str, optional, default: "HOMDEL_AND_AMP"

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of discrete copy number alterations.
        :rtype: list[dict]
        """
        endpoint = f"/molecular-profiles/{molecular_profile_id}/discrete-copy-number"
        params = {
            "discreteCopyNumberEventType": discrete_copy_number_event_type,
            "projection": projection,
            "sampleListId": sample_list_id
        }
        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get discrete copy numbers in molecular profile. Status code: {response.status_code}")

    def fetch_discrete_copy_numbers_in_molecular_profile(self, molecular_profile_id, sample_list_id, discrete_copy_number_event_type="HOMDEL_AND_AMP", projection="SUMMARY"):
        """
        Fetch discrete copy number alterations in a molecular profile by sample list ID.

        :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_gistic".
        :type molecular_profile_id: str

        :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
        :type sample_list_id: str

        :param discrete_copy_number_event_type: Type of the copy number event.
            - "ALL": All events.
            - "AMP": Amplification.
            - "DIPLOID": Diploid.
            - "GAIN": Gain.
            - "HETLOSS": Heterozygous loss.
            - "HOMDEL": Homozygous deletion.
            - "HOMDEL_AND_AMP": Homozygous deletion and amplification (default).
        :type discrete_copy_number_event_type: str, optional, default: "HOMDEL_AND_AMP"

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of discrete copy number alterations.
        :rtype: list[dict]
        """
        endpoint = f"/molecular-profiles/{molecular_profile_id}/discrete-copy-number/fetch"
        params = {
            "discreteCopyNumberEventType": discrete_copy_number_event_type,
            "projection": projection
        }
        data = {
            "discreteCopyNumberFilter": {
                "sampleIds": [sample_list_id],
                "geneIds": []
            }
        }
        response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch discrete copy numbers in molecular profile. Status code: {response.status_code}")

    ###################
    # Gene Panel Data #
    ###################

    def get_gene_panel_data(self, molecular_profile_id, gene_panel_data_filter):
        """
        Get gene panel data for a specific molecular profile.

        :param molecular_profile_id: Molecular Profile ID, e.g., "nsclc_unito_2016_mutations".
        :type molecular_profile_id: str

        :param gene_panel_data_filter: List of Sample IDs/Sample List ID and Entrez Gene IDs.
        :type gene_panel_data_filter: dict

        :returns: Gene panel data.
        :rtype: list[dict]
        """
        endpoint = f"/molecular-profiles/{molecular_profile_id}/gene-panel-data/fetch"
        response = requests.post(f"{self.base_url}{endpoint}", json=gene_panel_data_filter)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get gene panel data. Status code: {response.status_code}")

    ##################
    # Molecular Data #
    ##################

    def get_all_molecular_data_in_molecular_profile(self, molecular_profile_id, sample_list_id, entrez_gene_id, projection="SUMMARY"):
        """
        Get all molecular data in a molecular profile for a specific gene.

        :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_rna_seq_v2_mrna".
        :type molecular_profile_id: str

        :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
        :type sample_list_id: str

        :param entrez_gene_id: Entrez Gene ID, e.g., 1.
        :type entrez_gene_id: int

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of molecular data for the specified gene.
        :rtype: list[dict]
        """
        endpoint = f"/molecular-profiles/{molecular_profile_id}/molecular-data"
        params = {
            "entrezGeneId": entrez_gene_id,
            "projection": projection,
            "sampleListId": sample_list_id
        }
        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get molecular data in molecular profile. Status code: {response.status_code}")
    
    def fetch_all_molecular_data_in_molecular_profile(self, molecular_profile_id, molecular_data_filter, projection="SUMMARY"):
        """
        Fetch molecular data in a molecular profile for a list of genes.

        :param molecular_profile_id: Molecular Profile ID, e.g., "acc_tcga_rna_seq_v2_mrna".
        :type molecular_profile_id: str

        :param molecular_data_filter: List of Sample IDs/Sample List ID and Entrez Gene IDs.
        :type molecular_data_filter: dict

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of molecular data for the specified genes.
        :rtype: list[dict]
        """
        endpoint = f"/molecular-profiles/{molecular_profile_id}/molecular-data/fetch"
        response = requests.post(f"{self.base_url}{endpoint}", json=molecular_data_filter)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch molecular data in molecular profile. Status code: {response.status_code}")

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

    ############
    # Patients #
    ############

    def get_all_patients(self, projection="SUMMARY", direction="ASC", keyword=None, pageNumber=0, pageSize=10000000, sortBy="patientId"):
        """
        Get all patients.

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

        :param keyword: Search keyword that applies to ID of the patients.
        :type keyword: str, optional

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param sortBy: Name of the property that the result list is sorted by.
            Possible values:
            - "patientId"
        :type sortBy: str, optional, default: "patientId"

        :returns: List of patients.
        :rtype: list[dict]
        """
        endpoint = "/patients"
        params = {
            "direction": direction,
            "keyword": keyword,
            "projection": projection,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "sortBy": sortBy
        }
        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get all patients. Status code: {response.status_code}")

    def fetch_patients(self, patient_filter, projection="SUMMARY"):
        """
        Fetch patients.

        :param patient_filter: List of patient identifiers.
        :type patient_filter: dict

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of patients.
        :rtype: list[dict]
        """
        endpoint = "/patients/fetch"
        params = {
            "projection": projection
        }
        response = requests.post(f"{self.base_url}{endpoint}", json=patient_filter, params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch patients. Status code: {response.status_code}")

    ################
    # Sample Lists #
    ################

    def get_all_sample_lists(self, projection="SUMMARY", direction="ASC", pageNumber=0, pageSize=10000000, sortBy="sampleListId"):
        """
        Get all sample lists.

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
            - "category"
            - "description"
            - "name"
            - "sampleListId"
            - "studyId"
        :type sortBy: str, optional, default: "sampleListId"

        :returns: List of sample lists.
        :rtype: list[dict]
        """
        endpoint = "/sample-lists"
        params = {
            "direction": direction,
            "projection": projection,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "sortBy": sortBy
        }
        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get all sample lists. Status code: {response.status_code}")

    def fetch_sample_lists(self, sample_list_ids, projection="SUMMARY"):
        """
        Fetch sample lists by ID.

        :param sample_list_ids: List of sample list IDs.
        :type sample_list_ids: list[str]

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of sample lists.
        :rtype: list[dict]
        """
        endpoint = "/sample-lists/fetch"
        params = {
            "projection": projection
        }
        response = requests.post(f"{self.base_url}{endpoint}", json=sample_list_ids, params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch sample lists. Status code: {response.status_code}")

    def get_sample_list(self, sample_list_id):
        """
        Get sample list.

        :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
        :type sample_list_id: str

        :returns: Sample list details.
        :rtype: dict
        """
        endpoint = f"/sample-lists/{sample_list_id}"
        response = requests.get(f"{self.base_url}{endpoint}")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get sample list. Status code: {response.status_code}")

    def get_all_sample_ids_in_sample_list(self, sample_list_id):
        """
        Get all sample IDs in a sample list.

        :param sample_list_id: Sample List ID, e.g., "acc_tcga_all".
        :type sample_list_id: str

        :returns: List of sample IDs in the sample list.
        :rtype: list[str]
        """
        endpoint = f"/sample-lists/{sample_list_id}/sample-ids"
        response = requests.get(f"{self.base_url}{endpoint}")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get all sample IDs in sample list. Status code: {response.status_code}")

    ###########
    # Samples #
    ###########

    def get_samples_by_keyword(self, keyword=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleId"):
        """
        Get all samples matching a keyword.

        :param keyword: Search keyword that applies to the study ID.
        :type keyword: str, optional

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            Possible values:
            - "sampleId"
            - "sampleType"
        :type sortBy: str, optional, default: "sampleId"

        :returns: List of samples matching the keyword.
        :rtype: list[dict]
        """
        endpoint = "/samples"
        params = {
            "keyword": keyword,
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }
        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get samples by keyword. Status code: {response.status_code}")

    def fetch_samples(self, sample_ids, projection="SUMMARY"):
        """
        Fetch samples by ID.

        :param sample_ids: List of sample identifiers.
        :type sample_ids: list[str]

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of samples by ID.
        :rtype: list[dict]
        """
        endpoint = "/samples/fetch"
        params = {
            "projection": projection
        }
        response = requests.post(f"{self.base_url}{endpoint}", json=sample_ids, params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch samples by ID. Status code: {response.status_code}")

    ###########
    # Studies #
    ###########

    def get_all_studies(self, keyword=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="studyId"):
        """
        Get all studies.

        :param keyword: Search keyword that applies to name and cancer type of the studies.
        :type keyword: str, optional

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            Possible values:
            - "cancerTypeId"
            - "citation"
            - "description"
            - "groups"
            - "importDate"
            - "name"
            - "pmid"
            - "publicStudy"
            - "status"
            - "studyId"
        :type sortBy: str, optional, default: "studyId"

        :returns: List of studies.
        :rtype: list[dict]
        """
        endpoint = "/studies"
        params = {
            "keyword": keyword,
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }
        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get all studies. Status code: {response.status_code}")

    def fetch_studies(self, study_ids, projection="SUMMARY"):
        """
        Fetch studies by IDs.

        :param study_ids: List of study identifiers.
        :type study_ids: list[str]

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of studies by IDs.
        :rtype: list[dict]
        """
        endpoint = "/studies/fetch"
        params = {
            "projection": projection
        }
        response = requests.post(f"{self.base_url}{endpoint}", json=study_ids, params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch studies by IDs. Status code: {response.status_code}")

    def get_tags_for_multiple_studies(self, study_ids):
        """
        Get the study tags by IDs.

        :param study_ids: List of study identifiers.
        :type study_ids: list[str]

        :returns: Study tags for multiple studies.
        :rtype: list[dict]
        """
        endpoint = "/studies/tags/fetch"
        response = requests.post(f"{self.base_url}{endpoint}", json=study_ids)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get study tags for multiple studies. Status code: {response.status_code}")

    def get_study(self, study_id):
        """
        Get a study by ID.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :returns: Information about the study.
        :rtype: dict
        """
        endpoint = f"/studies/{study_id}"
        response = requests.get(f"{self.base_url}{endpoint}")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get the study by ID. Status code: {response.status_code}")

    #######################
    # Clinical Attributes #
    #######################

    def get_all_clinical_attributes_in_study(self, study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="clinicalAttributeId"):
        """
        Get all clinical attributes in the specified study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            Possible values:
            - "clinicalAttributeId"
            - "datatype"
            - "description"
            - "displayName"
            - "patientAttribute"
            - "priority"
            - "studyId"
        :type sortBy: str, optional, default: "clinicalAttributeId"

        :returns: List of clinical attributes in the specified study.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/clinical-attributes"
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }
        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get clinical attributes in the specified study. Status code: {response.status_code}")

    def get_clinical_attribute_in_study(self, study_id, clinical_attribute_id):
        """
        Get the specified clinical attribute in the study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param clinical_attribute_id: Clinical Attribute ID, e.g., "CANCER_TYPE".
        :type clinical_attribute_id: str

        :returns: Information about the specified clinical attribute in the study.
        :rtype: dict
        """
        endpoint = f"/studies/{study_id}/clinical-attributes/{clinical_attribute_id}"
        response = requests.get(f"{self.base_url}{endpoint}")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get the specified clinical attribute in the study. Status code: {response.status_code}")

    #################
    # Clinical Data #
    #################

    def get_all_clinical_data_in_study(self, study_id, attribute_id=None, clinical_data_type="SAMPLE", direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="clinicalAttributeId"):
        """
        Get all clinical data in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param attribute_id: Attribute ID, e.g., "CANCER_TYPE".
        :type attribute_id: str, optional

        :param clinical_data_type: Type of clinical data.
            - "PATIENT": Clinical data for patients.
            - "SAMPLE": Clinical data for samples (default).
        :type clinical_data_type: str, optional, default: "SAMPLE"

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            Possible values:
            - "clinicalAttributeId"
            - "value"
        :type sortBy: str, optional, default: "clinicalAttributeId"

        :returns: List of clinical data in the specified study.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/clinical-data"
        params = {
            "clinicalDataType": clinical_data_type,
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }
        if attribute_id:
            params["attributeId"] = attribute_id

        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get clinical data in the specified study. Status code: {response.status_code}")

    def fetch_all_clinical_data_in_study(self, study_id, clinical_data_filter, clinical_data_type="SAMPLE", projection="SUMMARY"):
        """
        Fetch clinical data by patient IDs or sample IDs in a specific study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param clinical_data_filter: List of patient or sample IDs and attribute IDs.
        :type clinical_data_filter: dict

        :param clinical_data_type: Type of clinical data.
            - "PATIENT": Clinical data for patients.
            - "SAMPLE": Clinical data for samples (default).
        :type clinical_data_type: str, optional, default: "SAMPLE"

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :returns: List of clinical data in the specified study based on the provided filter.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/clinical-data/fetch"
        params = {
            "clinicalDataType": clinical_data_type,
            "projection": projection
        }
        data = {
            "clinicalDataSingleStudyFilter": clinical_data_filter
        }
        response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to fetch clinical data in the specified study. Status code: {response.status_code}")

    ######################
    # Molecular Profiles #
    ######################

    def get_all_molecular_profiles_in_study(self, study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="datatype"):
        """
        Get all molecular profiles in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            Possible values:
            - "datatype"
            - "description"
            - "molecularAlterationType"
            - "molecularProfileId"
            - "name"
            - "showProfileInAnalysisTab"
        :type sortBy: str, optional, default: "datatype"

        :returns: List of molecular profiles in the specified study.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/molecular-profiles"
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }

        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get molecular profiles in the specified study. Status code: {response.status_code}")

    ############
    # Patients #
    ############

    def get_all_patients_in_study(self, study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="patientId"):
        """
        Get all patients in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            - "patientId": Sort by patient ID.
        :type sortBy: str, optional, default: "patientId"

        :returns: List of patients in the specified study.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/patients"
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }

        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get patients in the specified study. Status code: {response.status_code}")

    def get_patient_in_study(self, study_id, patient_id):
        """
        Get a patient in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param patient_id: Patient ID, e.g., "TCGA-OR-A5J2".
        :type patient_id: str

        :returns: Details of the specified patient in the study.
        :rtype: dict
        """
        endpoint = f"/studies/{study_id}/patients/{patient_id}"

        response = requests.get(f"{self.base_url}{endpoint}")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get the specified patient in the study. Status code: {response.status_code}")

    #################
    # Clinical Data #
    #################

    def get_all_clinical_data_of_patient_in_study(self, study_id, patient_id, attributeId=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="clinicalAttributeId"):
        """
        Get all clinical data of a patient in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param patient_id: Patient ID, e.g., "TCGA-OR-A5J2".
        :type patient_id: str

        :param attributeId: Attribute ID, e.g., "AGE".
        :type attributeId: str, optional

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            - "clinicalAttributeId": Sort by clinical attribute ID.
            - "value": Sort by clinical data value.
        :type sortBy: str, optional, default: "clinicalAttributeId"

        :returns: List of clinical data of the specified patient in the study.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/patients/{patient_id}/clinical-data"
        params = {
            "attributeId": attributeId,
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }

        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get clinical data of the specified patient in the study. Status code: {response.status_code}")


    ###########
    # Samples #
    ###########
    
    def get_all_samples_of_patient_in_study(self, study_id, patient_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleId"):
        """
        Get all samples of a patient in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param patient_id: Patient ID, e.g., "TCGA-OR-A5J2".
        :type patient_id: str

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            - "sampleId": Sort by sample ID.
            - "sampleType": Sort by sample type.
        :type sortBy: str, optional, default: "sampleId"

        :returns: List of samples of the specified patient in the study.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/patients/{patient_id}/samples"
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }

        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get samples of the specified patient in the study. Status code: {response.status_code}")
    
    ################
    # Sample Lists #
    ################

    def get_all_sample_lists_in_study(self, study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleListId"):
        """
        Get all sample lists in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            - "category": Sort by category.
            - "description": Sort by description.
            - "name": Sort by name.
            - "sampleListId": Sort by sample list ID.
            - "studyId": Sort by study ID.
        :type sortBy: str, optional, default: "sampleListId"

        :returns: List of sample lists in the specified study.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/sample-lists"
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }

        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get sample lists in the study. Status code: {response.status_code}")
    
    ###########
    # Samples #
    ###########

    def get_all_samples_in_study(self, study_id, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="sampleId"):
        """
        Get all samples in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            - "sampleId": Sort by sample ID.
            - "sampleType": Sort by sample type.
        :type sortBy: str, optional, default: "sampleId"

        :returns: List of samples in the specified study.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/samples"
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
            "sortBy": sortBy
        }

        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get samples in the study. Status code: {response.status_code}")

    def get_sample_in_study(self, study_id, sample_id):
        """
        Get information about a specific sample in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param sample_id: Sample ID, e.g., "TCGA-OR-A5J2-01".
        :type sample_id: str

        :returns: Information about the specified sample.
        :rtype: dict
        """
        endpoint = f"/studies/{study_id}/samples/{sample_id}"

        response = requests.get(f"{self.base_url}{endpoint}")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get sample information. Status code: {response.status_code}")
    
    #################
    # Clinical Data #
    #################

    def get_all_clinical_data_of_sample_in_study(self, study_id, sample_id, attributeId=None, direction="ASC", pageNumber=0, pageSize=10000000, projection="SUMMARY", sortBy="clinicalAttributeId"):
        """
        Get all clinical data of a sample in a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :param sample_id: Sample ID, e.g., "TCGA-OR-A5J2-01".
        :type sample_id: str

        :param attributeId: Attribute ID, e.g., "CANCER_TYPE".
        :type attributeId: str, optional

        :param direction: Direction of the sort.
            - "ASC": Ascending.
            - "DESC": Descending.
        :type direction: str, optional, default: "ASC"

        :param pageNumber: Page number of the result list.
        :type pageNumber: int, optional, default: 0

        :param pageSize: Page size of the result list.
        :type pageSize: int, optional, default: 10000000

        :param projection: Level of detail of the response.
            - "DETAILED": Detailed information.
            - "ID": Information with only IDs.
            - "META": Metadata information.
            - "SUMMARY": Summary information (default).
        :type projection: str, optional, default: "SUMMARY"

        :param sortBy: Name of the property that the result list is sorted by.
            - "clinicalAttributeId": Sort by clinical attribute ID.
            - "value": Sort by clinical data value.
        :type sortBy: str, optional, default: "clinicalAttributeId"

        :returns: List of clinical data for the specified sample in the study.
        :rtype: list[dict]
        """
        endpoint = f"/studies/{study_id}/samples/{sample_id}/clinical-data"
        params = {
            "direction": direction,
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "projection": projection,
        }
        if attributeId:
            params["attributeId"] = attributeId
        if sortBy:
            params["sortBy"] = sortBy

        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get clinical data for the sample. Status code: {response.status_code}")
    
    ########################
    # Copy Number Segments #
    ########################

    def get_copy_number_segments_in_sample_in_study(self, study_id, sample_id, chromosome=None, direction="ASC", pageNumber=0, pageSize=20000, projection="SUMMARY", sortBy="chromosome"):
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

        response = requests.get(f"{self.base_url}{endpoint}", params=params)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get copy number segments for the sample. Status code: {response.status_code}")
    
    ###########
    # Studies #
    ###########

    def get_tags_of_study(self, study_id):
        """
        Get the tags of a study.

        :param study_id: Study ID, e.g., "acc_tcga".
        :type study_id: str

        :return: Dictionary of tags associated with the study.
        :rtype: dict
        """
        endpoint = f"/studies/{study_id}/tags"
        response = requests.get(f"{self.base_url}{endpoint}")

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get tags for the study. Status code: {response.status_code}")
    
    ##############
    # Treatments #
    ##############

    def should_display_patient_level_treatments(self, study_ids, tier="Agent"):
        """
        Check if patient level treatments should be displayed.

        :param study_ids: List of Study IDs.
        :type study_ids: list of str
        :param tier: Tier for treatment (default: "Agent").
        :type tier: str
        :values tier: "Agent" - Display treatments by agent.
                     "AgentClass" - Display treatments by agent class.
                     "AgentTarget" - Display treatments by agent target.

        :return: True if patient level treatments should be displayed, False otherwise.
        :rtype: bool
        """
        endpoint = "/treatments/display-patient"
        params = {"tier": tier}
        data = {"studyIds": study_ids}
        response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to check if patient level treatments should be displayed. Status code: {response.status_code}")

    def should_display_sample_level_treatments(self, study_ids, tier="Agent"):
        """
        Check if sample level treatments should be displayed.

        :param study_ids: List of Study IDs.
        :type study_ids: list of str
        :param tier: Tier for treatment (default: "Agent").
        :type tier: str
        :values tier: "Agent" - Display treatments by agent.
                     "AgentClass" - Display treatments by agent class.
                     "AgentTarget" - Display treatments by agent target.

        :return: True if sample level treatments should be displayed, False otherwise.
        :rtype: bool
        """
        endpoint = "/treatments/display-sample"
        params = {"tier": tier}
        data = {"studyIds": study_ids}
        response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to check if sample level treatments should be displayed. Status code: {response.status_code}")

    def get_all_patient_level_treatments(self, study_view_filter, tier="Agent"):
        """
        Get all patient level treatments.

        :param study_view_filter: Study view filter.
        :type study_view_filter: dict
        :param tier: Tier for treatment (default: "Agent").
        :type tier: str
        :values tier: "Agent" - Display treatments by agent.
                     "AgentClass" - Display treatments by agent class.
                     "AgentTarget" - Display treatments by agent target.

        :return: List of patient treatment rows.
        :rtype: list of dict
        """
        endpoint = "/treatments/patient"
        params = {"tier": tier}
        data = {"studyViewFilter": study_view_filter}
        response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get all patient level treatments. Status code: {response.status_code}")

    def get_all_sample_level_treatments(self, study_view_filter, tier="Agent"):
        """
        Get all sample level treatments.

        :param study_view_filter: Study view filter.
        :type study_view_filter: dict
        :param tier: Tier for treatment (default: "Agent").
        :type tier: str
        :values tier: "Agent" - Display treatments by agent.
                     "AgentClass" - Display treatments by agent class.
                     "AgentTarget" - Display treatments by agent target.

        :return: List of sample treatment rows.
        :rtype: list of dict
        """
        endpoint = "/treatments/sample"
        params = {"tier": tier}
        data = {"studyViewFilter": study_view_filter}
        response = requests.post(f"{self.base_url}{endpoint}", params=params, json=data)

        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            raise Exception(f"Failed to get all sample level treatments. Status code: {response.status_code}")

    