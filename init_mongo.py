import os
import pymongo
from pymongo import MongoClient

def initialize_database():
    try:
        # Connect to the MongoDB server
        client = MongoClient(os.environ.get('MONGO_URI'))
        
        # Get the list of database names
        database_names = client.list_database_names()
        
        # Specify the name of the database you want to create
        database_name = os.environ.get('DJANGO_DB_NAME', 'attackflow')

        # Check if the database already exists
        if database_name not in database_names:
            # Create the database and any initial collections
            db = client[database_name]
            db.create_collection("users")
            db.create_collection("current_documents")
            db.create_collection("pending_documents")
            db.create_collection("legacy_documents")
            db.create_collection("rejected_documents")
            print(f"Database '{database_name}' created.")
        else:
            print(f"Database '{database_name}' already exists.")
            print("it has the following collections:\n", client[database_name].list_collection_names())
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("running init__py")
    initialize_database()