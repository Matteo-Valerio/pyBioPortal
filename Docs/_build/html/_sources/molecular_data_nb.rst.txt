.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioGate import molecular_data as md

.. code:: ipython3

    df1a = md.fetch_molecular_data(entrez_gene_ids=["672","675"], 
                                   molecular_profile_ids=["brca_tcga_mrna", "acc_tcga_rna_seq_v2_mrna"])
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
          <th>entrezGeneId</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1PUi1BNUoxLTAxOmFjY190Y2dh</td>
          <td>VENHQS1PUi1BNUoxOmFjY190Y2dh</td>
          <td>672</td>
          <td>acc_tcga_rna_seq_v2_mrna</td>
          <td>TCGA-OR-A5J1-01</td>
          <td>TCGA-OR-A5J1</td>
          <td>acc_tcga</td>
          <td>40.345800</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1PUi1BNUoxLTAxOmFjY190Y2dh</td>
          <td>VENHQS1PUi1BNUoxOmFjY190Y2dh</td>
          <td>675</td>
          <td>acc_tcga_rna_seq_v2_mrna</td>
          <td>TCGA-OR-A5J1-01</td>
          <td>TCGA-OR-A5J1</td>
          <td>acc_tcga</td>
          <td>15.850100</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1PUi1BNUoyLTAxOmFjY190Y2dh</td>
          <td>VENHQS1PUi1BNUoyOmFjY190Y2dh</td>
          <td>672</td>
          <td>acc_tcga_rna_seq_v2_mrna</td>
          <td>TCGA-OR-A5J2-01</td>
          <td>TCGA-OR-A5J2</td>
          <td>acc_tcga</td>
          <td>177.560000</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1PUi1BNUoyLTAxOmFjY190Y2dh</td>
          <td>VENHQS1PUi1BNUoyOmFjY190Y2dh</td>
          <td>675</td>
          <td>acc_tcga_rna_seq_v2_mrna</td>
          <td>TCGA-OR-A5J2-01</td>
          <td>TCGA-OR-A5J2</td>
          <td>acc_tcga</td>
          <td>29.392000</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1PUi1BNUozLTAxOmFjY190Y2dh</td>
          <td>VENHQS1PUi1BNUozOmFjY190Y2dh</td>
          <td>672</td>
          <td>acc_tcga_rna_seq_v2_mrna</td>
          <td>TCGA-OR-A5J3-01</td>
          <td>TCGA-OR-A5J3</td>
          <td>acc_tcga</td>
          <td>47.992900</td>
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
          <th>1211</th>
          <td>VENHQS1FMi1BMTVBLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTVBOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_mrna</td>
          <td>TCGA-E2-A15A-06</td>
          <td>TCGA-E2-A15A</td>
          <td>brca_tcga</td>
          <td>-1.171750</td>
        </tr>
        <tr>
          <th>1212</th>
          <td>VENHQS1FMi1BMTVLLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTVLOmJyY2FfdGNnYQ</td>
          <td>672</td>
          <td>brca_tcga_mrna</td>
          <td>TCGA-E2-A15K-06</td>
          <td>TCGA-E2-A15K</td>
          <td>brca_tcga</td>
          <td>-0.918167</td>
        </tr>
        <tr>
          <th>1213</th>
          <td>VENHQS1FMi1BMTVLLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTVLOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_mrna</td>
          <td>TCGA-E2-A15K-06</td>
          <td>TCGA-E2-A15K</td>
          <td>brca_tcga</td>
          <td>-0.193000</td>
        </tr>
        <tr>
          <th>1214</th>
          <td>VENHQS1FMi1BMTVFLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTVFOmJyY2FfdGNnYQ</td>
          <td>672</td>
          <td>brca_tcga_mrna</td>
          <td>TCGA-E2-A15E-06</td>
          <td>TCGA-E2-A15E</td>
          <td>brca_tcga</td>
          <td>-1.898417</td>
        </tr>
        <tr>
          <th>1215</th>
          <td>VENHQS1FMi1BMTVFLTA2OmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTVFOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_mrna</td>
          <td>TCGA-E2-A15E-06</td>
          <td>TCGA-E2-A15E</td>
          <td>brca_tcga</td>
          <td>-2.228000</td>
        </tr>
      </tbody>
    </table>
    <p>1216 rows × 8 columns</p>
    </div>



