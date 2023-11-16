.. raw:: html

  <hr>

.. raw:: html

    <head>
        <link rel="stylesheet" href="_static/css/notebook_cell_style.css" type="text/css">
    </head>     

Examples
^^^^^^^^

.. code:: ipython3

    from pyBioGate import mutations as mts

.. code:: ipython3

    df1 = mts.get_muts_in_mol_prof_by_sample_list_id(molecular_profile_id="brca_tcga_mutations", 
                                                     sample_list_id="brca_tcga_all", 
                                                     entrez_gene_id="672")
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
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>entrezGeneId</th>
          <th>studyId</th>
          <th>center</th>
          <th>mutationStatus</th>
          <th>validationStatus</th>
          <th>...</th>
          <th>proteinChange</th>
          <th>mutationType</th>
          <th>ncbiBuild</th>
          <th>variantType</th>
          <th>keyword</th>
          <th>chr</th>
          <th>variantAllele</th>
          <th>refseqMrnaId</th>
          <th>proteinPosStart</th>
          <th>proteinPosEnd</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1BMi1BNFMwLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BNFMwOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A2-A4S0-01</td>
          <td>TCGA-A2-A4S0</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>K50T</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 K50 missense</td>
          <td>17</td>
          <td>G</td>
          <td>NM_007294.3</td>
          <td>50</td>
          <td>50</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1FMi1BMUw5LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUw5OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1L9-01</td>
          <td>TCGA-E2-A1L9</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>S1027I</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 S1027 missense</td>
          <td>17</td>
          <td>A</td>
          <td>NM_007294.3</td>
          <td>1027</td>
          <td>1027</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1CSC1BMFdBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMFdBOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A0WA-01</td>
          <td>TCGA-BH-A0WA</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>X1559_splice</td>
          <td>Splice_Site</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 truncating</td>
          <td>17</td>
          <td>T</td>
          <td>NM_007294.3</td>
          <td>1559</td>
          <td>1559</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1FOS1BMU5DLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FOS1BMU5DOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E9-A1NC-01</td>
          <td>TCGA-E9-A1NC</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>Q139*</td>
          <td>Nonsense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 truncating</td>
          <td>17</td>
          <td>A</td>
          <td>NM_007294.3</td>
          <td>139</td>
          <td>139</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1DOC1BMTJULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTJUOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-C8-A12T-01</td>
          <td>TCGA-C8-A12T</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>D1344H</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 D1344 missense</td>
          <td>17</td>
          <td>G</td>
          <td>NM_007294.3</td>
          <td>1344</td>
          <td>1344</td>
        </tr>
        <tr>
          <th>5</th>
          <td>VENHQS1MTC1BNVlQLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1MTC1BNVlQOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-LL-A5YP-01</td>
          <td>TCGA-LL-A5YP</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>D96H</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 D96 missense</td>
          <td>17</td>
          <td>G</td>
          <td>NM_007294.3</td>
          <td>96</td>
          <td>96</td>
        </tr>
        <tr>
          <th>6</th>
          <td>VENHQS1BTy1BMUtSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTy1BMUtSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AO-A1KR-01</td>
          <td>TCGA-AO-A1KR</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>C644del</td>
          <td>In_Frame_Del</td>
          <td>GRCh37</td>
          <td>DEL</td>
          <td>BRCA1 644-644 deletion</td>
          <td>17</td>
          <td>-</td>
          <td>NM_007294.3</td>
          <td>644</td>
          <td>644</td>
        </tr>
        <tr>
          <th>7</th>
          <td>VENHQS1BMS1BMFNJLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNJOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A1-A0SI-01</td>
          <td>TCGA-A1-A0SI</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E9Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 E9 missense</td>
          <td>17</td>
          <td>G</td>
          <td>NM_007294.3</td>
          <td>9</td>
          <td>9</td>
        </tr>
        <tr>
          <th>8</th>
          <td>VENHQS1BTi1BMFhVLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTi1BMFhVOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AN-A0XU-01</td>
          <td>TCGA-AN-A0XU</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>G1788V</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 G1788 missense</td>
          <td>17</td>
          <td>A</td>
          <td>NM_007294.3</td>
          <td>1788</td>
          <td>1788</td>
        </tr>
        <tr>
          <th>9</th>
          <td>VENHQS1BMi1BMjVCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMjVCOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A2-A25B-01</td>
          <td>TCGA-A2-A25B</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E720*</td>
          <td>Nonsense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 truncating</td>
          <td>17</td>
          <td>A</td>
          <td>NM_007294.3</td>
          <td>720</td>
          <td>720</td>
        </tr>
        <tr>
          <th>10</th>
          <td>VENHQS1FVy1BMkZSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FVy1BMkZSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-EW-A2FR-01</td>
          <td>TCGA-EW-A2FR</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>D366N</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 D366 missense</td>
          <td>17</td>
          <td>T</td>
          <td>NM_007294.3</td>
          <td>366</td>
          <td>366</td>
        </tr>
        <tr>
          <th>11</th>
          <td>VENHQS1EOC1BMjdNLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1EOC1BMjdNOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-D8-A27M-01</td>
          <td>TCGA-D8-A27M</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>P1614Qfs*19</td>
          <td>Frame_Shift_Del</td>
          <td>GRCh37</td>
          <td>DEL</td>
          <td>BRCA1 truncating</td>
          <td>17</td>
          <td>-</td>
          <td>NM_007294.3</td>
          <td>1614</td>
          <td>1614</td>
        </tr>
        <tr>
          <th>12</th>
          <td>VENHQS1QRS1BNURFLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1QRS1BNURFOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-PE-A5DE-01</td>
          <td>TCGA-PE-A5DE</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E1419K</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>BRCA1 E1419 missense</td>
          <td>17</td>
          <td>T</td>
          <td>NM_007294.3</td>
          <td>1419</td>
          <td>1419</td>
        </tr>
      </tbody>
    </table>
    <p>13 rows × 25 columns</p>
    </div>



