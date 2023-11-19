.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioPortal import clinical_attributes as ca

.. code:: ipython3

    df1 = ca.get_all_clinical_attributes()
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
          <th>displayName</th>
          <th>description</th>
          <th>datatype</th>
          <th>patientAttribute</th>
          <th>priority</th>
          <th>clinicalAttributeId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Adjuvant Chemotherapy</td>
          <td>Adjuvant Chemotherapy</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>ADJUVANT_CHEMO</td>
          <td>acbc_mskcc_2015</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Adjuvant Treatment</td>
          <td>Adjuvant treatment.</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>ADJUVANT_TX</td>
          <td>acbc_mskcc_2015</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Diagnosis Age</td>
          <td>Age at which a condition or disease was first ...</td>
          <td>NUMBER</td>
          <td>True</td>
          <td>1</td>
          <td>AGE</td>
          <td>acbc_mskcc_2015</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Cancer Type</td>
          <td>Cancer Type</td>
          <td>STRING</td>
          <td>False</td>
          <td>1</td>
          <td>CANCER_TYPE</td>
          <td>acbc_mskcc_2015</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Cancer Type Detailed</td>
          <td>Cancer Type Detailed</td>
          <td>STRING</td>
          <td>False</td>
          <td>1</td>
          <td>CANCER_TYPE_DETAILED</td>
          <td>acbc_mskcc_2015</td>
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
          <th>14752</th>
          <td>Race Category</td>
          <td>The text for reporting information about race.</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>RACE</td>
          <td>wt_target_2018_pub</td>
        </tr>
        <tr>
          <th>14753</th>
          <td>Number of Samples Per Patient</td>
          <td>Number of Samples Per Patient</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>SAMPLE_COUNT</td>
          <td>wt_target_2018_pub</td>
        </tr>
        <tr>
          <th>14754</th>
          <td>Sex</td>
          <td>Sex</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>SEX</td>
          <td>wt_target_2018_pub</td>
        </tr>
        <tr>
          <th>14755</th>
          <td>Somatic Status</td>
          <td>Somatic Status</td>
          <td>STRING</td>
          <td>False</td>
          <td>1</td>
          <td>SOMATIC_STATUS</td>
          <td>wt_target_2018_pub</td>
        </tr>
        <tr>
          <th>14756</th>
          <td>TMB (nonsynonymous)</td>
          <td>TMB (nonsynonymous)</td>
          <td>NUMBER</td>
          <td>False</td>
          <td>1</td>
          <td>TMB_NONSYNONYMOUS</td>
          <td>wt_target_2018_pub</td>
        </tr>
      </tbody>
    </table>
    <p>14757 rows × 7 columns</p>
    </div>



