.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioGate import sample_lists as sl

.. code:: ipython3

    df1 = sl.get_all_sample_lists(projection="DETAILED")
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
          <th>category</th>
          <th>name</th>
          <th>description</th>
          <th>sampleCount</th>
          <th>sampleIds</th>
          <th>sampleListId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>all_cases_with_mrna_rnaseq_data</td>
          <td>Samples with mRNA data (RNA Seq V2)</td>
          <td>Samples with mRNA expression data (79 samples)</td>
          <td>79</td>
          <td>[TCGA-OR-A5J1-01, TCGA-OR-A5J2-01, TCGA-OR-A5J...</td>
          <td>acc_tcga_rna_seq_v2_mrna</td>
          <td>acc_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>all_cases_in_study</td>
          <td>All samples</td>
          <td>All samples (92 samples)</td>
          <td>92</td>
          <td>[TCGA-OR-A5J1-01, TCGA-OR-A5J2-01, TCGA-OR-A5J...</td>
          <td>acc_tcga_all</td>
          <td>acc_tcga</td>
        </tr>
        <tr>
          <th>2</th>
          <td>all_cases_with_cna_data</td>
          <td>Samples with CNA data</td>
          <td>Samples with CNA data (90 samples)</td>
          <td>90</td>
          <td>[TCGA-OR-A5J1-01, TCGA-OR-A5J2-01, TCGA-OR-A5J...</td>
          <td>acc_tcga_cna</td>
          <td>acc_tcga</td>
        </tr>
        <tr>
          <th>3</th>
          <td>all_cases_with_mutation_and_cna_data</td>
          <td>Samples with mutation and CNA data</td>
          <td>Samples with mutation and CNA data (88 samples)</td>
          <td>88</td>
          <td>[TCGA-OR-A5J1-01, TCGA-OR-A5J2-01, TCGA-OR-A5J...</td>
          <td>acc_tcga_cnaseq</td>
          <td>acc_tcga</td>
        </tr>
        <tr>
          <th>4</th>
          <td>all_cases_with_mutation_and_cna_and_mrna_data</td>
          <td>Complete samples</td>
          <td>Samples with mutation, CNA and expression data...</td>
          <td>75</td>
          <td>[TCGA-OR-A5J1-01, TCGA-OR-A5J2-01, TCGA-OR-A5J...</td>
          <td>acc_tcga_3way_complete</td>
          <td>acc_tcga</td>
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
          <th>2225</th>
          <td>all_cases_with_mutation_and_cna_data</td>
          <td>Samples with mutation and CNA data</td>
          <td>Samples with mutation and CNA data (322 samples)</td>
          <td>322</td>
          <td>[P-0000463-T01-IM3, P-0000583-T01-IM3, P-00006...</td>
          <td>bm_nsclc_mskcc_2023_cnaseq</td>
          <td>bm_nsclc_mskcc_2023</td>
        </tr>
        <tr>
          <th>2226</th>
          <td>all_cases_with_mutation_data</td>
          <td>Samples with mutation data</td>
          <td>Samples with mutation data (322 samples)</td>
          <td>322</td>
          <td>[P-0000463-T01-IM3, P-0000583-T01-IM3, P-00006...</td>
          <td>bm_nsclc_mskcc_2023_sequenced</td>
          <td>bm_nsclc_mskcc_2023</td>
        </tr>
        <tr>
          <th>2227</th>
          <td>all_cases_with_sv_data</td>
          <td>Samples with SV data</td>
          <td>Samples with SV data</td>
          <td>322</td>
          <td>[P-0000463-T01-IM3, P-0000583-T01-IM3, P-00006...</td>
          <td>bm_nsclc_mskcc_2023_sv</td>
          <td>bm_nsclc_mskcc_2023</td>
        </tr>
        <tr>
          <th>2228</th>
          <td>all_cases_in_study</td>
          <td>All samples</td>
          <td>All samples (19 samples)</td>
          <td>19</td>
          <td>[2-001_Plexiform_Neurofibroma, 2-004_Plexiform...</td>
          <td>nst_nfosi_ntap_all</td>
          <td>nst_nfosi_ntap</td>
        </tr>
        <tr>
          <th>2229</th>
          <td>all_cases_with_mutation_data</td>
          <td>Samples with mutation data</td>
          <td>Samples with mutation data (19 samples)</td>
          <td>19</td>
          <td>[2-001_Plexiform_Neurofibroma, 2-004_Plexiform...</td>
          <td>nst_nfosi_ntap_sequenced</td>
          <td>nst_nfosi_ntap</td>
        </tr>
      </tbody>
    </table>
    <p>2230 rows × 7 columns</p>
    </div>



.. code:: ipython3

    df2 = sl.get_sample_list(sample_list_id="brca_tcga_cna")
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
          <th>category</th>
          <th>name</th>
          <th>description</th>
          <th>sampleCount</th>
          <th>sampleIds</th>
          <th>sampleListId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>all_cases_with_cna_data</td>
          <td>Samples with CNA data</td>
          <td>Samples with CNA data (1080 samples)</td>
          <td>1080</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_cna</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df3 = sl.get_all_sample_ids_in_sample_list(sample_list_id="brca_tcga_cna")
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
          <th>0</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>TCGA-AR-A1AR-01</td>
        </tr>
        <tr>
          <th>1</th>
          <td>TCGA-BH-A1EO-01</td>
        </tr>
        <tr>
          <th>2</th>
          <td>TCGA-BH-A1ES-01</td>
        </tr>
        <tr>
          <th>3</th>
          <td>TCGA-BH-A1ET-01</td>
        </tr>
        <tr>
          <th>4</th>
          <td>TCGA-BH-A1EU-01</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
        </tr>
        <tr>
          <th>1075</th>
          <td>TCGA-E2-A1B4-01</td>
        </tr>
        <tr>
          <th>1076</th>
          <td>TCGA-E2-A1B5-01</td>
        </tr>
        <tr>
          <th>1077</th>
          <td>TCGA-E2-A1B6-01</td>
        </tr>
        <tr>
          <th>1078</th>
          <td>TCGA-E2-A1BC-01</td>
        </tr>
        <tr>
          <th>1079</th>
          <td>TCGA-E2-A1BD-01</td>
        </tr>
      </tbody>
    </table>
    <p>1080 rows × 1 columns</p>
    </div>



.. code:: ipython3

    df4 = sl.fetch_sample_lists(sample_list_ids=["brca_tcga_cna", "brca_tcga_mrna"], projection="DETAILED")
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
          <th>category</th>
          <th>name</th>
          <th>description</th>
          <th>sampleCount</th>
          <th>sampleIds</th>
          <th>sampleListId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>all_cases_with_cna_data</td>
          <td>Samples with CNA data</td>
          <td>Samples with CNA data (1080 samples)</td>
          <td>1080</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_cna</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>all_cases_with_mrna_array_data</td>
          <td>Samples with mRNA data (Agilent microarray)</td>
          <td>Samples with mRNA expression data (529 samples)</td>
          <td>529</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_mrna</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df5 = sl.get_all_sample_lists_in_study(study_id="brca_tcga",projection="DETAILED")
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
          <th>category</th>
          <th>name</th>
          <th>description</th>
          <th>sampleCount</th>
          <th>sampleIds</th>
          <th>sampleListId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>all_cases_with_mrna_rnaseq_data</td>
          <td>Samples with mRNA data (RNA Seq V2)</td>
          <td>Samples with mRNA expression data (1100 samples)</td>
          <td>1100</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_rna_seq_v2_mrna</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>all_cases_in_study</td>
          <td>All samples</td>
          <td>All samples (1108 samples)</td>
          <td>1108</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_all</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>2</th>
          <td>all_cases_with_cna_data</td>
          <td>Samples with CNA data</td>
          <td>Samples with CNA data (1080 samples)</td>
          <td>1080</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_cna</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>3</th>
          <td>all_cases_with_mutation_and_cna_data</td>
          <td>Samples with mutation and CNA data</td>
          <td>Samples with mutation and CNA data (963 samples)</td>
          <td>963</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_cnaseq</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>4</th>
          <td>all_cases_with_mutation_and_cna_and_mrna_data</td>
          <td>Complete samples</td>
          <td>Samples with mutation, CNA and expression data...</td>
          <td>960</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_3way_complete</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>5</th>
          <td>all_cases_with_mrna_array_data</td>
          <td>Samples with mRNA data (Agilent microarray)</td>
          <td>Samples with mRNA expression data (529 samples)</td>
          <td>529</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_mrna</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>6</th>
          <td>all_cases_with_methylation_data</td>
          <td>Samples with methylation data</td>
          <td>Samples with methylation data (788 samples)</td>
          <td>788</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_methylation_all</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>7</th>
          <td>all_cases_with_methylation_data</td>
          <td>Samples with methylation data (HM27)</td>
          <td>Samples with methylation data (HM27) (343 samp...</td>
          <td>316</td>
          <td>[TCGA-A2-A0CX-01, TCGA-A2-A0D0-01, TCGA-A2-A0D...</td>
          <td>brca_tcga_methylation_hm27</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>8</th>
          <td>all_cases_with_methylation_data</td>
          <td>Samples with methylation data (HM450)</td>
          <td>Samples with methylation data (HM450) (885 sam...</td>
          <td>788</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_methylation_hm450</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>9</th>
          <td>other</td>
          <td>Samples with phosphoprotein quantification dat...</td>
          <td>Tumor samples with phosphoprotein quantificati...</td>
          <td>74</td>
          <td>[TCGA-A7-A0CE-01, TCGA-A7-A0CJ-01, TCGA-A8-A06...</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>10</th>
          <td>other</td>
          <td>Samples with protein data (Mass Spec)</td>
          <td>Samples with protein data (Mass Spec) (74 samp...</td>
          <td>74</td>
          <td>[TCGA-A7-A0CE-01, TCGA-A7-A0CJ-01, TCGA-A8-A06...</td>
          <td>brca_tcga_protein_quantification</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>11</th>
          <td>all_cases_with_rppa_data</td>
          <td>Samples with protein data (RPPA)</td>
          <td>Samples protein data (RPPA) (892 samples)</td>
          <td>892</td>
          <td>[TCGA-BH-A1EO-01, TCGA-BH-A1ES-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_rppa</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>12</th>
          <td>all_cases_with_mutation_data</td>
          <td>Samples with mutation data</td>
          <td>Samples with mutation data (982 samples)</td>
          <td>982</td>
          <td>[TCGA-AR-A1AR-01, TCGA-BH-A1EO-01, TCGA-BH-A1E...</td>
          <td>brca_tcga_sequenced</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    </div>


