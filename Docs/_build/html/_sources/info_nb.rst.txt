.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pybioportal.info import get_info
    get_info()




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
          <th>portalVersion</th>
          <th>dbVersion</th>
          <th>gitBranch</th>
          <th>gitCommitId</th>
          <th>gitCommitIdDescribe</th>
          <th>gitCommitIdDescribeShort</th>
          <th>gitCommitMessageFull</th>
          <th>gitCommitMessageShort</th>
          <th>gitCommitMessageUserEmail</th>
          <th>gitCommitMessageUserName</th>
          <th>gitDirty</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>5.4.7-dirty-SNAPSHOT</td>
          <td>2.13.1</td>
          <td>d4b06559c81a99911d620107113b2acf0e40523e</td>
          <td>d4b06559c81a99911d620107113b2acf0e40523e</td>
          <td>v5.4.7-dirty</td>
          <td>v5.4.7-dirty</td>
          <td>Merge pull request #10453 from cBioPortal/fron...</td>
          <td>Merge pull request #10453 from cBioPortal/fron...</td>
          <td>15748980+dippindots@users.noreply.github.com</td>
          <td>Gaofei Zhao</td>
          <td>True</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df = get_info()
    for column in df.columns:
        print(f'{column}: {df[column].to_string(index=False)}')
    


.. parsed-literal::

    portalVersion: 5.4.7-dirty-SNAPSHOT
    dbVersion: 2.13.1
    gitBranch: d4b06559c81a99911d620107113b2acf0e40523e
    gitCommitId: d4b06559c81a99911d620107113b2acf0e40523e
    gitCommitIdDescribe: v5.4.7-dirty
    gitCommitIdDescribeShort: v5.4.7-dirty
    gitCommitMessageFull: Merge pull request #10453 from cBioPortal/front...
    gitCommitMessageShort: Merge pull request #10453 from cBioPortal/front...
    gitCommitMessageUserEmail: 15748980+dippindots@users.noreply.github.com
    gitCommitMessageUserName: Gaofei Zhao
    gitDirty: True
    
