.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pybioportal import samples as sp

.. code:: ipython3

    df1 = sp.get_samples_by_keyword(keyword="TCGA")
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
          <th>sampleType</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS0wMi0wMDAxLTAxOmdibV90Y2dhX3Bhbl9jYW5fYX...</td>
          <td>VENHQS0wMi0wMDAxOmdibV90Y2dhX3Bhbl9jYW5fYXRsYX...</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-02-0001-01</td>
          <td>TCGA-02-0001</td>
          <td>gbm_tcga_pan_can_atlas_2018</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS0wMi0wMDAxLTAxOmxnZ2dibV90Y2dhX3B1Yg</td>
          <td>VENHQS0wMi0wMDAxOmxnZ2dibV90Y2dhX3B1Yg</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-02-0001-01</td>
          <td>TCGA-02-0001</td>
          <td>lgggbm_tcga_pub</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS0wMi0wMDAxLTAxOmdibV90Y2dhX3B1Yg</td>
          <td>VENHQS0wMi0wMDAxOmdibV90Y2dhX3B1Yg</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-02-0001-01</td>
          <td>TCGA-02-0001</td>
          <td>gbm_tcga_pub</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS0wMi0wMDAxLTAxOmdibV90Y2dhX3B1YjIwMTM</td>
          <td>VENHQS0wMi0wMDAxOmdibV90Y2dhX3B1YjIwMTM</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-02-0001-01</td>
          <td>TCGA-02-0001</td>
          <td>gbm_tcga_pub2013</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS0wMi0wMDAxLTAxOmdibV90Y2dh</td>
          <td>VENHQS0wMi0wMDAxOmdibV90Y2dh</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-02-0001-01</td>
          <td>TCGA-02-0001</td>
          <td>gbm_tcga</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>33581</th>
          <td>SURUQ0dBLTAyOm1peGVkX21za190Y2dhXzIwMjE</td>
          <td>SURUQ0dBLTAyOm1peGVkX21za190Y2dhXzIwMjE</td>
          <td>Primary Solid Tumor</td>
          <td>IDTCGA-02</td>
          <td>IDTCGA-02</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
        <tr>
          <th>33582</th>
          <td>SURUQ0dBLTAzOm1peGVkX21za190Y2dhXzIwMjE</td>
          <td>SURUQ0dBLTAzOm1peGVkX21za190Y2dhXzIwMjE</td>
          <td>Primary Solid Tumor</td>
          <td>IDTCGA-03</td>
          <td>IDTCGA-03</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
        <tr>
          <th>33583</th>
          <td>SURUQ0dBLTA0Om1peGVkX21za190Y2dhXzIwMjE</td>
          <td>SURUQ0dBLTA0Om1peGVkX21za190Y2dhXzIwMjE</td>
          <td>Primary Solid Tumor</td>
          <td>IDTCGA-04</td>
          <td>IDTCGA-04</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
        <tr>
          <th>33584</th>
          <td>SURUQ0dBLTA1Om1peGVkX21za190Y2dhXzIwMjE</td>
          <td>SURUQ0dBLTA1Om1peGVkX21za190Y2dhXzIwMjE</td>
          <td>Primary Solid Tumor</td>
          <td>IDTCGA-05</td>
          <td>IDTCGA-05</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
        <tr>
          <th>33585</th>
          <td>SURUQ0dBLTA2Om1peGVkX21za190Y2dhXzIwMjE</td>
          <td>SURUQ0dBLTA2Om1peGVkX21za190Y2dhXzIwMjE</td>
          <td>Primary Solid Tumor</td>
          <td>IDTCGA-06</td>
          <td>IDTCGA-06</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
      </tbody>
    </table>
    <p>33586 rows × 6 columns</p>
    </div>