.. code:: ipython3

    df2 = ca.fetch_clinical_attributes(study_ids=["brca_tcga", "brca_bccrc"])
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
          <th>displayName</th>
          <th>description</th>
          <th>datatype</th>
          <th>patientAttribute</th>
          <th>priority</th>
          <th>clinicalAttributeId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Diagnosis Age</td>
          <td>Age at which a condition or disease was first ...</td>
          <td>NUMBER</td>
          <td>True</td>
          <td>1</td>
          <td>AGE</td>
          <td>brca_bccrc</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Angiolymphatic Invasion</td>
          <td>Presence of angiolymphatic invasion.</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>ANGIOLYMPHATIC_INVASION</td>
          <td>brca_bccrc</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Cancer Type</td>
          <td>Cancer Type</td>
          <td>STRING</td>
          <td>False</td>
          <td>1</td>
          <td>CANCER_TYPE</td>
          <td>brca_bccrc</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Cancer Type Detailed</td>
          <td>Cancer Type Detailed</td>
          <td>STRING</td>
          <td>False</td>
          <td>1</td>
          <td>CANCER_TYPE_DETAILED</td>
          <td>brca_bccrc</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Neoplasm American Joint Committee on Cancer Cl...</td>
          <td>Extent of the distant metastasis for the cance...</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>CLIN_M_STAGE</td>
          <td>brca_bccrc</td>
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
          <th>156</th>
          <td>Time between excision and freezing</td>
          <td>Time between excision and freezing</td>
          <td>STRING</td>
          <td>False</td>
          <td>1</td>
          <td>TIME_BETWEEN_EXCISION_AND_FREEZING</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>157</th>
          <td>Tissue Source Site</td>
          <td>A Tissue Source Site collects samples (tissue,...</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>TISSUE_SOURCE_SITE</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>158</th>
          <td>TMB (nonsynonymous)</td>
          <td>TMB (nonsynonymous)</td>
          <td>NUMBER</td>
          <td>False</td>
          <td>1</td>
          <td>TMB_NONSYNONYMOUS</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>159</th>
          <td>Person Neoplasm Status</td>
          <td>The state or condition of an individual's neop...</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>TUMOR_STATUS</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>160</th>
          <td>Vial number</td>
          <td>Vial number</td>
          <td>STRING</td>
          <td>False</td>
          <td>1</td>
          <td>VIAL_NUMBER</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    <p>161 rows × 7 columns</p>
    </div>



.. code:: ipython3

    df3a = ca.get_all_clinical_attributes_in_study(study_id="brca_tcga", projection="DETAILED")
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
          <th>displayName</th>
          <th>description</th>
          <th>datatype</th>
          <th>patientAttribute</th>
          <th>priority</th>
          <th>clinicalAttributeId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Diagnosis Age</td>
          <td>Age at which a condition or disease was first ...</td>
          <td>NUMBER</td>
          <td>True</td>
          <td>1</td>
          <td>AGE</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>American Joint Committee on Cancer Metastasis ...</td>
          <td>Code to represent the defined absence or prese...</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>AJCC_METASTASIS_PATHOLOGIC_PM</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Neoplasm Disease Lymph Node Stage American Joi...</td>
          <td>The codes that represent the stage of cancer b...</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>AJCC_NODES_PATHOLOGIC_PN</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Neoplasm Disease Stage American Joint Committe...</td>
          <td>The extent of a cancer, especially whether the...</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>AJCC_PATHOLOGIC_TUMOR_STAGE</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>4</th>
          <td>American Joint Committee on Cancer Publication...</td>
          <td>The version or edition of the American Joint C...</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>AJCC_STAGING_EDITION</td>
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
        </tr>
        <tr>
          <th>133</th>
          <td>Time between excision and freezing</td>
          <td>Time between excision and freezing</td>
          <td>STRING</td>
          <td>False</td>
          <td>1</td>
          <td>TIME_BETWEEN_EXCISION_AND_FREEZING</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>134</th>
          <td>Tissue Source Site</td>
          <td>A Tissue Source Site collects samples (tissue,...</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>TISSUE_SOURCE_SITE</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>135</th>
          <td>TMB (nonsynonymous)</td>
          <td>TMB (nonsynonymous)</td>
          <td>NUMBER</td>
          <td>False</td>
          <td>1</td>
          <td>TMB_NONSYNONYMOUS</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>136</th>
          <td>Person Neoplasm Status</td>
          <td>The state or condition of an individual's neop...</td>
          <td>STRING</td>
          <td>True</td>
          <td>1</td>
          <td>TUMOR_STATUS</td>
          <td>brca_tcga</td>
        </tr>
        <tr>
          <th>137</th>
          <td>Vial number</td>
          <td>Vial number</td>
          <td>STRING</td>
          <td>False</td>
          <td>1</td>
          <td>VIAL_NUMBER</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    <p>138 rows × 7 columns</p>
    </div>



In case of data not present on cBioPortal a notification message is
reported.

.. code:: ipython3

    df3b = ca.get_all_clinical_attributes_in_study(study_id="brca_tcga", projection="META")
    df3b


.. parsed-literal::

    Response is empty. No data available.
    

.. code:: ipython3

    df4 = ca.get_clinical_attribute_in_study(study_id="brca_tcga", clinical_attribute_id="AGE")
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
          <th>displayName</th>
          <th>description</th>
          <th>datatype</th>
          <th>patientAttribute</th>
          <th>priority</th>
          <th>clinicalAttributeId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Diagnosis Age</td>
          <td>Age at which a condition or disease was first ...</td>
          <td>NUMBER</td>
          <td>True</td>
          <td>1</td>
          <td>AGE</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    </div>


