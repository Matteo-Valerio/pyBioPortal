# Variabile comune per l'URL di base
base_url = "https://www.cbioportal.org/api"

# Funzione di configurazione per l'URL di base
def configure_base_url(new_base_url=base_url):
    global base_url
    base_url = new_base_url