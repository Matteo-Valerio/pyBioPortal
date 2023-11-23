.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pybioportal import generic_assay_data as gad

.. code:: ipython3

    df1a = gad.fetch_generic_assay_data_in_molecular_profile(molecular_profile_id="brca_tcga_phosphoprotein_quantification", 
                                                             generic_assay_stable_ids = ["TULP4_pS563", "TEP1_pS397"],
                                                             sample_ids = ["TCGA-C8-A130-01", "TCGA-C8-A134-01"])
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
          <th>value</th>
          <th>genericAssayStableId</th>
          <th>stableId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1DOC1BMTMwLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTMwOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A130-01</td>
          <td>TCGA-C8-A130</td>
          <td>brca_tcga</td>
          <td>0.31374650000644216</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1DOC1BMTMwLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTMwOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A130-01</td>
          <td>TCGA-C8-A130</td>
          <td>brca_tcga</td>
          <td>1.8338606392734915</td>
          <td>TULP4_pS563</td>
          <td>TULP4_pS563</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>0.13629911078391418</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>-0.2314224260050513</td>
          <td>TULP4_pS563</td>
          <td>TULP4_pS563</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df1b = gad.fetch_generic_assay_data_in_molecular_profile(molecular_profile_id="brca_tcga_phosphoprotein_quantification", 
                                                             generic_assay_stable_ids = ["TULP4_pS563", "TEP1_pS397"],
                                                             sample_list_id = "brca_tcga_all")
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
          <th>value</th>
          <th>genericAssayStableId</th>
          <th>stableId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BMi1BMENNLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMENNOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-A2-A0CM-01</td>
          <td>TCGA-A2-A0CM</td>
          <td>brca_tcga</td>
          <td>0.3990168921075522</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BMi1BMEQyLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMEQyOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-A2-A0D2-01</td>
          <td>TCGA-A2-A0D2</td>
          <td>brca_tcga</td>
          <td>-0.6936246814411646</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1BMi1BMEVRLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMEVROmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-A2-A0EQ-01</td>
          <td>TCGA-A2-A0EQ</td>
          <td>brca_tcga</td>
          <td>0.3121367021962257</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1BMi1BMEVWLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMEVWOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-A2-A0EV-01</td>
          <td>TCGA-A2-A0EV</td>
          <td>brca_tcga</td>
          <td>-1.14562097925631</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1BMi1BMEVYLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMEVYOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-A2-A0EX-01</td>
          <td>TCGA-A2-A0EX</td>
          <td>brca_tcga</td>
          <td>0.20418754958872287</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
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
        </tr>
        <tr>
          <th>65</th>
          <td>VENHQS1DOC1BMTM4LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM4OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A138-01</td>
          <td>TCGA-C8-A138</td>
          <td>brca_tcga</td>
          <td>0.6359899875778352</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>66</th>
          <td>VENHQS1EOC1BMTQyLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1EOC1BMTQyOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-D8-A142-01</td>
          <td>TCGA-D8-A142</td>
          <td>brca_tcga</td>
          <td>-0.578947377398709</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>67</th>
          <td>VENHQS1FMi1BMTU0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTU0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-E2-A154-01</td>
          <td>TCGA-E2-A154</td>
          <td>brca_tcga</td>
          <td>-0.3888088589350173</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>68</th>
          <td>VENHQS1FMi1BMTU4LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTU4OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-E2-A158-01</td>
          <td>TCGA-E2-A158</td>
          <td>brca_tcga</td>
          <td>-0.3037812098567177</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>69</th>
          <td>VENHQS1FMi1BMTVBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMTVBOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-E2-A15A-01</td>
          <td>TCGA-E2-A15A</td>
          <td>brca_tcga</td>
          <td>-0.25129006810968774</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
      </tbody>
    </table>
    <p>70 rows × 9 columns</p>
    </div>