.. code:: ipython3

    df2a = mts.fetch_muts_in_mol_prof(molecular_profile_id="brca_tcga_mutations",
                                      entrez_gene_ids=["1005", "1020"],
                                      sample_ids = ["TCGA-AR-A1AR-01","TCGA-BH-A1EO-01"])                                                 
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
          <th>entrezGeneId</th>
          <th>studyId</th>
          <th>center</th>
          <th>mutationStatus</th>
          <th>validationStatus</th>
          <th>...</th>
          <th>proteinChange</th>
          <th>mutationType</th>
          <th>ncbiBuild</th>
          <th>variantType</th>
          <th>keyword</th>
          <th>chr</th>
          <th>variantAllele</th>
          <th>refseqMrnaId</th>
          <th>proteinPosStart</th>
          <th>proteinPosEnd</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>1005</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>R695Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>CDH7 R695 missense</td>
          <td>18</td>
          <td>A</td>
          <td>NM_004361.2</td>
          <td>695</td>
          <td>695</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>1020</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>V162L</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>CDK5 V162 missense</td>
          <td>7</td>
          <td>A</td>
          <td>NM_004935.3</td>
          <td>162</td>
          <td>162</td>
        </tr>
      </tbody>
    </table>
    <p>2 rows × 25 columns</p>
    </div>



.. code:: ipython3

    df2b = mts.fetch_muts_in_mol_prof(molecular_profile_id="brca_tcga_mutations", 
                                      entrez_gene_ids=["1005", "1020"],
                                      sample_list_id="brca_tcga_all")
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
          <th>entrezGeneId</th>
          <th>studyId</th>
          <th>center</th>
          <th>mutationStatus</th>
          <th>validationStatus</th>
          <th>...</th>
          <th>proteinChange</th>
          <th>mutationType</th>
          <th>ncbiBuild</th>
          <th>variantType</th>
          <th>keyword</th>
          <th>chr</th>
          <th>variantAllele</th>
          <th>refseqMrnaId</th>
          <th>proteinPosStart</th>
          <th>proteinPosEnd</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>1005</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>R695Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>CDH7 R695 missense</td>
          <td>18</td>
          <td>A</td>
          <td>NM_004361.2</td>
          <td>695</td>
          <td>695</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1PTC1BNUQ4LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1PTC1BNUQ4OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-OL-A5D8-01</td>
          <td>TCGA-OL-A5D8</td>
          <td>1005</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>S556*</td>
          <td>Nonsense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>CDH7 truncating</td>
          <td>18</td>
          <td>A</td>
          <td>NM_004361.2</td>
          <td>556</td>
          <td>556</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1EOC1BMUpMLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1EOC1BMUpMOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-D8-A1JL-01</td>
          <td>TCGA-D8-A1JL</td>
          <td>1005</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>G78A</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>CDH7 G78 missense</td>
          <td>18</td>
          <td>C</td>
          <td>NM_004361.2</td>
          <td>78</td>
          <td>78</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1BTi1BMDQ2LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTi1BMDQ2OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AN-A046-01</td>
          <td>TCGA-AN-A046</td>
          <td>1005</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>T178M</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>CDH7 T178 missense</td>
          <td>18</td>
          <td>T</td>
          <td>NM_004361.2</td>
          <td>178</td>
          <td>178</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1BTi1BMDQ2LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTi1BMDQ2OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AN-A046-01</td>
          <td>TCGA-AN-A046</td>
          <td>1005</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>R264Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>CDH7 R264 missense</td>
          <td>18</td>
          <td>A</td>
          <td>NM_004361.2</td>
          <td>264</td>
          <td>264</td>
        </tr>
        <tr>
          <th>5</th>
          <td>VENHQS1CSC1BMUVPLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMUVPOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A1EO-01</td>
          <td>TCGA-BH-A1EO</td>
          <td>1020</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>V162L</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>CDK5 V162 missense</td>
          <td>7</td>
          <td>A</td>
          <td>NM_004935.3</td>
          <td>162</td>
          <td>162</td>
        </tr>
        <tr>
          <th>6</th>
          <td>VENHQS1EOC1BMUpBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1EOC1BMUpBOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-D8-A1JA-01</td>
          <td>TCGA-D8-A1JA</td>
          <td>1020</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E101Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>CDK5 E101 missense</td>
          <td>7</td>
          <td>G</td>
          <td>NM_004935.3</td>
          <td>101</td>
          <td>101</td>
        </tr>
      </tbody>
    </table>
    <p>7 rows × 25 columns</p>
    </div>