.. code:: ipython3

    df2a = sp.fetch_samples(sample_identifiers=[
                                                {"sample_ids": ["TCGA-AR-A1AR-01","TCGA-BH-A1EO-01","TCGA-BH-A1ES-01"], 
                                                 "study_id": "brca_tcga"},
                                                {"sample_ids": ["TCGA-A2-A0T2-01","TCGA-A2-A04P-01"], 
                                                 "study_id": "brca_tcga_pub"}
                                                ])
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
          <th>sampleType</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CSC1BMUVTLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1ES-01</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1BMi1BMFQyLTAxOmJyY2FfdGNnYV9wdWI</td>
          <td>VENHQS1BMi1BMFQyOmJyY2FfdGNnYV9wdWI</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-A2-A0T2-01</td>
          <td>TCGA-A2-A0T2</td>
          <td>brca_tcga_pub</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1BMi1BMDRQLTAxOmJyY2FfdGNnYV9wdWI</td>
          <td>VENHQS1BMi1BMDRQOmJyY2FfdGNnYV9wdWI</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-A2-A04P-01</td>
          <td>TCGA-A2-A04P</td>
          <td>brca_tcga_pub</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2b = sp.fetch_samples(sample_list_ids=["brca_tcga_cna", "brca_tcga_mrna", "brca_tcga_pub_cna"])
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
          <th>sampleType</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CSC1BMUVTLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1ES-01</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1CSC1BMUVULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVUOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1ET-01</td>
          <td>TCGA-BH-A1ET</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1CSC1BMUVVLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVVOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1EU-01</td>
          <td>TCGA-BH-A1EU</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>2382</th>
          <td>VENHQS1BQy1BMkZGLTAxOmJyY2FfdGNnYV9wdWI</td>
          <td>VENHQS1BQy1BMkZGOmJyY2FfdGNnYV9wdWI</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-AC-A2FF-01</td>
          <td>TCGA-AC-A2FF</td>
          <td>brca_tcga_pub</td>
        </tr>
        <tr>
          <th>2383</th>
          <td>VENHQS1BQy1BMkZCLTAxOmJyY2FfdGNnYV9wdWI</td>
          <td>VENHQS1BQy1BMkZCOmJyY2FfdGNnYV9wdWI</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-AC-A2FB-01</td>
          <td>TCGA-AC-A2FB</td>
          <td>brca_tcga_pub</td>
        </tr>
        <tr>
          <th>2384</th>
          <td>VENHQS1BQy1BMkZHLTAxOmJyY2FfdGNnYV9wdWI</td>
          <td>VENHQS1BQy1BMkZHOmJyY2FfdGNnYV9wdWI</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-AC-A2FG-01</td>
          <td>TCGA-AC-A2FG</td>
          <td>brca_tcga_pub</td>
        </tr>
        <tr>
          <th>2385</th>
          <td>VENHQS1HSS1BMkM4LTAxOmJyY2FfdGNnYV9wdWI</td>
          <td>VENHQS1HSS1BMkM4OmJyY2FfdGNnYV9wdWI</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-GI-A2C8-01</td>
          <td>TCGA-GI-A2C8</td>
          <td>brca_tcga_pub</td>
        </tr>
        <tr>
          <th>2386</th>
          <td>VENHQS1FOS1BMjk1LTAxOmJyY2FfdGNnYV9wdWI</td>
          <td>VENHQS1FOS1BMjk1OmJyY2FfdGNnYV9wdWI</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-E9-A295-01</td>
          <td>TCGA-E9-A295</td>
          <td>brca_tcga_pub</td>
        </tr>
      </tbody>
    </table>
    <p>2387 rows × 6 columns</p>
    </div>



.. code:: ipython3

    df2c = sp.fetch_samples(unique_sample_keys=["VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ",
                                                "VENHQS1CNi1BMElRLTAxOmJyY2FfdGNnYV9wdWI",
                                                "VENHQS1CSC1BMUZELTAxOmJyY2FfdGNnYQ"])
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
          <th>sampleType</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1CSC1BMUZELTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUZEOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1FD-01</td>
          <td>TCGA-BH-A1FD</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CNi1BMElRLTAxOmJyY2FfdGNnYV9wdWI</td>
          <td>VENHQS1CNi1BMElROmJyY2FfdGNnYV9wdWI</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-B6-A0IQ-01</td>
          <td>TCGA-B6-A0IQ</td>
          <td>brca_tcga_pub</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df3 = sp.get_all_samples_of_patient_in_study(study_id="brca_tcga", patient_id="TCGA-AR-A1AR")
    df3




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
          <th>sampleType</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df4 = sp.get_all_samples_in_study(study_id="brca_tcga")
    df4




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
          <th>sampleType</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CSC1BMUVTLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1ES-01</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1CSC1BMUVTLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>Metastatic</td>
          <td>TCGA-BH-A1ES-06</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1CSC1BMUVULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVUOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-BH-A1ET-01</td>
          <td>TCGA-BH-A1ET</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>1103</th>
          <td>VENHQS1FMi1BMUI0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUI0OmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-E2-A1B4-01</td>
          <td>TCGA-E2-A1B4</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1104</th>
          <td>VENHQS1FMi1BMUI1LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUI1OmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-E2-A1B5-01</td>
          <td>TCGA-E2-A1B5</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1105</th>
          <td>VENHQS1FMi1BMUI2LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUI2OmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-E2-A1B6-01</td>
          <td>TCGA-E2-A1B6</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1106</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1107</th>
          <td>VENHQS1FMi1BMUJELTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJEOmJyY2FfdGNnYQ</td>
          <td>Primary Solid Tumor</td>
          <td>TCGA-E2-A1BD-01</td>
          <td>TCGA-E2-A1BD</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    <p>1108 rows × 6 columns</p>
    </div>



.. code:: ipython3

    df5 = sp.get_sample_in_study(study_id="brca_tcga",sample_id="TCGA-AR-A1AR-01")
    df5




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
          <th>sampleType</th>
          <th>sequenced</th>
          <th>copyNumberSegmentPresent</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Primary Solid Tumor</td>
          <td>True</td>
          <td>True</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    </div>


