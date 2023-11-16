.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioGate import molecular_profiles as mf

.. code:: ipython3

    df1 = mf.get_all_molecular_profiles()
    df1.head(5)




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
          <th>molecularAlterationType</th>
          <th>datatype</th>
          <th>name</th>
          <th>description</th>
          <th>showProfileInAnalysisTab</th>
          <th>patientLevel</th>
          <th>molecularProfileId</th>
          <th>studyId</th>
          <th>genericAssayType</th>
          <th>pivotThreshold</th>
          <th>sortOrder</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>PROTEIN_LEVEL</td>
          <td>LOG2-VALUE</td>
          <td>Protein expression (RPPA)</td>
          <td>Protein expression measured by reverse-phase p...</td>
          <td>False</td>
          <td>False</td>
          <td>acc_tcga_rppa</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>PROTEIN_LEVEL</td>
          <td>Z-SCORE</td>
          <td>Protein expression z-scores (RPPA)</td>
          <td>Protein expression, measured by reverse-phase ...</td>
          <td>True</td>
          <td>False</td>
          <td>acc_tcga_rppa_Zscores</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>2</th>
          <td>COPY_NUMBER_ALTERATION</td>
          <td>DISCRETE</td>
          <td>Putative copy-number alterations from GISTIC</td>
          <td>Putative copy-number calls on 90 cases determi...</td>
          <td>True</td>
          <td>False</td>
          <td>acc_tcga_gistic</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>3</th>
          <td>COPY_NUMBER_ALTERATION</td>
          <td>CONTINUOUS</td>
          <td>Capped relative linear copy-number values</td>
          <td>Capped relative linear copy-number values for ...</td>
          <td>False</td>
          <td>False</td>
          <td>acc_tcga_linear_CNA</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td>MUTATION_EXTENDED</td>
          <td>MAF</td>
          <td>Mutations</td>
          <td>Mutation data from whole exome sequencing. Mut...</td>
          <td>True</td>
          <td>False</td>
          <td>acc_tcga_mutations</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2 = mf.get_molecular_profile("gbm_tcga_pan_can_atlas_2018_armlevel_cna")
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
          <th>molecularAlterationType</th>
          <th>genericAssayType</th>
          <th>datatype</th>
          <th>name</th>
          <th>description</th>
          <th>showProfileInAnalysisTab</th>
          <th>patientLevel</th>
          <th>molecularProfileId</th>
          <th>studyId</th>
          <th>study_name</th>
          <th>...</th>
          <th>study_publicStudy</th>
          <th>study_pmid</th>
          <th>study_citation</th>
          <th>study_groups</th>
          <th>study_status</th>
          <th>study_importDate</th>
          <th>study_readPermission</th>
          <th>study_studyId</th>
          <th>study_cancerTypeId</th>
          <th>study_referenceGenome</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>GENERIC_ASSAY</td>
          <td>ARMLEVEL_CNA</td>
          <td>CATEGORICAL</td>
          <td>Putative arm-level copy-number from GISTIC</td>
          <td>Putative arm-level copy-number from GISTIC 2.0.</td>
          <td>True</td>
          <td>False</td>
          <td>gbm_tcga_pan_can_atlas_2018_armlevel_cna</td>
          <td>gbm_tcga_pan_can_atlas_2018</td>
          <td>Glioblastoma Multiforme (TCGA, PanCancer Atlas)</td>
          <td>...</td>
          <td>True</td>
          <td>29625048,29596782,29622463,29617662,29625055,2...</td>
          <td>TCGA, Cell 2018</td>
          <td>PUBLIC;PANCAN</td>
          <td>0</td>
          <td>2023-08-14 08:28:47</td>
          <td>True</td>
          <td>gbm_tcga_pan_can_atlas_2018</td>
          <td>gbm</td>
          <td>hg19</td>
        </tr>
      </tbody>
    </table>
    <p>1 rows × 21 columns</p>
    </div>