.. code:: ipython3

    df3a = mts.fetch_muts_in_multiple_mol_profs(entrez_gene_ids=["672","675"], 
                                                molecular_profile_ids=["brca_tcga_mutations", "acc_tcga_mutations"])
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
          <th>uniqueSampleKey</th>
          <th>uniquePatientKey</th>
          <th>molecularProfileId</th>
          <th>sampleId</th>
          <th>patientId</th>
          <th>entrezGeneId</th>
          <th>studyId</th>
          <th>center</th>
          <th>mutationStatus</th>
          <th>validationStatus</th>
          <th>...</th>
          <th>proteinChange</th>
          <th>mutationType</th>
          <th>ncbiBuild</th>
          <th>variantType</th>
          <th>chr</th>
          <th>variantAllele</th>
          <th>refseqMrnaId</th>
          <th>proteinPosStart</th>
          <th>proteinPosEnd</th>
          <th>keyword</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1PUi1BNUxFLTAxOmFjY190Y2dh</td>
          <td>VENHQS1PUi1BNUxFOmFjY190Y2dh</td>
          <td>acc_tcga_mutations</td>
          <td>TCGA-OR-A5LE-01</td>
          <td>TCGA-OR-A5LE</td>
          <td>675</td>
          <td>acc_tcga</td>
          <td>bcgsc.ca</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>V733_L734insFFF</td>
          <td>In_Frame_Ins</td>
          <td>GRCh37</td>
          <td>INS</td>
          <td>13</td>
          <td>TCTTCTTCT</td>
          <td>NA</td>
          <td>733</td>
          <td>734</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1BMi1BNFMwLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BNFMwOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A2-A4S0-01</td>
          <td>TCGA-A2-A4S0</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>K50T</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>G</td>
          <td>NM_007294.3</td>
          <td>50</td>
          <td>50</td>
          <td>BRCA1 K50 missense</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1FMi1BMUw5LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUw5OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1L9-01</td>
          <td>TCGA-E2-A1L9</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>S1027I</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>A</td>
          <td>NM_007294.3</td>
          <td>1027</td>
          <td>1027</td>
          <td>BRCA1 S1027 missense</td>
        </tr>
        <tr>
          <th>3</th>
          <td>VENHQS1CSC1BMFdBLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMFdBOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A0WA-01</td>
          <td>TCGA-BH-A0WA</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>X1559_splice</td>
          <td>Splice_Site</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>T</td>
          <td>NM_007294.3</td>
          <td>1559</td>
          <td>1559</td>
          <td>BRCA1 truncating</td>
        </tr>
        <tr>
          <th>4</th>
          <td>VENHQS1FOS1BMU5DLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FOS1BMU5DOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E9-A1NC-01</td>
          <td>TCGA-E9-A1NC</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>Q139*</td>
          <td>Nonsense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>A</td>
          <td>NM_007294.3</td>
          <td>139</td>
          <td>139</td>
          <td>BRCA1 truncating</td>
        </tr>
        <tr>
          <th>5</th>
          <td>VENHQS1DOC1BMTJULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTJUOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-C8-A12T-01</td>
          <td>TCGA-C8-A12T</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>D1344H</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>G</td>
          <td>NM_007294.3</td>
          <td>1344</td>
          <td>1344</td>
          <td>BRCA1 D1344 missense</td>
        </tr>
        <tr>
          <th>6</th>
          <td>VENHQS1MTC1BNVlQLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1MTC1BNVlQOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-LL-A5YP-01</td>
          <td>TCGA-LL-A5YP</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>D96H</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>G</td>
          <td>NM_007294.3</td>
          <td>96</td>
          <td>96</td>
          <td>BRCA1 D96 missense</td>
        </tr>
        <tr>
          <th>7</th>
          <td>VENHQS1BTy1BMUtSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTy1BMUtSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AO-A1KR-01</td>
          <td>TCGA-AO-A1KR</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>C644del</td>
          <td>In_Frame_Del</td>
          <td>GRCh37</td>
          <td>DEL</td>
          <td>17</td>
          <td>-</td>
          <td>NM_007294.3</td>
          <td>644</td>
          <td>644</td>
          <td>BRCA1 644-644 deletion</td>
        </tr>
        <tr>
          <th>8</th>
          <td>VENHQS1BMS1BMFNJLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMS1BMFNJOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A1-A0SI-01</td>
          <td>TCGA-A1-A0SI</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E9Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>G</td>
          <td>NM_007294.3</td>
          <td>9</td>
          <td>9</td>
          <td>BRCA1 E9 missense</td>
        </tr>
        <tr>
          <th>9</th>
          <td>VENHQS1BTi1BMFhVLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTi1BMFhVOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AN-A0XU-01</td>
          <td>TCGA-AN-A0XU</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>G1788V</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>A</td>
          <td>NM_007294.3</td>
          <td>1788</td>
          <td>1788</td>
          <td>BRCA1 G1788 missense</td>
        </tr>
        <tr>
          <th>10</th>
          <td>VENHQS1BMi1BMjVCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMjVCOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A2-A25B-01</td>
          <td>TCGA-A2-A25B</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E720*</td>
          <td>Nonsense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>A</td>
          <td>NM_007294.3</td>
          <td>720</td>
          <td>720</td>
          <td>BRCA1 truncating</td>
        </tr>
        <tr>
          <th>11</th>
          <td>VENHQS1FVy1BMkZSLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FVy1BMkZSOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-EW-A2FR-01</td>
          <td>TCGA-EW-A2FR</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>D366N</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>T</td>
          <td>NM_007294.3</td>
          <td>366</td>
          <td>366</td>
          <td>BRCA1 D366 missense</td>
        </tr>
        <tr>
          <th>12</th>
          <td>VENHQS1EOC1BMjdNLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1EOC1BMjdNOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-D8-A27M-01</td>
          <td>TCGA-D8-A27M</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>P1614Qfs*19</td>
          <td>Frame_Shift_Del</td>
          <td>GRCh37</td>
          <td>DEL</td>
          <td>17</td>
          <td>-</td>
          <td>NM_007294.3</td>
          <td>1614</td>
          <td>1614</td>
          <td>BRCA1 truncating</td>
        </tr>
        <tr>
          <th>13</th>
          <td>VENHQS1QRS1BNURFLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1QRS1BNURFOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-PE-A5DE-01</td>
          <td>TCGA-PE-A5DE</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E1419K</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>T</td>
          <td>NM_007294.3</td>
          <td>1419</td>
          <td>1419</td>
          <td>BRCA1 E1419 missense</td>
        </tr>
        <tr>
          <th>14</th>
          <td>VENHQS1BOC1BMDdJLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BOC1BMDdJOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A8-A07I-01</td>
          <td>TCGA-A8-A07I</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>D1355Y</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>T</td>
          <td>NA</td>
          <td>1355</td>
          <td>1355</td>
          <td>BRCA2 D1355 missense</td>
        </tr>
        <tr>
          <th>15</th>
          <td>VENHQS1EOC1BMUpQLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1EOC1BMUpQOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-D8-A1JP-01</td>
          <td>TCGA-D8-A1JP</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>L1965Ffs*39</td>
          <td>Frame_Shift_Del</td>
          <td>GRCh37</td>
          <td>DEL</td>
          <td>13</td>
          <td>-</td>
          <td>NA</td>
          <td>1965</td>
          <td>1965</td>
          <td>BRCA2 truncating</td>
        </tr>
        <tr>
          <th>16</th>
          <td>VENHQS1BOC1BMDhMLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BOC1BMDhMOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A8-A08L-01</td>
          <td>TCGA-A8-A08L</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>X2602_splice</td>
          <td>Splice_Site</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>A</td>
          <td>NA</td>
          <td>2602</td>
          <td>2602</td>
          <td>BRCA2 truncating</td>
        </tr>
        <tr>
          <th>17</th>
          <td>VENHQS1EOC1BMjdHLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1EOC1BMjdHOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-D8-A27G-01</td>
          <td>TCGA-D8-A27G</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E2175Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>C</td>
          <td>NA</td>
          <td>2175</td>
          <td>2175</td>
          <td>BRCA2 E2175 missense</td>
        </tr>
        <tr>
          <th>18</th>
          <td>VENHQS1BTi1BMEFULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTi1BMEFUOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AN-A0AT-01</td>
          <td>TCGA-AN-A0AT</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E2650Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>C</td>
          <td>NA</td>
          <td>2650</td>
          <td>2650</td>
          <td>BRCA2 E2650 missense</td>
        </tr>
        <tr>
          <th>19</th>
          <td>VENHQS1BMi1BMFQwLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMFQwOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A2-A0T0-01</td>
          <td>TCGA-A2-A0T0</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>L2926*</td>
          <td>Nonsense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>G</td>
          <td>NA</td>
          <td>2926</td>
          <td>2926</td>
          <td>BRCA2 truncating</td>
        </tr>
        <tr>
          <th>20</th>
          <td>VENHQS1DOC1BMTJULTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1DOC1BMTJUOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-C8-A12T-01</td>
          <td>TCGA-C8-A12T</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E3177Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>C</td>
          <td>NA</td>
          <td>3177</td>
          <td>3177</td>
          <td>BRCA2 E3177 missense</td>
        </tr>
        <tr>
          <th>21</th>
          <td>VENHQS1BOC1BMDhCLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BOC1BMDhCOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A8-A08B-01</td>
          <td>TCGA-A8-A08B</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>V1270del</td>
          <td>In_Frame_Del</td>
          <td>GRCh37</td>
          <td>DEL</td>
          <td>13</td>
          <td>-</td>
          <td>NA</td>
          <td>1268</td>
          <td>1270</td>
          <td>BRCA2 1270-1270 deletion</td>
        </tr>
        <tr>
          <th>22</th>
          <td>VENHQS1BUi1BMUFJLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BUi1BMUFJOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AR-A1AI-01</td>
          <td>TCGA-AR-A1AI</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>R2336C</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>T</td>
          <td>NA</td>
          <td>2336</td>
          <td>2336</td>
          <td>BRCA2 R2336 missense</td>
        </tr>
        <tr>
          <th>23</th>
          <td>VENHQS1CSC1BMEhGLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1CSC1BMEhGOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-BH-A0HF-01</td>
          <td>TCGA-BH-A0HF</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>S879F</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>T</td>
          <td>NA</td>
          <td>879</td>
          <td>879</td>
          <td>BRCA2 S879 missense</td>
        </tr>
        <tr>
          <th>24</th>
          <td>VENHQS1BQy1BMjNILTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BQy1BMjNIOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AC-A23H-01</td>
          <td>TCGA-AC-A23H</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>D687H</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>C</td>
          <td>NA</td>
          <td>687</td>
          <td>687</td>
          <td>BRCA2 D687 missense</td>
        </tr>
        <tr>
          <th>25</th>
          <td>VENHQS1BQy1BMjNILTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BQy1BMjNIOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AC-A23H-01</td>
          <td>TCGA-AC-A23H</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>D1033H</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>C</td>
          <td>NA</td>
          <td>1033</td>
          <td>1033</td>
          <td>BRCA2 D1033 missense</td>
        </tr>
        <tr>
          <th>26</th>
          <td>VENHQS1FVy1BMVBFLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FVy1BMVBFOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-EW-A1PE-01</td>
          <td>TCGA-EW-A1PE</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E1158Q</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>C</td>
          <td>NA</td>
          <td>1158</td>
          <td>1158</td>
          <td>BRCA2 E1158 missense</td>
        </tr>
        <tr>
          <th>27</th>
          <td>VENHQS1FVy1BMVBFLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FVy1BMVBFOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-EW-A1PE-01</td>
          <td>TCGA-EW-A1PE</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>K1191N</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>C</td>
          <td>NA</td>
          <td>1191</td>
          <td>1191</td>
          <td>BRCA2 K1191 missense</td>
        </tr>
        <tr>
          <th>28</th>
          <td>VENHQS1BMi1BMjVGLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BMjVGOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A2-A25F-01</td>
          <td>TCGA-A2-A25F</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>Y3049S</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>C</td>
          <td>NA</td>
          <td>3049</td>
          <td>3049</td>
          <td>BRCA2 Y3049 missense</td>
        </tr>
        <tr>
          <th>29</th>
          <td>VENHQS1BTy1BMTI0LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTy1BMTI0OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AO-A124-01</td>
          <td>TCGA-AO-A124</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>C3304S</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>C</td>
          <td>NA</td>
          <td>3304</td>
          <td>3304</td>
          <td>BRCA2 C3304 missense</td>
        </tr>
        <tr>
          <th>30</th>
          <td>VENHQS1BTi1BMDQ2LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BTi1BMDQ2OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-AN-A046-01</td>
          <td>TCGA-AN-A046</td>
          <td>675</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>E3342K</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>13</td>
          <td>A</td>
          <td>NA</td>
          <td>3342</td>
          <td>3342</td>
          <td>BRCA2 E3342 missense</td>
        </tr>
      </tbody>
    </table>
    <p>31 rows × 27 columns</p>
    </div>



