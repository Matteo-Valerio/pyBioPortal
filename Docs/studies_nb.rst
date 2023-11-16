.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioGate import studies as std

.. code:: ipython3

    df1 = std.get_all_studies(keyword="TCGA", projection="DETAILED")
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
          <th>name</th>
          <th>description</th>
          <th>publicStudy</th>
          <th>groups</th>
          <th>status</th>
          <th>importDate</th>
          <th>allSampleCount</th>
          <th>sequencedSampleCount</th>
          <th>cnaSampleCount</th>
          <th>mrnaRnaSeqSampleCount</th>
          <th>...</th>
          <th>studyId</th>
          <th>cancerTypeId</th>
          <th>cancerType_name</th>
          <th>cancerType_dedicatedColor</th>
          <th>cancerType_shortName</th>
          <th>cancerType_parent</th>
          <th>cancerType_cancerTypeId</th>
          <th>referenceGenome</th>
          <th>pmid</th>
          <th>citation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Acute Myeloid Leukemia (TCGA, Firehose Legacy)</td>
          <td>TCGA Acute Myeloid Leukemia. Source data from ...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-06-19 09:43:19</td>
          <td>200</td>
          <td>197</td>
          <td>191</td>
          <td>179</td>
          <td>...</td>
          <td>laml_tcga</td>
          <td>aml</td>
          <td>Acute Myeloid Leukemia</td>
          <td>LightSalmon</td>
          <td>AML</td>
          <td>mnm</td>
          <td>aml</td>
          <td>hg19</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Acute Myeloid Leukemia (TCGA, NEJM 2013)</td>
          <td>Whole-genome or whole-exome sequencing analysi...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-06-19 23:07:48</td>
          <td>200</td>
          <td>200</td>
          <td>191</td>
          <td>0</td>
          <td>...</td>
          <td>laml_tcga_pub</td>
          <td>aml</td>
          <td>Acute Myeloid Leukemia</td>
          <td>LightSalmon</td>
          <td>AML</td>
          <td>mnm</td>
          <td>aml</td>
          <td>hg19</td>
          <td>23634996</td>
          <td>TCGA, NEJM 2013</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Acute Myeloid Leukemia (TCGA, PanCancer Atlas)</td>
          <td>Acute Myeloid Leukemia TCGA PanCancer data. Th...</td>
          <td>True</td>
          <td>PUBLIC;PANCAN</td>
          <td>0</td>
          <td>2023-06-19 12:05:01</td>
          <td>200</td>
          <td>200</td>
          <td>191</td>
          <td>0</td>
          <td>...</td>
          <td>laml_tcga_pan_can_atlas_2018</td>
          <td>aml</td>
          <td>Acute Myeloid Leukemia</td>
          <td>LightSalmon</td>
          <td>AML</td>
          <td>mnm</td>
          <td>aml</td>
          <td>hg19</td>
          <td>29625048,29596782,29622463,29617662,29625055,2...</td>
          <td>TCGA, Cell 2018</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Adrenocortical Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Adrenocortical Carcinoma. Source data fro...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-06-19 09:42:47</td>
          <td>92</td>
          <td>90</td>
          <td>90</td>
          <td>0</td>
          <td>...</td>
          <td>acc_tcga</td>
          <td>acc</td>
          <td>Adrenocortical Carcinoma</td>
          <td>Purple</td>
          <td>ACC</td>
          <td>adrenal_gland</td>
          <td>acc</td>
          <td>hg19</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Adrenocortical Carcinoma (TCGA, PanCancer Atlas)</td>
          <td>Adrenocortical Carcinoma TCGA PanCancer data. ...</td>
          <td>True</td>
          <td>PUBLIC;PANCAN</td>
          <td>0</td>
          <td>2023-08-12 08:25:24</td>
          <td>92</td>
          <td>91</td>
          <td>89</td>
          <td>0</td>
          <td>...</td>
          <td>acc_tcga_pan_can_atlas_2018</td>
          <td>acc</td>
          <td>Adrenocortical Carcinoma</td>
          <td>Purple</td>
          <td>ACC</td>
          <td>adrenal_gland</td>
          <td>acc</td>
          <td>hg19</td>
          <td>29625048,29596782,29622463,29617662,29625055,2...</td>
          <td>TCGA, Cell 2018</td>
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
          <th>86</th>
          <td>Uterine Corpus Endometrial Carcinoma (TCGA, Na...</td>
          <td>Whole exome sequencing of 373 endometrial carc...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-06-20 17:02:23</td>
          <td>373</td>
          <td>248</td>
          <td>363</td>
          <td>0</td>
          <td>...</td>
          <td>ucec_tcga_pub</td>
          <td>ucec</td>
          <td>Endometrial Carcinoma</td>
          <td>PeachPuff</td>
          <td>UCEC</td>
          <td>uterus</td>
          <td>ucec</td>
          <td>hg19</td>
          <td>23636398</td>
          <td>TCGA, Nature 2013</td>
        </tr>
        <tr>
          <th>87</th>
          <td>Uterine Corpus Endometrial Carcinoma (TCGA, Pa...</td>
          <td>Uterine Corpus Endometrial Carcinoma TCGA PanC...</td>
          <td>True</td>
          <td>PUBLIC;PANCAN</td>
          <td>0</td>
          <td>2023-08-15 17:17:50</td>
          <td>529</td>
          <td>517</td>
          <td>523</td>
          <td>0</td>
          <td>...</td>
          <td>ucec_tcga_pan_can_atlas_2018</td>
          <td>ucec</td>
          <td>Endometrial Carcinoma</td>
          <td>PeachPuff</td>
          <td>UCEC</td>
          <td>uterus</td>
          <td>ucec</td>
          <td>hg19</td>
          <td>29625048,29596782,29622463,29617662,29625055,2...</td>
          <td>TCGA, Cell 2018</td>
        </tr>
        <tr>
          <th>88</th>
          <td>Uveal Melanoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Uveal Melanoma. Source data from &lt;A HREF=...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-06-19 11:16:24</td>
          <td>80</td>
          <td>80</td>
          <td>80</td>
          <td>0</td>
          <td>...</td>
          <td>uvm_tcga</td>
          <td>um</td>
          <td>Uveal Melanoma</td>
          <td>Green</td>
          <td>UM</td>
          <td>om</td>
          <td>um</td>
          <td>hg19</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>89</th>
          <td>Uveal Melanoma (TCGA, PanCancer Atlas)</td>
          <td>Uveal melanoma TCGA PanCancer data. The origin...</td>
          <td>True</td>
          <td>PUBLIC;PANCAN</td>
          <td>0</td>
          <td>2023-08-15 21:52:13</td>
          <td>80</td>
          <td>80</td>
          <td>80</td>
          <td>0</td>
          <td>...</td>
          <td>uvm_tcga_pan_can_atlas_2018</td>
          <td>um</td>
          <td>Uveal Melanoma</td>
          <td>Green</td>
          <td>UM</td>
          <td>om</td>
          <td>um</td>
          <td>hg19</td>
          <td>29625048,29596782,29622463,29617662,29625055,2...</td>
          <td>TCGA, Cell 2018</td>
        </tr>
        <tr>
          <th>90</th>
          <td>RAD51B Associated Mixed Cancers (Mandelker 2021)</td>
          <td>Germline RAD51B loss-of-function variants conf...</td>
          <td>True</td>
          <td></td>
          <td>0</td>
          <td>2023-06-20 10:33:20</td>
          <td>19</td>
          <td>19</td>
          <td>0</td>
          <td>0</td>
          <td>...</td>
          <td>mixed_msk_tcga_2021</td>
          <td>mixed</td>
          <td>Mixed Cancer Types</td>
          <td>Black</td>
          <td>MIXED</td>
          <td>other</td>
          <td>mixed</td>
          <td>hg19</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    <p>91 rows × 29 columns</p>
    </div>



.. code:: ipython3

    df2 = std.get_study(study_id="brca_tcga")
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
          <th>name</th>
          <th>description</th>
          <th>publicStudy</th>
          <th>groups</th>
          <th>status</th>
          <th>importDate</th>
          <th>allSampleCount</th>
          <th>sequencedSampleCount</th>
          <th>cnaSampleCount</th>
          <th>mrnaRnaSeqSampleCount</th>
          <th>...</th>
          <th>readPermission</th>
          <th>treatmentCount</th>
          <th>studyId</th>
          <th>cancerTypeId</th>
          <th>cancerType_name</th>
          <th>cancerType_dedicatedColor</th>
          <th>cancerType_shortName</th>
          <th>cancerType_parent</th>
          <th>cancerType_cancerTypeId</th>
          <th>referenceGenome</th>
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
          <td>1108</td>
          <td>982</td>
          <td>1080</td>
          <td>0</td>
          <td>...</td>
          <td>True</td>
          <td>0</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>Invasive Breast Carcinoma</td>
          <td>HotPink</td>
          <td>BRCA</td>
          <td>breast</td>
          <td>brca</td>
          <td>hg19</td>
        </tr>
      </tbody>
    </table>
    <p>1 rows × 27 columns</p>
    </div>



.. code:: ipython3

    df3 = std.get_tags_of_study(study_id="bowel_colitis_msk_2022")
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
        </tr>
      </thead>
      <tbody>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df4 = std.fetch_studies(study_ids=["brca_tcga","acc_tcga"], projection="DETAILED")
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
          <th>name</th>
          <th>description</th>
          <th>publicStudy</th>
          <th>groups</th>
          <th>status</th>
          <th>importDate</th>
          <th>allSampleCount</th>
          <th>sequencedSampleCount</th>
          <th>cnaSampleCount</th>
          <th>mrnaRnaSeqSampleCount</th>
          <th>...</th>
          <th>readPermission</th>
          <th>treatmentCount</th>
          <th>studyId</th>
          <th>cancerTypeId</th>
          <th>cancerType_name</th>
          <th>cancerType_dedicatedColor</th>
          <th>cancerType_shortName</th>
          <th>cancerType_parent</th>
          <th>cancerType_cancerTypeId</th>
          <th>referenceGenome</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Adrenocortical Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Adrenocortical Carcinoma. Source data fro...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-06-19 09:42:47</td>
          <td>92</td>
          <td>90</td>
          <td>90</td>
          <td>0</td>
          <td>...</td>
          <td>True</td>
          <td>0</td>
          <td>acc_tcga</td>
          <td>acc</td>
          <td>Adrenocortical Carcinoma</td>
          <td>Purple</td>
          <td>ACC</td>
          <td>adrenal_gland</td>
          <td>acc</td>
          <td>hg19</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Breast Invasive Carcinoma (TCGA, Firehose Legacy)</td>
          <td>TCGA Breast Invasive Carcinoma. Source data fr...</td>
          <td>True</td>
          <td>PUBLIC</td>
          <td>0</td>
          <td>2023-11-09 17:45:45</td>
          <td>1108</td>
          <td>982</td>
          <td>1080</td>
          <td>0</td>
          <td>...</td>
          <td>True</td>
          <td>0</td>
          <td>brca_tcga</td>
          <td>brca</td>
          <td>Invasive Breast Carcinoma</td>
          <td>HotPink</td>
          <td>BRCA</td>
          <td>breast</td>
          <td>brca</td>
          <td>hg19</td>
        </tr>
      </tbody>
    </table>
    <p>2 rows × 27 columns</p>
    </div>



.. code:: ipython3

    df5 = std.fetch_tags_for_studies(study_ids=["brca_tcga","acc_tcga"])
    df5


.. parsed-literal::

    Response is empty. No data available.
    
