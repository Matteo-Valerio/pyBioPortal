.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioPortal import copy_number_segment as cns

.. code:: ipython3

    df1a = cns.fetch_copy_number_segments(sample_study_ids=[
                                                  {"sample_ids": ["P-0000004-T01-IM3", "P-0000950-T01-IM3"],  "study_id": "msk_met_2021"},
                                                  {"sample_ids": ["TCGA-5T-A9QA-01", "TCGA-A1-A0SB-01"], "study_id": "brca_tcga"}
                                            ])
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
          <th>patientId</th>
          <th>start</th>
          <th>end</th>
          <th>segmentMean</th>
          <th>studyId</th>
          <th>sampleId</th>
          <th>chromosome</th>
          <th>numberOfProbes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>3218610</td>
          <td>247813706</td>
          <td>0.0034</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>1</td>
          <td>129072</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>484222</td>
          <td>174313755</td>
          <td>0.0014</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>2</td>
          <td>92446</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>174314142</td>
          <td>174314161</td>
          <td>-1.2680</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>2</td>
          <td>2</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>174315778</td>
          <td>194887369</td>
          <td>0.0019</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>2</td>
          <td>10897</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>194888052</td>
          <td>194892814</td>
          <td>-0.9361</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>2</td>
          <td>4</td>
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
        </tr>
        <tr>
          <th>443</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>36164670</td>
          <td>37954722</td>
          <td>0.3705</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>21</td>
          <td>11</td>
        </tr>
        <tr>
          <th>444</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>39625779</td>
          <td>45660694</td>
          <td>0.0544</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>21</td>
          <td>48</td>
        </tr>
        <tr>
          <th>445</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>19053406</td>
          <td>49370834</td>
          <td>-0.2394</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>22</td>
          <td>101</td>
        </tr>
        <tr>
          <th>446</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>451142</td>
          <td>1331488</td>
          <td>-0.5502</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>X</td>
          <td>7</td>
        </tr>
        <tr>
          <th>447</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>3085464</td>
          <td>149924738</td>
          <td>0.3045</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>X</td>
          <td>312</td>
        </tr>
      </tbody>
    </table>
    <p>448 rows × 10 columns</p>
    </div>



.. code:: ipython3

    df1b = cns.fetch_copy_number_segments(sample_study_ids=[
                                                  {"sample_ids": ["P-0000004-T01-IM3", "P-0000950-T01-IM3"],  "study_id": "msk_met_2021"},
                                                  {"sample_ids": ["TCGA-5T-A9QA-01", "TCGA-A1-A0SB-01"], "study_id": "brca_tcga"}
                                            ], chromosome="5")
    df1b.head(10)




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
          <th>patientId</th>
          <th>start</th>
          <th>end</th>
          <th>segmentMean</th>
          <th>studyId</th>
          <th>sampleId</th>
          <th>chromosome</th>
          <th>numberOfProbes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>914233</td>
          <td>31655645</td>
          <td>-0.0041</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>5</td>
          <td>18310</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>31656726</td>
          <td>31656768</td>
          <td>-1.7983</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>5</td>
          <td>2</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>31657098</td>
          <td>53873836</td>
          <td>-0.0002</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>5</td>
          <td>9892</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>53873994</td>
          <td>53874176</td>
          <td>-1.5816</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>5</td>
          <td>2</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1BMS1BMFNCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNCOmJyY2FfdGNnYQ</td>
          <td>TCGA-A1-A0SB</td>
          <td>53875569</td>
          <td>180360469</td>
          <td>0.0025</td>
          <td>brca_tcga</td>
          <td>TCGA-A1-A0SB-01</td>
          <td>5</td>
          <td>72240</td>
        </tr>
        <tr>
          <th>5</th>
          <td>VENHQS01VC1BOVFBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>914233</td>
          <td>111111798</td>
          <td>0.0329</td>
          <td>brca_tcga</td>
          <td>TCGA-5T-A9QA-01</td>
          <td>5</td>
          <td>58513</td>
        </tr>
        <tr>
          <th>6</th>
          <td>VENHQS01VC1BOVFBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>111112994</td>
          <td>111119490</td>
          <td>-1.0722</td>
          <td>brca_tcga</td>
          <td>TCGA-5T-A9QA-01</td>
          <td>5</td>
          <td>4</td>
        </tr>
        <tr>
          <th>7</th>
          <td>VENHQS01VC1BOVFBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>111119554</td>
          <td>112443378</td>
          <td>0.0489</td>
          <td>brca_tcga</td>
          <td>TCGA-5T-A9QA-01</td>
          <td>5</td>
          <td>1080</td>
        </tr>
        <tr>
          <th>8</th>
          <td>VENHQS01VC1BOVFBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>112450364</td>
          <td>112450424</td>
          <td>-1.4587</td>
          <td>brca_tcga</td>
          <td>TCGA-5T-A9QA-01</td>
          <td>5</td>
          <td>2</td>
        </tr>
        <tr>
          <th>9</th>
          <td>VENHQS01VC1BOVFBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS01VC1BOVFBOmJyY2FfdGNnYQ</td>
          <td>TCGA-5T-A9QA</td>
          <td>112453010</td>
          <td>116143516</td>
          <td>0.0538</td>
          <td>brca_tcga</td>
          <td>TCGA-5T-A9QA-01</td>
          <td>5</td>
          <td>2225</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df2 = cns.get_copy_number_segments_in_sample_in_study(study_id="msk_met_2021", sample_id="P-0000950-T01-IM3")
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
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>patientId</th>
          <th>start</th>
          <th>end</th>
          <th>segmentMean</th>
          <th>studyId</th>
          <th>sampleId</th>
          <th>chromosome</th>
          <th>numberOfProbes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>2488138</td>
          <td>245977996</td>
          <td>-0.2332</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>1</td>
          <td>545</td>
        </tr>
        <tr>
          <th>1</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>104375092</td>
          <td>104389868</td>
          <td>-0.5508</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>10</td>
          <td>5</td>
        </tr>
        <tr>
          <th>2</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>1510047</td>
          <td>104359246</td>
          <td>-0.2373</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>10</td>
          <td>113</td>
        </tr>
        <tr>
          <th>3</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>105517162</td>
          <td>134199067</td>
          <td>-0.1375</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>10</td>
          <td>34</td>
        </tr>
        <tr>
          <th>4</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>67198913</td>
          <td>68758509</td>
          <td>-0.4173</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>11</td>
          <td>12</td>
        </tr>
        <tr>
          <th>5</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>532696</td>
          <td>67197032</td>
          <td>-0.0058</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>11</td>
          <td>91</td>
        </tr>
        <tr>
          <th>6</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>69069538</td>
          <td>133495556</td>
          <td>0.0651</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>11</td>
          <td>235</td>
        </tr>
        <tr>
          <th>7</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>394725</td>
          <td>133263871</td>
          <td>0.2584</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>12</td>
          <td>372</td>
        </tr>
        <tr>
          <th>8</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>21004738</td>
          <td>111119077</td>
          <td>0.3586</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>13</td>
          <td>207</td>
        </tr>
        <tr>
          <th>9</th>
          <td>UC0wMDAwOTUwLVQwMS1JTTM6bXNrX21ldF8yMDIx</td>
          <td>UC0wMDAwOTUwOm1za19tZXRfMjAyMQ</td>
          <td>P-0000950</td>
          <td>38055061</td>
          <td>38068061</td>
          <td>0.5235</td>
          <td>msk_met_2021</td>
          <td>P-0000950-T01-IM3</td>
          <td>14</td>
          <td>5</td>
        </tr>
      </tbody>
    </table>
    </div>


