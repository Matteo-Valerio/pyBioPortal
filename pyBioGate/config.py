# Global variable
base_url = "https://www.cbioportal.org/api"

# Setting base url
def configure_base_url(new_base_url=base_url):
    global base_url
    base_url = new_base_url