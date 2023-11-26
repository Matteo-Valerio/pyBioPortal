.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pybioportal import clinical_data as cd

.. code:: ipython3

    df1a = cd.fetch_clinical_data(attribute_ids=["SEX", "RACE"], 
                                  entity_study_ids=[
                                          {"entity_ids": ["P-0000004", "P-0000950"], "study": "msk_met_2021"},
                                          {"entity_ids": ["TCGA-5T-A9QA", "TCGA-A1-A0SB"], "study": "brca_tcga"}
                                  ], 
                                  clinical_data_type="PATIENT", ret_format="LONG")
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
          <th>uniquePatientKey</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>clinicalAttributeId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>brca_tcga</td>
          <td>RACE</td>
          <td>WHITE</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>brca_tcga</td>
          <td>SEX</td>
          <td>Female</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>RACE</td>
          <td>BLACK OR AFRICAN AMERICAN</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>SEX</td>
          <td>Female</td>
        </tr>
        <tr>
          <th>4</th>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>RACE</td>
          <td>White</td>
        </tr>
        <tr>
          <th>5</th>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>SEX</td>
          <td>Female</td>
        </tr>
        <tr>
          <th>6</th>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>msk_met_2021</td>
          <td>RACE</td>
          <td>Other</td>
        </tr>
        <tr>
          <th>7</th>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>msk_met_2021</td>
          <td>SEX</td>
          <td>Male</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df1b = cd.fetch_clinical_data(attribute_ids=["ORGAN_SYSTEM", "SUBTYPE", "CANCER_TYPE", "MUTATION_COUNT"], 
                                  entity_study_ids=[
                                          {"entity_ids": ["P-0000004-T01-IM3", "P-0000950-T01-IM3"], "study": "msk_met_2021"},
                                          {"entity_ids": ["TCGA-5T-A9QA-01", "TCGA-A1-A0SB-01"], "study": "brca_tcga"}
                                  ], 
                                  clinical_data_type="SAMPLE", ret_format="WIDE")
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
          <th>clinicalAttributeId</th>
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>CANCER_TYPE</th>
          <th>MUTATION_COUNT</th>
          <th>ORGAN_SYSTEM</th>
          <th>SUBTYPE</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>Breast Cancer</td>
          <td>4</td>
          <td>Breast</td>
          <td>Breast Ductal HR+HER2-</td>
        </tr>
        <tr>
          <th>1</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950-T01-IM3</td>
          <td>P-0000950</td>
          <td>msk_met_2021</td>
          <td>Small Bowel Cancer</td>
          <td>12</td>
          <td>Core GI</td>
          <td>Small Bowel cancer</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS01VC1BOVFBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA-01</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>Breast Cancer</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>TCGA-A1-A0SB</td>
          <td>brca_tcga</td>
          <td>Breast Cancer</td>
          <td>16</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2a = cd.get_all_clinical_data_in_study("acc_tcga", clinical_data_type="PATIENT")
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
          <th>uniquePatientKey</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>clinicalAttributeId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1PUi1BNUoxOmFjY190Y2dh</td>
          <td>TCGA-OR-A5J1</td>
          <td>acc_tcga</td>
          <td>AGE</td>
          <td>58</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1PUi1BNUoxOmFjY190Y2dh</td>
          <td>TCGA-OR-A5J1</td>
          <td>acc_tcga</td>
          <td>AJCC_PATHOLOGIC_TUMOR_STAGE</td>
          <td>Stage II</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1PUi1BNUoxOmFjY190Y2dh</td>
          <td>TCGA-OR-A5J1</td>
          <td>acc_tcga</td>
          <td>ATYPICAL_MITOTIC_FIGURES</td>
          <td>Atypical Mitotic Figures Absent</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1PUi1BNUoxOmFjY190Y2dh</td>
          <td>TCGA-OR-A5J1</td>
          <td>acc_tcga</td>
          <td>CAPSULAR_INVASION</td>
          <td>Invasion of Tumor Capsule Absent</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1PUi1BNUoxOmFjY190Y2dh</td>
          <td>TCGA-OR-A5J1</td>
          <td>acc_tcga</td>
          <td>CLIN_M_STAGE</td>
          <td>M0</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>4729</th>
          <td>VENHQS1QSy1BNUhDOmFjY190Y2dh</td>
          <td>TCGA-PK-A5HC</td>
          <td>acc_tcga</td>
          <td>SITE_OF_TUMOR_TISSUE</td>
          <td>Adrenal</td>
        </tr>
        <tr>
          <th>4730</th>
          <td>VENHQS1QSy1BNUhDOmFjY190Y2dh</td>
          <td>TCGA-PK-A5HC</td>
          <td>acc_tcga</td>
          <td>TISSUE_SOURCE_SITE</td>
          <td>PK</td>
        </tr>
        <tr>
          <th>4731</th>
          <td>VENHQS1QSy1BNUhDOmFjY190Y2dh</td>
          <td>TCGA-PK-A5HC</td>
          <td>acc_tcga</td>
          <td>TREATMENT_OUTCOME_FIRST_COURSE</td>
          <td>Complete Remission/Response</td>
        </tr>
        <tr>
          <th>4732</th>
          <td>VENHQS1QSy1BNUhDOmFjY190Y2dh</td>
          <td>TCGA-PK-A5HC</td>
          <td>acc_tcga</td>
          <td>TUMOR_STATUS</td>
          <td>WITH TUMOR</td>
        </tr>
        <tr>
          <th>4733</th>
          <td>VENHQS1QSy1BNUhDOmFjY190Y2dh</td>
          <td>TCGA-PK-A5HC</td>
          <td>acc_tcga</td>
          <td>WEISS_VENOUS_INVASION</td>
          <td>Venous Invasion Present</td>
        </tr>
      </tbody>
    </table>
    <p>4734 rows × 5 columns</p>
    </div>



