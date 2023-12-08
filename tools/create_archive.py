import tarfile
import os
from conf_build import vVERSION

def crea_tar_gz(nome_file_output, cartelle, file_da_aggiungere):
    with tarfile.open(nome_file_output, "w:gz") as tar:
        # Aggiungi cartelle al file tar.gz
        for cartella in cartelle:
            tar.add(cartella, arcname=os.path.basename(cartella))

        # Aggiungi file al file tar.gz
        for file in file_da_aggiungere:
            tar.add(file, arcname=os.path.basename(file))

if __name__ == "__main__":
    # Definisci le cartelle e i file da includere nel file tar.gz
    cartelle_da_aggiungere = ["../pybioportal"]
    file_da_aggiungere = ["../setup.py", "../LICENSE.txt", "../README.md"]

    # Nome del file tar.gz da creare
    nome_file_output = f"../archive/pybioportal-{vVERSION}.tar.gz"

    # Crea il file tar.gz
    crea_tar_gz(nome_file_output, cartelle_da_aggiungere, file_da_aggiungere)
