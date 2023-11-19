.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioPortal import gene_panels as gp

.. code:: ipython3

    df1 = gp.get_all_gene_panels()
    df1.head(10)




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
          <th>description</th>
          <th>genePanelId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Targeted (27 cancer genes) sequencing of adeno...</td>
          <td>ACYC_FMI_27</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Targeted panel of 232 genes.</td>
          <td>Agilent</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Targeted panel of 8 genes.</td>
          <td>AmpliSeq</td>
        </tr>
        <tr>
          <th>3</th>
          <td>ARCHER-HEME gene panel (199 genes)</td>
          <td>ARCHER-HEME-CV1</td>
        </tr>
        <tr>
          <th>4</th>
          <td>ARCHER-SOLID Gene Panel (62 genes)</td>
          <td>ARCHER-SOLID-CV1</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Targeted sequencing of various tumor types via...</td>
          <td>bait_v3</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Targeted sequencing of various tumor types via...</td>
          <td>bait_v4</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Targeted sequencing of various tumor types via...</td>
          <td>bait_v5</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Targeted panel of 387 cancer-related genes.</td>
          <td>bcc_unige_2016_cancer_panel</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Research (CMO) IMPACT-Heme gene panel version 3.</td>
          <td>HemePACT_v3</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2 = gp.get_gene_panel("NSCLC_UNITO_2016_PANEL")
    df2.head(10)




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
          <th>description</th>
          <th>genePanelId</th>
          <th>entrezGeneId</th>
          <th>hugoGeneSymbol</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>25</td>
          <td>ABL1</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>207</td>
          <td>AKT1</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>324</td>
          <td>APC</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>472</td>
          <td>ATM</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>673</td>
          <td>BRAF</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>999</td>
          <td>CDH1</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>1029</td>
          <td>CDKN2A</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>1956</td>
          <td>EGFR</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>2064</td>
          <td>ERBB2</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>2066</td>
          <td>ERBB4</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df3 = gp.fetch_gene_panels(gene_panel_ids=["NSCLC_UNITO_2016_PANEL", "bcc_unige_2016_cancer_panel"], 
                               projection="DETAILED")
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
          <th>description</th>
          <th>genePanelId</th>
          <th>entrezGeneId</th>
          <th>hugoGeneSymbol</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Targeted panel of 387 cancer-related genes.</td>
          <td>bcc_unige_2016_cancer_panel</td>
          <td>25</td>
          <td>ABL1</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Targeted panel of 387 cancer-related genes.</td>
          <td>bcc_unige_2016_cancer_panel</td>
          <td>56</td>
          <td>ACRV1</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Targeted panel of 387 cancer-related genes.</td>
          <td>bcc_unige_2016_cancer_panel</td>
          <td>2181</td>
          <td>ACSL3</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Targeted panel of 387 cancer-related genes.</td>
          <td>bcc_unige_2016_cancer_panel</td>
          <td>91</td>
          <td>ACVR1B</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Targeted panel of 387 cancer-related genes.</td>
          <td>bcc_unige_2016_cancer_panel</td>
          <td>92</td>
          <td>ACVR2A</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>409</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>4089</td>
          <td>SMAD4</td>
        </tr>
        <tr>
          <th>410</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>6608</td>
          <td>SMO</td>
        </tr>
        <tr>
          <th>411</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>6794</td>
          <td>STK11</td>
        </tr>
        <tr>
          <th>412</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>7157</td>
          <td>TP53</td>
        </tr>
        <tr>
          <th>413</th>
          <td>Targeted NGS of NSCLC Samples.</td>
          <td>NSCLC_UNITO_2016_PANEL</td>
          <td>7428</td>
          <td>VHL</td>
        </tr>
      </tbody>
    </table>
    <p>414 rows × 4 columns</p>
    </div>