.. code:: ipython3

    df2b = cd.get_all_clinical_data_in_study("brca_tcga", attribute_id="MUTATION_COUNT")
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
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>clinicalAttributeId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>40</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>27</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CSC1BMUVTLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>TCGA-BH-A1ES-01</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>15</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1CSC1BMUVTLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>TCGA-BH-A1ES-06</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>23</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1CSC1BMUVULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVUOmJyY2FfdGNnYQ</td>
          <td>TCGA-BH-A1ET-01</td>
          <td>TCGA-BH-A1ET</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>16</td>
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
          <th>977</th>
          <td>VENHQS1FMi1BMUI0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUI0OmJyY2FfdGNnYQ</td>
          <td>TCGA-E2-A1B4-01</td>
          <td>TCGA-E2-A1B4</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>27</td>
        </tr>
        <tr>
          <th>978</th>
          <td>VENHQS1FMi1BMUI1LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUI1OmJyY2FfdGNnYQ</td>
          <td>TCGA-E2-A1B5-01</td>
          <td>TCGA-E2-A1B5</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>12</td>
        </tr>
        <tr>
          <th>979</th>
          <td>VENHQS1FMi1BMUI2LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUI2OmJyY2FfdGNnYQ</td>
          <td>TCGA-E2-A1B6-01</td>
          <td>TCGA-E2-A1B6</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>7</td>
        </tr>
        <tr>
          <th>980</th>
          <td>VENHQS1FMi1BMUJDLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>TCGA-E2-A1BC-01</td>
          <td>TCGA-E2-A1BC</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>24</td>
        </tr>
        <tr>
          <th>981</th>
          <td>VENHQS1FMi1BMUJELTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUJEOmJyY2FfdGNnYQ</td>
          <td>TCGA-E2-A1BD-01</td>
          <td>TCGA-E2-A1BD</td>
          <td>brca_tcga</td>
          <td>MUTATION_COUNT</td>
          <td>23</td>
        </tr>
      </tbody>
    </table>
    <p>982 rows × 7 columns</p>
    </div>



