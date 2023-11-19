.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioPortal import patients as pts

.. code:: ipython3

    df1 = pts.get_all_patients(keyword="TCGA")
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
          <th>uniquePatientKey</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS0wMi0wMDAxOmdibV90Y2dhX3B1Yg</td>
          <td>TCGA-02-0001</td>
          <td>gbm_tcga_pub</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS0wMi0wMDAxOmdibV90Y2dhX3B1YjIwMTM</td>
          <td>TCGA-02-0001</td>
          <td>gbm_tcga_pub2013</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS0wMi0wMDAxOmxnZ2dibV90Y2dhX3B1Yg</td>
          <td>TCGA-02-0001</td>
          <td>lgggbm_tcga_pub</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS0wMi0wMDAxOmdibV90Y2dhX3Bhbl9jYW5fYXRsYX...</td>
          <td>TCGA-02-0001</td>
          <td>gbm_tcga_pan_can_atlas_2018</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS0wMi0wMDAxOmdibV90Y2dh</td>
          <td>TCGA-02-0001</td>
          <td>gbm_tcga</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>33581</th>
          <td>SURUQ0dBLTAyOm1peGVkX21za190Y2dhXzIwMjE</td>
          <td>IDTCGA-02</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
        <tr>
          <th>33582</th>
          <td>SURUQ0dBLTAzOm1peGVkX21za190Y2dhXzIwMjE</td>
          <td>IDTCGA-03</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
        <tr>
          <th>33583</th>
          <td>SURUQ0dBLTA0Om1peGVkX21za190Y2dhXzIwMjE</td>
          <td>IDTCGA-04</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
        <tr>
          <th>33584</th>
          <td>SURUQ0dBLTA1Om1peGVkX21za190Y2dhXzIwMjE</td>
          <td>IDTCGA-05</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
        <tr>
          <th>33585</th>
          <td>SURUQ0dBLTA2Om1peGVkX21za190Y2dhXzIwMjE</td>
          <td>IDTCGA-06</td>
          <td>mixed_msk_tcga_2021</td>
        </tr>
      </tbody>
    </table>
    <p>33586 rows × 3 columns</p>
    </div>



.. code:: ipython3

    df2a = pts.fetch_patients(patient_identifiers=[
                                                   {"patient_ids": ["TCGA-3C-AAAU","TCGA-3C-AALI"], 
                                                    "study_id": "brca_tcga"},
                                                   {"patient_ids": ["TCGA-A1-A0SB","TCGA-A1-A0SD"], 
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
          <th>uniquePatientKey</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS0zQy1BQUFVOmJyY2FfdGNnYQ</td>
          <td>TCGA-3C-AAAU</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS0zQy1BQUxJOmJyY2FfdGNnYQ</td>
          <td>TCGA-3C-AALI</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1BMS1BMFNEOmJyY2FfdGNnYV9wdWI</td>
          <td>TCGA-A1-A0SD</td>
          <td>brca_tcga_pub</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYV9wdWI</td>
          <td>TCGA-A1-A0SB</td>
          <td>brca_tcga_pub</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2b = pts.fetch_patients(unique_patient_keys=["VENHQS0zQy1BQUFVOmJyY2FfdGNnYQ", 
                                                   "VENHQS1BMS1BMFNEOmJyY2FfdGNnYV9wdWI"], projection="DETAILED")   
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
          <th>uniquePatientKey</th>
          <th>cancerStudy_name</th>
          <th>cancerStudy_description</th>
          <th>cancerStudy_publicStudy</th>
          <th>cancerStudy_groups</th>
          <th>cancerStudy_status</th>
          <th>cancerStudy_importDate</th>
          <th>cancerStudy_readPermission</th>
          <th>cancerStudy_studyId</th>
          <th>cancerStudy_cancerTypeId</th>
          <th>cancerStudy_referenceGenome</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>cancerStudy_pmid</th>
          <th>cancerStudy_citation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS0zQy1BQUFVOmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-3C-AAAU</td>
          <td>brca_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BMS1BMFNEOmJyY2FfdGNnYV9wdWI</td>
          <td>Breast Invasive Carcinoma (TCGA, Nature 2012)</td>
          <td>Whole-exome sequencing (510 samples with match...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-06-21 17:11:52</td>
          <td>True</td>
          <td>brca_tcga_pub</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-A1-A0SD</td>
          <td>brca_tcga_pub</td>
          <td>23000897</td>
          <td>TCGA, Nature 2012</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df3 = pts.get_all_patients_in_study(study_id="brca_tcga", projection="DETAILED")
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
          <th>uniquePatientKey</th>
          <th>cancerStudy_name</th>
          <th>cancerStudy_description</th>
          <th>cancerStudy_publicStudy</th>
          <th>cancerStudy_groups</th>
          <th>cancerStudy_status</th>
          <th>cancerStudy_importDate</th>
          <th>cancerStudy_readPermission</th>
          <th>cancerStudy_studyId</th>
          <th>cancerStudy_cancerTypeId</th>
          <th>cancerStudy_referenceGenome</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CSC1BMUVTOmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-BH-A1ES</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1CSC1BMUVUOmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-BH-A1ET</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1CSC1BMUVVOmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
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
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>1096</th>
          <td>VENHQS1FMi1BMUI0OmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-E2-A1B4</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1097</th>
          <td>VENHQS1FMi1BMUI1OmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-E2-A1B5</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1098</th>
          <td>VENHQS1FMi1BMUI2OmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-E2-A1B6</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1099</th>
          <td>VENHQS1FMi1BMUJDOmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-E2-A1BC</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1100</th>
          <td>VENHQS1FMi1BMUJEOmJyY2FfdGNnYQ</td>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-E2-A1BD</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    <p>1101 rows × 13 columns</p>
    </div>



.. code:: ipython3

    df4 = pts.get_patient_in_study(patient_id="TCGA-3C-AAAU", study_id="brca_tcga")
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
          <th>cancerStudy_name</th>
          <th>cancerStudy_description</th>
          <th>cancerStudy_publicStudy</th>
          <th>cancerStudy_groups</th>
          <th>cancerStudy_status</th>
          <th>cancerStudy_importDate</th>
          <th>cancerStudy_readPermission</th>
          <th>cancerStudy_studyId</th>
          <th>cancerStudy_cancerTypeId</th>
          <th>cancerStudy_referenceGenome</th>
          <th>patientId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>True</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>hg19</td>
          <td>TCGA-3C-AAAU</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    </div>


