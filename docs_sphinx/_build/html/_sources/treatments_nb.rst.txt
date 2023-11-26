.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pybioportal import treatments as trt

Get the Study IDs of all studies

.. code:: ipython3

    from pybioportal import studies as std
    studies = std.get_all_studies(projection="DETAILED")
    std_ids = studies["studyId"].to_list()
    print(f"First Study IDs of {len(std_ids)}: {std_ids[0:5]}")


.. parsed-literal::

    First Study IDs of 393: ['acc_tcga', 'laml_tcga', 'blca_tcga', 'kirc_tcga', 'cesc_tcga']
    

.. code:: ipython3

    trt.fetch_status_display_patient_trts(study_ids=std_ids)




.. parsed-literal::

    True



.. code:: ipython3

    trt.fetch_status_display_sample_trts(study_ids=std_ids)




.. parsed-literal::

    True



.. code:: ipython3

    filter1a = {"studyIds": std_ids}
    df1a = trt.fetch_all_patient_level_treatments(study_view_filter=filter1a)
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
          <th>treatment</th>
          <th>count</th>
          <th>patientId</th>
          <th>sampleId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>CCNU + thalidomide</td>
          <td>1</td>
          <td>P01</td>
          <td>P01_Pri</td>
          <td>lgg_ucsf_2014</td>
        </tr>
        <tr>
          <th>1</th>
          <td>CCNU + thalidomide</td>
          <td>1</td>
          <td>P01</td>
          <td>P01_Rec</td>
          <td>lgg_ucsf_2014</td>
        </tr>
        <tr>
          <th>2</th>
          <td>MK-3475</td>
          <td>2</td>
          <td>P-19</td>
          <td>121441-2T-19</td>
          <td>mel_tsam_liang_2017</td>
        </tr>
        <tr>
          <th>3</th>
          <td>MK-3475</td>
          <td>2</td>
          <td>P-17</td>
          <td>101984-1T-17</td>
          <td>mel_tsam_liang_2017</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Doxorubicin HCL</td>
          <td>1</td>
          <td>HTA9_1</td>
          <td>HTA9_1-Bx3</td>
          <td>brca_hta9_htan_2022</td>
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
          <th>21974</th>
          <td>Megestrol Acetate</td>
          <td>17</td>
          <td>TCGA-B5-A11I</td>
          <td>TCGA-B5-A11I-01</td>
          <td>ucec_tcga_pan_can_atlas_2018</td>
        </tr>
        <tr>
          <th>21975</th>
          <td>Megestrol Acetate</td>
          <td>17</td>
          <td>TCGA-AP-A0LL</td>
          <td>TCGA-AP-A0LL-01</td>
          <td>ucec_tcga_pan_can_atlas_2018</td>
        </tr>
        <tr>
          <th>21976</th>
          <td>Megestrol Acetate</td>
          <td>17</td>
          <td>TCGA-B5-A11Q</td>
          <td>TCGA-B5-A11Q-01</td>
          <td>ucec_tcga_pan_can_atlas_2018</td>
        </tr>
        <tr>
          <th>21977</th>
          <td>Plfe</td>
          <td>1</td>
          <td>TCGA-D7-8570</td>
          <td>TCGA-D7-8570-01</td>
          <td>stad_tcga_pan_can_atlas_2018</td>
        </tr>
        <tr>
          <th>21978</th>
          <td>Ondansetron</td>
          <td>1</td>
          <td>TCGA-EB-A57M</td>
          <td>TCGA-EB-A57M-01</td>
          <td>skcm_tcga_pan_can_atlas_2018</td>
        </tr>
      </tbody>
    </table>
    <p>21979 rows × 5 columns</p>
    </div>



.. code:: ipython3

    filter1b = {"patientTreatmentFilters": {
        "filters": [
          {
            "filters": [
              {
                "treatment": "Palbociclib"
              }
            ]
          }
        ]
      },
      "studyIds": std_ids}
    
    df1b = trt.fetch_all_patient_level_treatments(study_view_filter=filter1b)
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
          <th>treatment</th>
          <th>count</th>
          <th>patientId</th>
          <th>sampleId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Doxorubicin HCL</td>
          <td>1</td>
          <td>HTA9_1</td>
          <td>HTA9_1-Bx3</td>
          <td>brca_hta9_htan_2022</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Doxorubicin HCL</td>
          <td>1</td>
          <td>HTA9_1</td>
          <td>HTA9_1-Bx4</td>
          <td>brca_hta9_htan_2022</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Doxorubicin HCL</td>
          <td>1</td>
          <td>HTA9_1</td>
          <td>HTA9_1-Bx1</td>
          <td>brca_hta9_htan_2022</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Doxorubicin HCL</td>
          <td>1</td>
          <td>HTA9_1</td>
          <td>HTA9_1-Bx2</td>
          <td>brca_hta9_htan_2022</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Doxorubicin HCL</td>
          <td>1</td>
          <td>HTA9_1</td>
          <td>HTA9_1-PR</td>
          <td>brca_hta9_htan_2022</td>
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
          <th>116</th>
          <td>Letrozole</td>
          <td>6</td>
          <td>37916</td>
          <td>37916</td>
          <td>pog570_bcgsc_2020</td>
        </tr>
        <tr>
          <th>117</th>
          <td>Letrozole</td>
          <td>6</td>
          <td>38725</td>
          <td>38725</td>
          <td>pog570_bcgsc_2020</td>
        </tr>
        <tr>
          <th>118</th>
          <td>Letrozole</td>
          <td>6</td>
          <td>37844</td>
          <td>37844</td>
          <td>pog570_bcgsc_2020</td>
        </tr>
        <tr>
          <th>119</th>
          <td>Letrozole</td>
          <td>6</td>
          <td>36621</td>
          <td>36621</td>
          <td>pog570_bcgsc_2020</td>
        </tr>
        <tr>
          <th>120</th>
          <td>Letrozole</td>
          <td>6</td>
          <td>31509</td>
          <td>31509</td>
          <td>pog570_bcgsc_2020</td>
        </tr>
      </tbody>
    </table>
    <p>121 rows × 5 columns</p>
    </div>



