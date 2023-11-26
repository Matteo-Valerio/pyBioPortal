.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pybioportal import gene_panel_data as gpd

.. code:: ipython3

    df1a = gpd.fetch_gene_panel_data(molecular_profile_ids=["brca_tcga_gistic", "acc_tcga_gistic", "brca_tcga_mutations"])
    df1a




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>profiled</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CSC1BMUVTLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-BH-A1ES-01</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1CSC1BMUVTLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-BH-A1ES-06</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
          <td>False</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1CSC1BMUVULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVUOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-BH-A1ET-01</td>
          <td>TCGA-BH-A1ET</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2303</th>
          <td>VENHQS1FMi1BMUI0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUI0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1B4-01</td>
          <td>TCGA-E2-A1B4</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>2304</th>
          <td>VENHQS1FMi1BMUI1LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUI1OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1B5-01</td>
          <td>TCGA-E2-A1B5</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>2305</th>
          <td>VENHQS1FMi1BMUI2LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUI2OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1B6-01</td>
          <td>TCGA-E2-A1B6</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>2306</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>2307</th>
          <td>VENHQS1FMi1BMUJELTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJEOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1BD-01</td>
          <td>TCGA-E2-A1BD</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
      </tbody>
    </table>
    <p>2308 rows × 7 columns</p>
    </div>



.. code:: ipython3

    df1b = gpd.fetch_gene_panel_data(molecular_prof_sample_ids=[
                                                {"molecular_profile_id": "brca_tcga_gistic",
                                                 "sample_ids": ["TCGA-AR-A1AR-01", "TCGA-E2-A1BC-01"]},
                                                {"molecular_profile_id": "brca_tcga_mutations",
                                                 "sample_ids": ["TCGA-AR-A1AR-01", "TCGA-E2-A1BC-01"]},
                                                {"molecular_profile_id": "msk_met_2021_mutations",
                                                 "sample_ids": ["P-0000004-T01-IM3", "P-0000950-T01-IM3"]}
                                      ])
    df1b




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>profiled</th>
          <th>genePanelId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
          <td>True</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>brca_tcga</td>
          <td>True</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>2</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>msk_met_2021_mutations</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>True</td>
          <td>IMPACT341</td>
        </tr>
        <tr>
          <th>3</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>msk_met_2021_mutations</td>
          <td>P-0000950-T01-IM3</td>
          <td>P-0000950</td>
          <td>msk_met_2021</td>
          <td>True</td>
          <td>IMPACT341</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
          <td>True</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>5</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>brca_tcga</td>
          <td>True</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2a = gpd.fetch_gene_panel_data_in_molecular_profile("brca_tcga_mutations",sample_ids=["TCGA-AR-A1AR-01", "TCGA-E2-A1BC-01"])
    df2a




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>profiled</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2b = gpd.fetch_gene_panel_data_in_molecular_profile("brca_tcga_mutations", sample_list_id="brca_tcga_all")
    df2b




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>profiled</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CSC1BMUVTLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A1ES-01</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1CSC1BMUVULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVUOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A1ET-01</td>
          <td>TCGA-BH-A1ET</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1CSC1BMUVVLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVVOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A1EU-01</td>
          <td>TCGA-BH-A1EU</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>1103</th>
          <td>VENHQS1FMi1BMTVBLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTVBOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A15A-06</td>
          <td>TCGA-E2-A15A</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>1104</th>
          <td>VENHQS1CSC1BMThWLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMThWOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A18V-06</td>
          <td>TCGA-BH-A18V</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>1105</th>
          <td>VENHQS1FMi1BMTVLLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTVLOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A15K-06</td>
          <td>TCGA-E2-A15K</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>1106</th>
          <td>VENHQS1FMi1BMTVFLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTVFOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A15E-06</td>
          <td>TCGA-E2-A15E</td>
          <td>brca_tcga</td>
          <td>True</td>
        </tr>
        <tr>
          <th>1107</th>
          <td>VENHQS1BQy1BNklYLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1BQy1BNklYOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AC-A6IX-06</td>
          <td>TCGA-AC-A6IX</td>
          <td>brca_tcga</td>
          <td>False</td>
        </tr>
      </tbody>
    </table>
    <p>1108 rows × 7 columns</p>
    </div>