.. code:: ipython3

    df3a = cd.fetch_all_clinical_data_in_study(study_id="brca_tcga", 
                                               attribute_ids=["SEX", "RACE"],
                                               ids=["TCGA-5T-A9QA", "TCGA-A1-A0SB"],
                                               clinical_data_type="PATIENT", ret_format="LONG")
    df3a




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
          <th>uniquePatientKey</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>clinicalAttributeId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>brca_tcga</td>
          <td>RACE</td>
          <td>WHITE</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>brca_tcga</td>
          <td>SEX</td>
          <td>Female</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>RACE</td>
          <td>BLACK OR AFRICAN AMERICAN</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>SEX</td>
          <td>Female</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    
    df3b = cd.fetch_all_clinical_data_in_study(study_id="brca_tcga",                                            
                                               ids=["TCGA-5T-A9QA", "TCGA-A1-A0SB"],
                                               clinical_data_type="PATIENT", ret_format="WIDE")
    df3b




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
          <th>clinicalAttributeId</th>
          <th>uniquePatientKey</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>AGE</th>
          <th>AJCC_METASTASIS_PATHOLOGIC_PM</th>
          <th>AJCC_NODES_PATHOLOGIC_PN</th>
          <th>AJCC_PATHOLOGIC_TUMOR_STAGE</th>
          <th>AJCC_STAGING_EDITION</th>
          <th>AJCC_TUMOR_PATHOLOGIC_PT</th>
          <th>DAYS_TO_INITIAL_PATHOLOGIC_DIAGNOSIS</th>
          <th>...</th>
          <th>PR_STATUS_BY_IHC</th>
          <th>RACE</th>
          <th>RETROSPECTIVE_COLLECTION</th>
          <th>SAMPLE_COUNT</th>
          <th>SEX</th>
          <th>SITE_OF_TUMOR_TISSUE</th>
          <th>STAGING_SYSTEM</th>
          <th>SURGICAL_PROCEDURE_FIRST</th>
          <th>TISSUE_SOURCE_SITE</th>
          <th>TUMOR_STATUS</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>52</td>
          <td>MX</td>
          <td>NX</td>
          <td>Stage IIA</td>
          <td>7th</td>
          <td>T2</td>
          <td>0</td>
          <td>...</td>
          <td>Negative</td>
          <td>BLACK OR AFRICAN AMERICAN</td>
          <td>NO</td>
          <td>1</td>
          <td>Female</td>
          <td>Breast</td>
          <td>No axillary staging</td>
          <td>NaN</td>
          <td>5T</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>brca_tcga</td>
          <td>70</td>
          <td>M0</td>
          <td>N0</td>
          <td>Stage I</td>
          <td>6th</td>
          <td>T1c</td>
          <td>0</td>
          <td>...</td>
          <td>Negative</td>
          <td>WHITE</td>
          <td>YES</td>
          <td>1</td>
          <td>Female</td>
          <td>Breast</td>
          <td>Sentinel node biopsy alone</td>
          <td>Lumpectomy</td>
          <td>A1</td>
          <td>TUMOR FREE</td>
        </tr>
      </tbody>
    </table>
    <p>2 rows × 54 columns</p>
    </div>



