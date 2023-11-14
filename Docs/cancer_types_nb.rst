.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioGate import cancer_types as ct

.. code:: ipython3

    df1 = ct.get_all_cancer_types()
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
          <th>dedicatedColor</th>
          <th>shortName</th>
          <th>parent</th>
          <th>cancerTypeId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Aggressive Angiomyxoma</td>
          <td>LightYellow</td>
          <td>AA</td>
          <td>soft_tissue</td>
          <td>aa</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Anaplastic Astrocytoma</td>
          <td>Gray</td>
          <td>AASTR</td>
          <td>difg</td>
          <td>aastr</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Activated B-cell Type</td>
          <td>LimeGreen</td>
          <td>ABC</td>
          <td>dlbclnos</td>
          <td>abc</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Acute Basophilic Leukemia</td>
          <td>LightSalmon</td>
          <td>ABL</td>
          <td>amlnos</td>
          <td>abl</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Adrenocortical Adenoma</td>
          <td>Purple</td>
          <td>ACA</td>
          <td>adrenal_gland</td>
          <td>aca</td>
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
          <th>880</th>
          <td>Well-Differentiated Liposarcoma</td>
          <td>LightYellow</td>
          <td>WDLS</td>
          <td>lipo</td>
          <td>wdls</td>
        </tr>
        <tr>
          <th>881</th>
          <td>Well-Differentiated Thyroid Cancer</td>
          <td>Teal</td>
          <td>WDTC</td>
          <td>thyroid</td>
          <td>wdtc</td>
        </tr>
        <tr>
          <th>882</th>
          <td>Waldenstrom Macroglobulinemia</td>
          <td>LimeGreen</td>
          <td>WM</td>
          <td>lpl</td>
          <td>wm</td>
        </tr>
        <tr>
          <th>883</th>
          <td>Warty Penile Squamous Cell Carcinoma</td>
          <td>Blue</td>
          <td>WPSCC</td>
          <td>pscc</td>
          <td>wpscc</td>
        </tr>
        <tr>
          <th>884</th>
          <td>Wilms' Tumor</td>
          <td>Orange</td>
          <td>WT</td>
          <td>kidney</td>
          <td>wt</td>
        </tr>
      </tbody>
    </table>
    <p>885 rows × 5 columns</p>
    </div>



.. code:: ipython3

    df2 = ct.get_cancer_type(cancer_type_id="brca")
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
          <th>dedicatedColor</th>
          <th>shortName</th>
          <th>parent</th>
          <th>cancerTypeId</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Invasive Breast Carcinoma</td>
          <td>HotPink</td>
          <td>BRCA</td>
          <td>breast</td>
          <td>brca</td>
        </tr>
      </tbody>
    </table>
    </div>