.. code:: ipython3

    df2a = gad.fetch_generic_assay_data(generic_assay_stable_ids=["TULP4_pS563", "TEP1_pS397", "ALAD_214_215_1_1_S215"],
                                        molecular_profile_ids=["brca_tcga_phosphoprotein_quantification","brain_cptac_2020_phosphoprotein"])
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
          <th>value</th>
          <th>genericAssayStableId</th>
          <th>stableId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>NzMxNi0xNzgxOmJyYWluX2NwdGFjXzIwMjA</td>
          <td>UFRfTTFSWU43QjA6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-1781</td>
          <td>PT_M1RYN7B0</td>
          <td>brain_cptac_2020</td>
          <td>-0.696372026845622</td>
          <td>ALAD_214_215_1_1_S215</td>
          <td>ALAD_214_215_1_1_S215</td>
        </tr>
        <tr>
          <th>1</th>
          <td>NzMxNi0xNzkwOmJyYWluX2NwdGFjXzIwMjA</td>
          <td>UFRfRVNIQUNXRjY6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-1790</td>
          <td>PT_ESHACWF6</td>
          <td>brain_cptac_2020</td>
          <td>-0.890851197690543</td>
          <td>ALAD_214_215_1_1_S215</td>
          <td>ALAD_214_215_1_1_S215</td>
        </tr>
        <tr>
          <th>2</th>
          <td>NzMxNi04Nzg6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>UFRfRVNIQUNXRjY6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-878</td>
          <td>PT_ESHACWF6</td>
          <td>brain_cptac_2020</td>
          <td>-1.11503373579888</td>
          <td>ALAD_214_215_1_1_S215</td>
          <td>ALAD_214_215_1_1_S215</td>
        </tr>
        <tr>
          <th>3</th>
          <td>NzMxNi0yMTgxOmJyYWluX2NwdGFjXzIwMjA</td>
          <td>UFRfR0g2OTNUVDg6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-2181</td>
          <td>PT_GH693TT8</td>
          <td>brain_cptac_2020</td>
          <td>-0.819816432243918</td>
          <td>ALAD_214_215_1_1_S215</td>
          <td>ALAD_214_215_1_1_S215</td>
        </tr>
        <tr>
          <th>4</th>
          <td>NzMxNi0yMTQxOmJyYWluX2NwdGFjXzIwMjA</td>
          <td>UFRfV0cyWjk1QjU6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-2141</td>
          <td>PT_WG2Z95B5</td>
          <td>brain_cptac_2020</td>
          <td>-1.10382655624193</td>
          <td>ALAD_214_215_1_1_S215</td>
          <td>ALAD_214_215_1_1_S215</td>
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
        </tr>
        <tr>
          <th>282</th>
          <td>VENHQS1BUi1BMUFTLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFTOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-AR-A1AS-01</td>
          <td>TCGA-AR-A1AS</td>
          <td>brca_tcga</td>
          <td>1.2692087467241393</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>283</th>
          <td>VENHQS1BUi1BMUFWLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFWOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-AR-A1AV-01</td>
          <td>TCGA-AR-A1AV</td>
          <td>brca_tcga</td>
          <td>-1.0879171469891096</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>284</th>
          <td>VENHQS1BUi1BMUFXLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFXOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-AR-A1AW-01</td>
          <td>TCGA-AR-A1AW</td>
          <td>brca_tcga</td>
          <td>-0.06646907668277764</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>285</th>
          <td>VENHQS1CSC1BMERELTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMEREOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-BH-A0DD-01</td>
          <td>TCGA-BH-A0DD</td>
          <td>brca_tcga</td>
          <td>-1.5077329846223932</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>286</th>
          <td>VENHQS1CSC1BMERHLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMERHOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-BH-A0DG-01</td>
          <td>TCGA-BH-A0DG</td>
          <td>brca_tcga</td>
          <td>0.18414782925259893</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
      </tbody>
    </table>
    <p>287 rows × 9 columns</p>
    </div>



