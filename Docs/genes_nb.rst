.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioGate import genes as gns

.. code:: ipython3

    df1a = gns.get_all_genes(keyword = "BRCA1")
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
          <th>entrezGeneId</th>
          <th>hugoGeneSymbol</th>
          <th>type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>394269</td>
          <td>BRCA1P1</td>
          <td>pseudogene</td>
        </tr>
        <tr>
          <th>1</th>
          <td>672</td>
          <td>BRCA1</td>
          <td>protein-coding</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df1b = gns.get_all_genes(alias = "FANCS")
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
          <th>entrezGeneId</th>
          <th>hugoGeneSymbol</th>
          <th>type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>672</td>
          <td>BRCA1</td>
          <td>protein-coding</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2 = gns.get_gene("BRCA1")
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
          <th>entrezGeneId</th>
          <th>hugoGeneSymbol</th>
          <th>type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>672</td>
          <td>BRCA1</td>
          <td>protein-coding</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df3 = gns.get_aliases_of_gene("BRCA2")
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
          <td>FAD1</td>
        </tr>
        <tr>
          <th>1</th>
          <td>FANCD1</td>
        </tr>
        <tr>
          <th>2</th>
          <td>XRCC11</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df4 = gns.fetch_genes(gene_ids=["BRCA1","BRCA2"], gene_id_type = "HUGO_GENE_SYMBOL")
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
          <th>entrezGeneId</th>
          <th>hugoGeneSymbol</th>
          <th>type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>672</td>
          <td>BRCA1</td>
          <td>protein-coding</td>
        </tr>
        <tr>
          <th>1</th>
          <td>675</td>
          <td>BRCA2</td>
          <td>protein-coding</td>
        </tr>
      </tbody>
    </table>
    </div>


