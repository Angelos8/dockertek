
from .mongo_utils import create_mongo_client

# Create the MongoDB client at Django startup
mongo_client = create_mongo_client()