.. code:: ipython3

    df3a = mf.fetch_molecular_profiles(molecular_profile_ids=["brca_tcga_mrna", "acc_tcga_rna_seq_v2_mrna"])
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
          <th>molecularAlterationType</th>
          <th>datatype</th>
          <th>name</th>
          <th>description</th>
          <th>showProfileInAnalysisTab</th>
          <th>patientLevel</th>
          <th>molecularProfileId</th>
          <th>studyId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>MRNA_EXPRESSION</td>
          <td>CONTINUOUS</td>
          <td>mRNA expression (RNA Seq V2 RSEM)</td>
          <td>mRNA gene expression (RNA Seq V2 RSEM)</td>
          <td>False</td>
          <td>False</td>
          <td>acc_tcga_rna_seq_v2_mrna</td>
          <td>acc_tcga</td>
        </tr>
        <tr>
          <th>1</th>
          <td>MRNA_EXPRESSION</td>
          <td>CONTINUOUS</td>
          <td>mRNA expression (microarray)</td>
          <td>Expression levels for 17155 genes in 590 brca ...</td>
          <td>False</td>
          <td>False</td>
          <td>brca_tcga_mrna</td>
          <td>brca_tcga</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df3b = mf.fetch_molecular_profiles(study_ids=["brca_tcga", "acc_tcga"])
    df3b.head(5)




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
          <th>molecularAlterationType</th>
          <th>datatype</th>
          <th>name</th>
          <th>description</th>
          <th>showProfileInAnalysisTab</th>
          <th>patientLevel</th>
          <th>molecularProfileId</th>
          <th>studyId</th>
          <th>genericAssayType</th>
          <th>pivotThreshold</th>
          <th>sortOrder</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>PROTEIN_LEVEL</td>
          <td>LOG2-VALUE</td>
          <td>Protein expression (RPPA)</td>
          <td>Protein expression measured by reverse-phase p...</td>
          <td>False</td>
          <td>False</td>
          <td>acc_tcga_rppa</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>PROTEIN_LEVEL</td>
          <td>Z-SCORE</td>
          <td>Protein expression z-scores (RPPA)</td>
          <td>Protein expression, measured by reverse-phase ...</td>
          <td>True</td>
          <td>False</td>
          <td>acc_tcga_rppa_Zscores</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>2</th>
          <td>COPY_NUMBER_ALTERATION</td>
          <td>DISCRETE</td>
          <td>Putative copy-number alterations from GISTIC</td>
          <td>Putative copy-number calls on 90 cases determi...</td>
          <td>True</td>
          <td>False</td>
          <td>acc_tcga_gistic</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>3</th>
          <td>COPY_NUMBER_ALTERATION</td>
          <td>CONTINUOUS</td>
          <td>Capped relative linear copy-number values</td>
          <td>Capped relative linear copy-number values for ...</td>
          <td>False</td>
          <td>False</td>
          <td>acc_tcga_linear_CNA</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td>MUTATION_EXTENDED</td>
          <td>MAF</td>
          <td>Mutations</td>
          <td>Mutation data from whole exome sequencing. Mut...</td>
          <td>True</td>
          <td>False</td>
          <td>acc_tcga_mutations</td>
          <td>acc_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df4 = mf.get_all_molecular_profiles_in_study(study_id="brca_tcga", sortBy="description")
    df4.head(5)




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
          <th>molecularAlterationType</th>
          <th>datatype</th>
          <th>name</th>
          <th>description</th>
          <th>showProfileInAnalysisTab</th>
          <th>patientLevel</th>
          <th>molecularProfileId</th>
          <th>studyId</th>
          <th>genericAssayType</th>
          <th>pivotThreshold</th>
          <th>sortOrder</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>COPY_NUMBER_ALTERATION</td>
          <td>CONTINUOUS</td>
          <td>Capped relative linear copy-number values</td>
          <td>Capped relative linear copy-number values for ...</td>
          <td>False</td>
          <td>False</td>
          <td>brca_tcga_linear_CNA</td>
          <td>brca_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>MRNA_EXPRESSION</td>
          <td>CONTINUOUS</td>
          <td>mRNA expression (microarray)</td>
          <td>Expression levels for 17155 genes in 590 brca ...</td>
          <td>False</td>
          <td>False</td>
          <td>brca_tcga_mrna</td>
          <td>brca_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>2</th>
          <td>MRNA_EXPRESSION</td>
          <td>Z-SCORE</td>
          <td>mRNA expression z-scores relative to all sampl...</td>
          <td>Log-transformed mRNA expression z-scores compa...</td>
          <td>True</td>
          <td>False</td>
          <td>brca_tcga_mrna_median_all_sample_Zscores</td>
          <td>brca_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>3</th>
          <td>MRNA_EXPRESSION</td>
          <td>Z-SCORE</td>
          <td>mRNA expression z-scores relative to all sampl...</td>
          <td>Log-transformed mRNA expression z-scores compa...</td>
          <td>True</td>
          <td>False</td>
          <td>brca_tcga_rna_seq_v2_mrna_median_all_sample_Zs...</td>
          <td>brca_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td>METHYLATION</td>
          <td>CONTINUOUS</td>
          <td>Methylation (HM450)</td>
          <td>Methylation (HM450) beta-values for genes in 8...</td>
          <td>False</td>
          <td>False</td>
          <td>brca_tcga_methylation_hm450</td>
          <td>brca_tcga</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>


