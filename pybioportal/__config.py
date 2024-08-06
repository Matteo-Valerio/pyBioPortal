<<<<<<< HEAD
import os

base_url = "https://www.cbioportal.org/api"
api_token = None

def configure_base_url(new_base_url):
    """
    Configure the base URL for the API.
    
    :param new_base_url: The new base URL to be set.
    """
    global base_url
    base_url = new_base_url

def set_api_token(token):
    """
    Set the API token for authentication.
    
    :param token: The API token to be set.
    """
    global api_token
    api_token = token

def get_headers():
    """
    Get the headers for the API request, including the API token.
    
    :returns: A dictionary of headers.
    :raises ValueError: If the API token is not set.
    """
    global api_token
    if not api_token:
        api_token = os.getenv("CBIOPORTAL_API_TOKEN")
    if not api_token:
        raise ValueError("API token not found. Please set the CBIOPORTAL_API_TOKEN environment variable or use set_api_token() function.")
    return {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}
=======
# Global variable
base_url = "https://www.cbioportal.org/api"

# Setting base url
def configure_base_url(new_base_url=base_url):
    global base_url
    base_url = new_base_url
>>>>>>> origin/master