.. code:: ipython3

    
    df3c = cd.fetch_all_clinical_data_in_study(study_id="msk_met_2021", 
                                               attribute_ids=["CANCER_TYPE", "MUTATION_COUNT"], 
                                               ids=["P-0000004-T01-IM3", "P-0000950-T01-IM3"],
                                               clinical_data_type="SAMPLE", ret_format="WIDE")
    df3c




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
          <th>clinicalAttributeId</th>
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>CANCER_TYPE</th>
          <th>MUTATION_COUNT</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>Breast Cancer</td>
          <td>4</td>
        </tr>
        <tr>
          <th>1</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950-T01-IM3</td>
          <td>P-0000950</td>
          <td>msk_met_2021</td>
          <td>Small Bowel Cancer</td>
          <td>12</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df4 = cd.get_all_clinical_data_of_patient_in_study(study_id="brca_tcga", patient_id="TCGA-5T-A9QA")
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
          <th>uniquePatientKey</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>clinicalAttributeId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>AGE</td>
          <td>52</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>AJCC_METASTASIS_PATHOLOGIC_PM</td>
          <td>MX</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>AJCC_NODES_PATHOLOGIC_PN</td>
          <td>NX</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>AJCC_PATHOLOGIC_TUMOR_STAGE</td>
          <td>Stage IIA</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>AJCC_STAGING_EDITION</td>
          <td>7th</td>
        </tr>
        <tr>
          <th>5</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>AJCC_TUMOR_PATHOLOGIC_PT</td>
          <td>T2</td>
        </tr>
        <tr>
          <th>6</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>DAYS_TO_INITIAL_PATHOLOGIC_DIAGNOSIS</td>
          <td>0</td>
        </tr>
        <tr>
          <th>7</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>DFS_MONTHS</td>
          <td>9.95</td>
        </tr>
        <tr>
          <th>8</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>DFS_STATUS</td>
          <td>0:DiseaseFree</td>
        </tr>
        <tr>
          <th>9</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>ER_POSITIVITY_SCALE_USED</td>
          <td>3 Point Scale</td>
        </tr>
        <tr>
          <th>10</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>ER_STATUS_BY_IHC</td>
          <td>Positive</td>
        </tr>
        <tr>
          <th>11</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>ER_STATUS_IHC_PERCENT_POSITIVE</td>
          <td>70-79%</td>
        </tr>
        <tr>
          <th>12</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>ETHNICITY</td>
          <td>NOT HISPANIC OR LATINO</td>
        </tr>
        <tr>
          <th>13</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>FORM_COMPLETION_DATE</td>
          <td>12/23/13</td>
        </tr>
        <tr>
          <th>14</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>HER2_FISH_STATUS</td>
          <td>Negative</td>
        </tr>
        <tr>
          <th>15</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>HER2_IHC_PERCENT_POSITIVE</td>
          <td>10-19%</td>
        </tr>
        <tr>
          <th>16</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>HER2_IHC_SCORE</td>
          <td>2</td>
        </tr>
        <tr>
          <th>17</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>HISTOLOGICAL_DIAGNOSIS</td>
          <td>Other, specify</td>
        </tr>
        <tr>
          <th>18</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>HISTORY_NEOADJUVANT_TRTYN</td>
          <td>No</td>
        </tr>
        <tr>
          <th>19</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>HISTORY_OTHER_MALIGNANCY</td>
          <td>No</td>
        </tr>
        <tr>
          <th>20</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>ICD_10</td>
          <td>C50.9</td>
        </tr>
        <tr>
          <th>21</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>ICD_O_3_HISTOLOGY</td>
          <td>8523/3</td>
        </tr>
        <tr>
          <th>22</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>ICD_O_3_SITE</td>
          <td>C50.9</td>
        </tr>
        <tr>
          <th>23</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>IHC_HER2</td>
          <td>Equivocal</td>
        </tr>
        <tr>
          <th>24</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>IHC_SCORE</td>
          <td>2</td>
        </tr>
        <tr>
          <th>25</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>INFORMED_CONSENT_VERIFIED</td>
          <td>YES</td>
        </tr>
        <tr>
          <th>26</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>INITIAL_PATHOLOGIC_DX_YEAR</td>
          <td>2013</td>
        </tr>
        <tr>
          <th>27</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>LYMPH_NODES_EXAMINED</td>
          <td>NO</td>
        </tr>
        <tr>
          <th>28</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>METHOD_OF_INITIAL_SAMPLE_PROCUREMENT</td>
          <td>Excisional Biopsy</td>
        </tr>
        <tr>
          <th>29</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>MICROMET_DETECTION_BY_IHC</td>
          <td>NO</td>
        </tr>
        <tr>
          <th>30</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>NEW_TUMOR_EVENT_AFTER_INITIAL_TREATMENT</td>
          <td>NO</td>
        </tr>
        <tr>
          <th>31</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>OS_MONTHS</td>
          <td>9.95</td>
        </tr>
        <tr>
          <th>32</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>OS_STATUS</td>
          <td>0:LIVING</td>
        </tr>
        <tr>
          <th>33</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>OTHER_PATIENT_ID</td>
          <td>2FD36838-5A83-433E-AC80-B1F77448E5AA</td>
        </tr>
        <tr>
          <th>34</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>PRIMARY_SITE_PATIENT</td>
          <td>Left</td>
        </tr>
        <tr>
          <th>35</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>PROSPECTIVE_COLLECTION</td>
          <td>YES</td>
        </tr>
        <tr>
          <th>36</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>PR_STATUS_BY_IHC</td>
          <td>Negative</td>
        </tr>
        <tr>
          <th>37</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>RACE</td>
          <td>BLACK OR AFRICAN AMERICAN</td>
        </tr>
        <tr>
          <th>38</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>RETROSPECTIVE_COLLECTION</td>
          <td>NO</td>
        </tr>
        <tr>
          <th>39</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>SAMPLE_COUNT</td>
          <td>1</td>
        </tr>
        <tr>
          <th>40</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>SEX</td>
          <td>Female</td>
        </tr>
        <tr>
          <th>41</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>SITE_OF_TUMOR_TISSUE</td>
          <td>Breast</td>
        </tr>
        <tr>
          <th>42</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>STAGING_SYSTEM</td>
          <td>No axillary staging</td>
        </tr>
        <tr>
          <th>43</th>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>TISSUE_SOURCE_SITE</td>
          <td>5T</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df5 = cd.get_all_clinical_data_of_sample_in_study(study_id="msk_met_2021", sample_id="P-0000004-T01-IM3")
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
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>clinicalAttributeId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>CANCER_TYPE</td>
          <td>Breast Cancer</td>
        </tr>
        <tr>
          <th>1</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>CANCER_TYPE_DETAILED</td>
          <td>Breast Invasive Ductal Carcinoma</td>
        </tr>
        <tr>
          <th>2</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_ADRENAL_GLAND</td>
          <td>No</td>
        </tr>
        <tr>
          <th>3</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_BILIARY_TRACT</td>
          <td>No</td>
        </tr>
        <tr>
          <th>4</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_BLADDER_UT</td>
          <td>No</td>
        </tr>
        <tr>
          <th>5</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_BONE</td>
          <td>Yes</td>
        </tr>
        <tr>
          <th>6</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_BOWEL</td>
          <td>No</td>
        </tr>
        <tr>
          <th>7</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_BREAST</td>
          <td>No</td>
        </tr>
        <tr>
          <th>8</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_CNS_BRAIN</td>
          <td>No</td>
        </tr>
        <tr>
          <th>9</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_DIST_LN</td>
          <td>No</td>
        </tr>
        <tr>
          <th>10</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_FEMALE_GENITAL</td>
          <td>No</td>
        </tr>
        <tr>
          <th>11</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_HEAD_NECK</td>
          <td>No</td>
        </tr>
        <tr>
          <th>12</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_INTRA_ABDOMINAL</td>
          <td>No</td>
        </tr>
        <tr>
          <th>13</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_KIDNEY</td>
          <td>No</td>
        </tr>
        <tr>
          <th>14</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_LIVER</td>
          <td>Yes</td>
        </tr>
        <tr>
          <th>15</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_LUNG</td>
          <td>No</td>
        </tr>
        <tr>
          <th>16</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_MALE_GENITAL</td>
          <td>No</td>
        </tr>
        <tr>
          <th>17</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_MEDIASTINUM</td>
          <td>No</td>
        </tr>
        <tr>
          <th>18</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_OVARY</td>
          <td>No</td>
        </tr>
        <tr>
          <th>19</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_PLEURA</td>
          <td>No</td>
        </tr>
        <tr>
          <th>20</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_PNS</td>
          <td>No</td>
        </tr>
        <tr>
          <th>21</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_SKIN</td>
          <td>No</td>
        </tr>
        <tr>
          <th>22</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>DMETS_DX_UNSPECIFIED</td>
          <td>No</td>
        </tr>
        <tr>
          <th>23</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>FGA</td>
          <td>0.278</td>
        </tr>
        <tr>
          <th>24</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>FRACTION_GENOME_ALTERED</td>
          <td>0.2782</td>
        </tr>
        <tr>
          <th>25</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>GENE_PANEL</td>
          <td>IMPACT341</td>
        </tr>
        <tr>
          <th>26</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>IS_DIST_MET_MAPPED</td>
          <td>TRUE</td>
        </tr>
        <tr>
          <th>27</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>MET_COUNT</td>
          <td>2</td>
        </tr>
        <tr>
          <th>28</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>MET_SITE_COUNT</td>
          <td>2</td>
        </tr>
        <tr>
          <th>29</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>MSI_SCORE</td>
          <td>2.5</td>
        </tr>
        <tr>
          <th>30</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>MSI_TYPE</td>
          <td>Stable</td>
        </tr>
        <tr>
          <th>31</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>MUTATION_COUNT</td>
          <td>4</td>
        </tr>
        <tr>
          <th>32</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>ONCOTREE_CODE</td>
          <td>IDC</td>
        </tr>
        <tr>
          <th>33</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>ORGAN_SYSTEM</td>
          <td>Breast</td>
        </tr>
        <tr>
          <th>34</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>PRIMARY_SITE</td>
          <td>Breast</td>
        </tr>
        <tr>
          <th>35</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>SAMPLE_COVERAGE</td>
          <td>428</td>
        </tr>
        <tr>
          <th>36</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>SAMPLE_TYPE</td>
          <td>Primary</td>
        </tr>
        <tr>
          <th>37</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>SUBTYPE</td>
          <td>Breast Ductal HR+HER2-</td>
        </tr>
        <tr>
          <th>38</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>SUBTYPE_ABBREVIATION</td>
          <td>IDC HR+HER2-</td>
        </tr>
        <tr>
          <th>39</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>TMB_NONSYNONYMOUS</td>
          <td>4.43662120239</td>
        </tr>
        <tr>
          <th>40</th>
          <td>UC0wMDAwMDA0LVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwMDA0Om1za19tZXRfMjAyMQ</td>
          <td>P-0000004-T01-IM3</td>
          <td>P-0000004</td>
          <td>msk_met_2021</td>
          <td>TUMOR_PURITY</td>
          <td>50</td>
        </tr>
      </tbody>
    </table>
    </div>