.. code:: ipython3

    df2b = gad.fetch_generic_assay_data(generic_assay_stable_ids=["TULP4_pS563", "TEP1_pS397", "ALAD_214_215_1_1_S215"],                            
                                        sample_molecular_identifiers=[
                                                          {"molecular_profile_id": "brca_tcga_phosphoprotein_quantification",  
                                                           "sample_ids": ["TCGA-C8-A130-01", "TCGA-C8-A134-01"]},
                                                          {"molecular_profile_id": "brain_cptac_2020_phosphoprotein", 
                                                           "sample_ids": ["7316-101", "7316-109"]}
                                                          ])
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
          <th>value</th>
          <th>genericAssayStableId</th>
          <th>stableId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>NzMxNi0xMDE6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>UFRfQ1dENzE3UTA6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-101</td>
          <td>PT_CWD717Q0</td>
          <td>brain_cptac_2020</td>
          <td>0.293524074916423</td>
          <td>ALAD_214_215_1_1_S215</td>
          <td>ALAD_214_215_1_1_S215</td>
        </tr>
        <tr>
          <th>1</th>
          <td>NzMxNi0xMDk6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>UFRfNUZSMllBNkU6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-109</td>
          <td>PT_5FR2YA6E</td>
          <td>brain_cptac_2020</td>
          <td>-0.709355260194312</td>
          <td>ALAD_214_215_1_1_S215</td>
          <td>ALAD_214_215_1_1_S215</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1DOC1BMTMwLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTMwOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A130-01</td>
          <td>TCGA-C8-A130</td>
          <td>brca_tcga</td>
          <td>0.31374650000644216</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1DOC1BMTMwLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTMwOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A130-01</td>
          <td>TCGA-C8-A130</td>
          <td>brca_tcga</td>
          <td>1.8338606392734915</td>
          <td>TULP4_pS563</td>
          <td>TULP4_pS563</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>0.13629911078391418</td>
          <td>TEP1_pS397</td>
          <td>TEP1_pS397</td>
        </tr>
        <tr>
          <th>5</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>-0.2314224260050513</td>
          <td>TULP4_pS563</td>
          <td>TULP4_pS563</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2c = gad.fetch_generic_assay_data(sample_molecular_identifiers=[
                                                            {"molecular_profile_id": "brca_tcga_phosphoprotein_quantification",  
                                                             "sample_ids": ["TCGA-C8-A130-01", "TCGA-C8-A134-01"]},
                                                            {"molecular_profile_id": "brain_cptac_2020_phosphoprotein", 
                                                             "sample_ids": ["7316-101", "7316-109"]}
                                                            ])
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
          <th>studyId</th>
          <th>value</th>
          <th>genericAssayStableId</th>
          <th>stableId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>NzMxNi0xMDE6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>UFRfQ1dENzE3UTA6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-101</td>
          <td>PT_CWD717Q0</td>
          <td>brain_cptac_2020</td>
          <td>0.293524074916423</td>
          <td>ALAD_214_215_1_1_S215</td>
          <td>ALAD_214_215_1_1_S215</td>
        </tr>
        <tr>
          <th>1</th>
          <td>NzMxNi0xMDE6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>UFRfQ1dENzE3UTA6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-101</td>
          <td>PT_CWD717Q0</td>
          <td>brain_cptac_2020</td>
          <td>1.18589905169363</td>
          <td>ALDOA_36_39_1_1_S36</td>
          <td>ALDOA_36_39_1_1_S36</td>
        </tr>
        <tr>
          <th>2</th>
          <td>NzMxNi0xMDE6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>UFRfQ1dENzE3UTA6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-101</td>
          <td>PT_CWD717Q0</td>
          <td>brain_cptac_2020</td>
          <td>1.05737336393577</td>
          <td>ALDOA_36_39_1_1_S39</td>
          <td>ALDOA_36_39_1_1_S39</td>
        </tr>
        <tr>
          <th>3</th>
          <td>NzMxNi0xMDE6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>UFRfQ1dENzE3UTA6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-101</td>
          <td>PT_CWD717Q0</td>
          <td>brain_cptac_2020</td>
          <td>0.0624267000967347</td>
          <td>ALDOA_46_52_1_1_S46</td>
          <td>ALDOA_46_52_1_1_S46</td>
        </tr>
        <tr>
          <th>4</th>
          <td>NzMxNi0xMDE6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>UFRfQ1dENzE3UTA6YnJhaW5fY3B0YWNfMjAyMA</td>
          <td>brain_cptac_2020_phosphoprotein</td>
          <td>7316-101</td>
          <td>PT_CWD717Q0</td>
          <td>brain_cptac_2020</td>
          <td>-1.46987364905827</td>
          <td>ANK1_1684_1693_1_1_S1686</td>
          <td>ANK1_1684_1693_1_1_S1686</td>
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
        </tr>
        <tr>
          <th>56312</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>0.6904941038059361</td>
          <td>OTUD4_pS320</td>
          <td>OTUD4_pS320</td>
        </tr>
        <tr>
          <th>56313</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>0.5406159008386409</td>
          <td>TBKBP1_pS415</td>
          <td>TBKBP1_pS415</td>
        </tr>
        <tr>
          <th>56314</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>0.34418985891868537</td>
          <td>PTPN3_pS241</td>
          <td>PTPN3_pS241</td>
        </tr>
        <tr>
          <th>56315</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>0.6839793452245334</td>
          <td>SIK2_pT484</td>
          <td>SIK2_pT484</td>
        </tr>
        <tr>
          <th>56316</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>0.36039894811889295</td>
          <td>PKN2_pT958</td>
          <td>PKN2_pT958</td>
        </tr>
      </tbody>
    </table>
    <p>56317 rows × 9 columns</p>
    </div>



.. code:: ipython3

    df3 = gad.get_generic_assay_data_in_molecular_profile(molecular_profile_id = "brca_tcga_phosphoprotein_quantification", 
                                                          generic_assay_stable_id = "TULP4_pS563")
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
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>studyId</th>
          <th>value</th>
          <th>genericAssayStableId</th>
          <th>stableId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BOC1BMDlHLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BOC1BMDlHOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-A8-A09G-01</td>
          <td>TCGA-A8-A09G</td>
          <td>brca_tcga</td>
          <td>-2.1236739808061182</td>
          <td>TULP4_pS563</td>
          <td>TULP4_pS563</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1DOC1BMTMwLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTMwOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A130-01</td>
          <td>TCGA-C8-A130</td>
          <td>brca_tcga</td>
          <td>1.8338606392734915</td>
          <td>TULP4_pS563</td>
          <td>TULP4_pS563</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1DOC1BMTM0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTM0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-C8-A134-01</td>
          <td>TCGA-C8-A134</td>
          <td>brca_tcga</td>
          <td>-0.2314224260050513</td>
          <td>TULP4_pS563</td>
          <td>TULP4_pS563</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1CSC1BMThRLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMThROmJyY2FfdGNnYQ</td>
          <td>brca_tcga_phosphoprotein_quantification</td>
          <td>TCGA-BH-A18Q-01</td>
          <td>TCGA-BH-A18Q</td>
          <td>brca_tcga</td>
          <td>-2.3187358473784534</td>
          <td>TULP4_pS563</td>
          <td>TULP4_pS563</td>
        </tr>
      </tbody>
    </table>
    </div>