.. code:: ipython3

    df1b = md.fetch_molecular_data(entrez_gene_ids=["672","675"],
                                   sample_molecular_identifiers=[
                                             {"molecular_profile_id": "brca_tcga_mrna", 
                                              "sample_ids": ["TCGA-AR-A1AR-01","TCGA-BH-A1EO-01"]},
                                             {"molecular_profile_id": "acc_tcga_rna_seq_v2_mrna", 
                                              "sample_ids": ["TCGA-OR-A5J1-01","TCGA-OR-A5J2"]}
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
          <th>entrezGeneId</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>672</td>
          <td>brca_tcga_mrna</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
          <td>-1.224333</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BUi1BMUFSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFSOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_mrna</td>
          <td>TCGA-AR-A1AR-01</td>
          <td>TCGA-AR-A1AR</td>
          <td>brca_tcga</td>
          <td>0.027250</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>672</td>
          <td>brca_tcga_mrna</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
          <td>-1.739417</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_mrna</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
          <td>-1.380500</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1PUi1BNUoxLTAxOmFjY190Y2dh</td>
          <td>VENHQS1PUi1BNUoxOmFjY190Y2dh</td>
          <td>672</td>
          <td>acc_tcga_rna_seq_v2_mrna</td>
          <td>TCGA-OR-A5J1-01</td>
          <td>TCGA-OR-A5J1</td>
          <td>acc_tcga</td>
          <td>40.345800</td>
        </tr>
        <tr>
          <th>5</th>
          <td>VENHQS1PUi1BNUoxLTAxOmFjY190Y2dh</td>
          <td>VENHQS1PUi1BNUoxOmFjY190Y2dh</td>
          <td>675</td>
          <td>acc_tcga_rna_seq_v2_mrna</td>
          <td>TCGA-OR-A5J1-01</td>
          <td>TCGA-OR-A5J1</td>
          <td>acc_tcga</td>
          <td>15.850100</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2 = md.get_all_molecular_data_in_molecular_profile(molecular_profile_id="brca_tcga_rppa", 
                                                         sample_list_id="brca_tcga_all", 
                                                         entrez_gene_id="675")
    df2




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
          <th>entrezGeneId</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS0zQy1BQUxJLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS0zQy1BQUxJOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-3C-AALI-01</td>
          <td>TCGA-3C-AALI</td>
          <td>brca_tcga</td>
          <td>-0.181730</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS0zQy1BQUxLLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS0zQy1BQUxLOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-3C-AALK-01</td>
          <td>TCGA-3C-AALK</td>
          <td>brca_tcga</td>
          <td>-0.366790</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS00SC1BQUFLLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS00SC1BQUFLOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-4H-AAAK-01</td>
          <td>TCGA-4H-AAAK</td>
          <td>brca_tcga</td>
          <td>-0.108050</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS01TC1BQVQxLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS01TC1BQVQxOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-5L-AAT1-01</td>
          <td>TCGA-5L-AAT1</td>
          <td>brca_tcga</td>
          <td>-0.785290</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS01VC1BOVFBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-5T-A9QA-01</td>
          <td>TCGA-5T-A9QA</td>
          <td>brca_tcga</td>
          <td>-0.469280</td>
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
          <th>887</th>
          <td>VENHQS1XOC1BODZHLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1XOC1BODZHOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-W8-A86G-01</td>
          <td>TCGA-W8-A86G</td>
          <td>brca_tcga</td>
          <td>-0.083261</td>
        </tr>
        <tr>
          <th>888</th>
          <td>VENHQS1XVC1BQjQxLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1XVC1BQjQxOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-WT-AB41-01</td>
          <td>TCGA-WT-AB41</td>
          <td>brca_tcga</td>
          <td>-0.386950</td>
        </tr>
        <tr>
          <th>889</th>
          <td>VENHQS1YWC1BODk5LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1YWC1BODk5OmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-XX-A899-01</td>
          <td>TCGA-XX-A899</td>
          <td>brca_tcga</td>
          <td>-0.472410</td>
        </tr>
        <tr>
          <th>890</th>
          <td>VENHQS1aNy1BOFI1LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1aNy1BOFI1OmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-Z7-A8R5-01</td>
          <td>TCGA-Z7-A8R5</td>
          <td>brca_tcga</td>
          <td>-0.458130</td>
        </tr>
        <tr>
          <th>891</th>
          <td>VENHQS1aNy1BOFI2LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1aNy1BOFI2OmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-Z7-A8R6-01</td>
          <td>TCGA-Z7-A8R6</td>
          <td>brca_tcga</td>
          <td>-0.382420</td>
        </tr>
      </tbody>
    </table>
    <p>892 rows × 8 columns</p>
    </div>



.. code:: ipython3

    df3 = md.fetch_all_molecular_data_in_molecular_profile(molecular_profile_id = "brca_tcga_rppa",
                                                           entrez_gene_ids = ["672","675"],
                                                           sample_ids = ["TCGA-AR-A1AR-01","TCGA-BH-A1EO-01"])
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
          <th>entrezGeneId</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>675</td>
          <td>brca_tcga_rppa</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>brca_tcga</td>
          <td>-0.40763</td>
        </tr>
      </tbody>
    </table>
    </div>


