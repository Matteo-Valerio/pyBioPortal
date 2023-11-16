.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioGate import discrete_copy_number_alterations as dcna

.. code:: ipython3

    df1 = dcna.get_discrete_copy_numbers_in_molecular_profile(molecular_profile_id="brca_tcga_gistic", 
                                                              sample_list_id="brca_tcga_all", 
                                                              projection="SUMMARY")
    df1




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
          <th>entrezGeneId</th>
          <th>studyId</th>
          <th>alteration</th>
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
          <td>4853</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>51205</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>100874392</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>284615</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>148741</td>
          <td>brca_tcga</td>
          <td>2</td>
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
          <td>...</td>
        </tr>
        <tr>
          <th>613540</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>57606</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>613541</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>201780</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>613542</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>7006</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>613543</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>326340</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>613544</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>9750</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
      </tbody>
    </table>
    <p>613545 rows × 8 columns</p>
    </div>



.. code:: ipython3

    df2a = dcna.fetch_discrete_copy_numbers_in_molecular_profile(molecular_profile_id="brca_tcga_gistic", 
                                                                 entrez_gene_ids=[2023,4853,54940], 
                                                                 sample_ids=["TCGA-AR-A1AR-01", "TCGA-E2-A1BC-01"])
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
          <th>entrezGeneId</th>
          <th>studyId</th>
          <th>alteration</th>
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
          <td>4853</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>54940</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2b = dcna.fetch_discrete_copy_numbers_in_molecular_profile(molecular_profile_id="brca_tcga_gistic", 
                                                                 entrez_gene_ids=[2023,4853,54940], 
                                                                 sample_list_id="brca_tcga_all")
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
          <th>entrezGeneId</th>
          <th>studyId</th>
          <th>alteration</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BQy1BMjNILTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BQy1BMjNIOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AC-A23H-01</td>
          <td>TCGA-AC-A23H</td>
          <td>2023</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1HTS1BM1hMLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1HTS1BM1hMOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-GM-A3XL-01</td>
          <td>TCGA-GM-A3XL</td>
          <td>2023</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1BNy1BNFNFLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BNy1BNFNFOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-A7-A4SE-01</td>
          <td>TCGA-A7-A4SE</td>
          <td>2023</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1PTC1BOTdDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1PTC1BOTdDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-OL-A97C-01</td>
          <td>TCGA-OL-A97C</td>
          <td>2023</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1BOC1BMDlYLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BOC1BMDlYOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-A8-A09X-01</td>
          <td>TCGA-A8-A09X</td>
          <td>2023</td>
          <td>brca_tcga</td>
          <td>-2</td>
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
          <td>...</td>
        </tr>
        <tr>
          <th>168</th>
          <td>VENHQS1BMi1BMDRULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMDRUOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-A2-A04T-01</td>
          <td>TCGA-A2-A04T</td>
          <td>54940</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>169</th>
          <td>VENHQS1BTy1BMEo0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTy1BMEo0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AO-A0J4-01</td>
          <td>TCGA-AO-A0J4</td>
          <td>54940</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>170</th>
          <td>VENHQS1BUS1BMDRMLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUS1BMDRMOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AQ-A04L-01</td>
          <td>TCGA-AQ-A04L</td>
          <td>54940</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>171</th>
          <td>VENHQS1BMi1BMDRVLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMDRVOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-A2-A04U-01</td>
          <td>TCGA-A2-A04U</td>
          <td>54940</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>172</th>
          <td>VENHQS1CSC1BMEJQLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMEJQOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-BH-A0BP-01</td>
          <td>TCGA-BH-A0BP</td>
          <td>54940</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
      </tbody>
    </table>
    <p>173 rows × 8 columns</p>
    </div>



.. code:: ipython3

    df2c = dcna.fetch_discrete_copy_numbers_in_molecular_profile(molecular_profile_id="brca_tcga_gistic", 
                                                                 sample_list_id="brca_tcga_all")
    df2c




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
          <th>entrezGeneId</th>
          <th>studyId</th>
          <th>alteration</th>
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
          <td>4853</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>51205</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>100874392</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>284615</td>
          <td>brca_tcga</td>
          <td>2</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>148741</td>
          <td>brca_tcga</td>
          <td>2</td>
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
          <td>...</td>
        </tr>
        <tr>
          <th>613540</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>57606</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>613541</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>201780</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>613542</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>7006</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>613543</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>326340</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>613544</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_gistic</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>9750</td>
          <td>brca_tcga</td>
          <td>-2</td>
        </tr>
      </tbody>
    </table>
    <p>613545 rows × 8 columns</p>
    </div>


