import pymongo
from django.conf import settings

# this create the connection between the mongo and django
def create_mongo_client():
    MONGO_URI = settings.MONGO_URI
    return pymongo.MongoClient(MONGO_URI)

# define CRUD functions
# Retrieve documents from a collection
def get_documents(collection_name, query={}):
    client = create_mongo_client()
    db = client[settings.MONGO_DB_NAME]
    collection = db[collection_name]
    
    # Perform a query to retrieve documents
    documents = list(collection.find(query))
    client.close()
    return documents

# Update a document in a collection
def update_document(collection_name, document_id, update_data):
    client = create_mongo_client()
    db = client[settings.MONGO_DB_NAME]
    collection = db[collection_name]
    
    # Update the document
    result = collection.update_one({"_id": document_id}, {"$set": update_data})
    client.close()
    
    return result

# Delete a document from a collection
def delete_document(collection_name, document_id):
    client = create_mongo_client()
    db = client[settings.MONGO_DB_NAME]
    collection = db[collection_name]
    
    # Delete the document
    result = collection.delete_one({"_id": document_id})
    client.close()
    
    return result