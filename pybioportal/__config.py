import os
from dotenv import load_dotenv
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
# Global variable
base_url = "https://www.cbioportal.org/api"

# Retrieve the API token from an environment variable
API_TOKEN = os.getenv('CBIOPORTAL_API_TOKEN')

#Raise an error if the API token is not set
if not API_TOKEN:
    raise ValueError("Please set the 'CBIOPORTAL_API_TOKEN' environment variable.")

# Setting base url
def configure_base_url(new_base_url=base_url):
    global base_url
    logger.info(f"Base URL updated to {new_base_url}")
    base_url = new_base_url 