.. code:: ipython3

    df3b = mts.fetch_muts_in_multiple_mol_profs(entrez_gene_ids=["672","675"], 
                                                sample_molecular_identifiers=[
                                                            {"molecular_profile_id": "brca_tcga_mutations", 
                                                             "sample_ids": ["TCGA-A2-A4S0-01","TCGA-E2-A1L9-01"]},
                                                            {"molecular_profile_id": "acc_tcga_mutations", 
                                                             "sample_ids": ["TCGA-OR-A5LE-01"]}
                                                            ])
    df3b                                                    




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
          <th>entrezGeneId</th>
          <th>studyId</th>
          <th>center</th>
          <th>mutationStatus</th>
          <th>validationStatus</th>
          <th>...</th>
          <th>proteinChange</th>
          <th>mutationType</th>
          <th>ncbiBuild</th>
          <th>variantType</th>
          <th>chr</th>
          <th>variantAllele</th>
          <th>refseqMrnaId</th>
          <th>proteinPosStart</th>
          <th>proteinPosEnd</th>
          <th>keyword</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>VENHQS1PUi1BNUxFLTAxOmFjY190Y2dh</td>
          <td>VENHQS1PUi1BNUxFOmFjY190Y2dh</td>
          <td>acc_tcga_mutations</td>
          <td>TCGA-OR-A5LE-01</td>
          <td>TCGA-OR-A5LE</td>
          <td>675</td>
          <td>acc_tcga</td>
          <td>bcgsc.ca</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>V733_L734insFFF</td>
          <td>In_Frame_Ins</td>
          <td>GRCh37</td>
          <td>INS</td>
          <td>13</td>
          <td>TCTTCTTCT</td>
          <td>NA</td>
          <td>733</td>
          <td>734</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>VENHQS1FMi1BMUw5LTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1FMi1BMUw5OmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-E2-A1L9-01</td>
          <td>TCGA-E2-A1L9</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>S1027I</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>A</td>
          <td>NM_007294.3</td>
          <td>1027</td>
          <td>1027</td>
          <td>BRCA1 S1027 missense</td>
        </tr>
        <tr>
          <th>2</th>
          <td>VENHQS1BMi1BNFMwLTAxOmJyY2FfdGNnYQ</td>
          <td>VENHQS1BMi1BNFMwOmJyY2FfdGNnYQ</td>
          <td>brca_tcga_mutations</td>
          <td>TCGA-A2-A4S0-01</td>
          <td>TCGA-A2-A4S0</td>
          <td>672</td>
          <td>brca_tcga</td>
          <td>genome.wustl.edu</td>
          <td>Somatic</td>
          <td>Untested</td>
          <td>...</td>
          <td>K50T</td>
          <td>Missense_Mutation</td>
          <td>GRCh37</td>
          <td>SNP</td>
          <td>17</td>
          <td>G</td>
          <td>NM_007294.3</td>
          <td>50</td>
          <td>50</td>
          <td>BRCA1 K50 missense</td>
        </tr>
      </tbody>
    </table>
    <p>3 rows × 27 columns</p>
    </div>


