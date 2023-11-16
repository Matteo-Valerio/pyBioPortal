.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioGate import generic_assays as ga

.. code:: ipython3

    df1a = ga.fetch_generic_assay_meta(generic_assay_stable_ids=["TULP4_pS563", "TEP1_pS397", "ALAD_214_215_1_1_S215"])
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
          <th>stableId</th>
          <th>entityType</th>
          <th>genericEntityMetaProperties_GENE_SYMBOL</th>
          <th>genericEntityMetaProperties_PHOSPHOSITE</th>
          <th>genericEntityMetaProperties_DESCRIPTION</th>
          <th>genericEntityMetaProperties_NAME</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>TEP1_pS397</td>
          <td>GENERIC_ASSAY</td>
          <td>TEP1</td>
          <td>pS397</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>TULP4_pS563</td>
          <td>GENERIC_ASSAY</td>
          <td>TULP4</td>
          <td>pS563</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>2</th>
          <td>ALAD_214_215_1_1_S215</td>
          <td>GENERIC_ASSAY</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NP_000022.3</td>
          <td>ALAD S215 214-215 1_1</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df1b = ga.fetch_generic_assay_meta(molecular_profile_ids=["brca_tcga_phosphoprotein_quantification",
                                                              "brain_cptac_2020_phosphoprotein"])
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
          <th>stableId</th>
          <th>entityType</th>
          <th>genericEntityMetaProperties_GENE_SYMBOL</th>
          <th>genericEntityMetaProperties_PHOSPHOSITE</th>
          <th>genericEntityMetaProperties_DESCRIPTION</th>
          <th>genericEntityMetaProperties_NAME</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>FSCN1_pS328</td>
          <td>GENERIC_ASSAY</td>
          <td>FSCN1</td>
          <td>pS328</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>YWHAZ_pS230</td>
          <td>GENERIC_ASSAY</td>
          <td>YWHAZ</td>
          <td>pS230</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>2</th>
          <td>GMPPB_pS246</td>
          <td>GENERIC_ASSAY</td>
          <td>GMPPB</td>
          <td>pS246</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>3</th>
          <td>EPN3_pS503</td>
          <td>GENERIC_ASSAY</td>
          <td>EPN3</td>
          <td>pS503</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td>C19orf47_pS395</td>
          <td>GENERIC_ASSAY</td>
          <td>C19orf47</td>
          <td>pS395</td>
          <td>NaN</td>
          <td>NaN</td>
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
          <th>76663</th>
          <td>DIS3L2_133_154_1_1_S139</td>
          <td>GENERIC_ASSAY</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NP_689596.4</td>
          <td>DIS3L2 S139 133-154 1_1</td>
        </tr>
        <tr>
          <th>76664</th>
          <td>CRYBG3_442_457_1_1_S457</td>
          <td>GENERIC_ASSAY</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NP_705833.3</td>
          <td>CRYBG3 S457 442-457 1_1</td>
        </tr>
        <tr>
          <th>76665</th>
          <td>RASAL2_1005_1006_1_1_S1005</td>
          <td>GENERIC_ASSAY</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NP_733793.2</td>
          <td>RASAL2 S1005 1005-1006 1_1</td>
        </tr>
        <tr>
          <th>76666</th>
          <td>CAMK2B_338_343_1_1_T342</td>
          <td>GENERIC_ASSAY</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NP_742078.1</td>
          <td>CAMK2B T342 338-343 1_1</td>
        </tr>
        <tr>
          <th>76667</th>
          <td>EXOC1_453_458_1_1_S455</td>
          <td>GENERIC_ASSAY</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NP_839955.1</td>
          <td>EXOC1 S455 453-458 1_1</td>
        </tr>
      </tbody>
    </table>
    <p>76668 rows × 6 columns</p>
    </div>



.. code:: ipython3

    df2 = ga.get_generic_assay_meta_by_molecular_profile_id("brca_tcga_phosphoprotein_quantification")
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
          <th>stableId</th>
          <th>entityType</th>
          <th>genericEntityMetaProperties_GENE_SYMBOL</th>
          <th>genericEntityMetaProperties_PHOSPHOSITE</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>FSCN1_pS328</td>
          <td>GENERIC_ASSAY</td>
          <td>FSCN1</td>
          <td>pS328</td>
        </tr>
        <tr>
          <th>1</th>
          <td>YWHAZ_pS230</td>
          <td>GENERIC_ASSAY</td>
          <td>YWHAZ</td>
          <td>pS230</td>
        </tr>
        <tr>
          <th>2</th>
          <td>GMPPB_pS246</td>
          <td>GENERIC_ASSAY</td>
          <td>GMPPB</td>
          <td>pS246</td>
        </tr>
        <tr>
          <th>3</th>
          <td>EPN3_pS503</td>
          <td>GENERIC_ASSAY</td>
          <td>EPN3</td>
          <td>pS503</td>
        </tr>
        <tr>
          <th>4</th>
          <td>C19orf47_pS395</td>
          <td>GENERIC_ASSAY</td>
          <td>C19orf47</td>
          <td>pS395</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>72115</th>
          <td>CIC_pS902_S904</td>
          <td>GENERIC_ASSAY</td>
          <td>CIC</td>
          <td>pS902_S904</td>
        </tr>
        <tr>
          <th>72116</th>
          <td>MAGI1_pT1336</td>
          <td>GENERIC_ASSAY</td>
          <td>MAGI1</td>
          <td>pT1336</td>
        </tr>
        <tr>
          <th>72117</th>
          <td>PRKD2_pT211_S214</td>
          <td>GENERIC_ASSAY</td>
          <td>PRKD2</td>
          <td>pT211_S214</td>
        </tr>
        <tr>
          <th>72118</th>
          <td>PDCD11_pT1012</td>
          <td>GENERIC_ASSAY</td>
          <td>PDCD11</td>
          <td>pT1012</td>
        </tr>
        <tr>
          <th>72119</th>
          <td>PKN2_pT958</td>
          <td>GENERIC_ASSAY</td>
          <td>PKN2</td>
          <td>pT958</td>
        </tr>
      </tbody>
    </table>
    <p>72120 rows × 4 columns</p>
    </div>



.. code:: ipython3

    df3 = ga.get_generic_assay_meta_by_id("TULP4_pS563")
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
          <th>stableId</th>
          <th>entityType</th>
          <th>genericEntityMetaProperties_GENE_SYMBOL</th>
          <th>genericEntityMetaProperties_PHOSPHOSITE</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>TULP4_pS563</td>
          <td>GENERIC_ASSAY</td>
          <td>TULP4</td>
          <td>pS563</td>
        </tr>
      </tbody>
    </table>
    </div>