.. code:: ipython3

    filter2b = {"sampleTreatmentFilters": {
        "filters": [
          {
            "filters": [
              {
                "time": "Pre",
                "treatment": "Palbociclib"
              },
              {
                "time": "Post",
                "treatment": "Palbociclib"
              }
            ]
          }
        ]
      },
      "studyIds": ["brca_tcga"]}
    
    df2b = trt.fetch_all_sample_level_treatments(study_view_filter=filter2b)
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
          <th>time</th>
          <th>treatment</th>
          <th>count</th>
          <th>patientId</th>
          <th>sampleId</th>
          <th>studyId</th>
          <th>timeTaken</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Post</td>
          <td>DOXORUBICIN</td>
          <td>1</td>
          <td>TCGA-60-2697</td>
          <td>TCGA-60-2697-01</td>
          <td>lusc_tcga_pan_can_atlas_2018</td>
          <td>93</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Pre</td>
          <td>pemetrexed+bevacizumab+erlotinib</td>
          <td>2</td>
          <td>MSK_LX25</td>
          <td>P-0000636-T01-IM3</td>
          <td>lung_msk_pdx</td>
          <td>203</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Pre</td>
          <td>pemetrexed+bevacizumab+erlotinib</td>
          <td>2</td>
          <td>MSK_LX25</td>
          <td>MSK_LX25</td>
          <td>lung_msk_pdx</td>
          <td>203</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Pre</td>
          <td>BICALUTAMIDE</td>
          <td>9</td>
          <td>MPCPROJECT_0319</td>
          <td>RP-1532_PCProject_0319_T1_v2_Exome_OnPrem</td>
          <td>mpcproject_broad_2021</td>
          <td>0</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Pre</td>
          <td>BICALUTAMIDE</td>
          <td>9</td>
          <td>MPCPROJECT_0130</td>
          <td>RP-1532_PCProject_0130_T1_v3_Exome_OnPrem</td>
          <td>mpcproject_broad_2021</td>
          <td>0</td>
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
          <th>12784</th>
          <td>Pre</td>
          <td>Vemurafenib</td>
          <td>11</td>
          <td>TCGA-GN-A4U7</td>
          <td>TCGA-GN-A4U7-06</td>
          <td>skcm_tcga_pan_can_atlas_2018</td>
          <td>163</td>
        </tr>
        <tr>
          <th>12785</th>
          <td>Pre</td>
          <td>TARCEVA/ERLOTINIB</td>
          <td>1</td>
          <td>TCGA-18-3412</td>
          <td>TCGA-18-3412-01</td>
          <td>lusc_tcga_pan_can_atlas_2018</td>
          <td>0</td>
        </tr>
        <tr>
          <th>12786</th>
          <td>Pre</td>
          <td>CPT-11</td>
          <td>1</td>
          <td>TCGA-38-4632</td>
          <td>TCGA-38-4632-01</td>
          <td>luad_tcga_pan_can_atlas_2018</td>
          <td>0</td>
        </tr>
        <tr>
          <th>12787</th>
          <td>Pre</td>
          <td>ZOLEDRONIC ACID</td>
          <td>1</td>
          <td>MPCPROJECT_0031</td>
          <td>RP-1532_PCProject_0031_T1_v2_Exome_OnPrem</td>
          <td>mpcproject_broad_2021</td>
          <td>0</td>
        </tr>
        <tr>
          <th>12788</th>
          <td>Post</td>
          <td>carboplatin+pemetrexed (maintenance) +bevacizumab</td>
          <td>1</td>
          <td>MSK_LX301</td>
          <td>MSK_LX301B</td>
          <td>lung_msk_pdx</td>
          <td>1786</td>
        </tr>
      </tbody>
    </table>
    <p>12789 rows × 7 columns</p>
    </div>


