import os
from dotenv import load_dotenv, find_dotenv
from datasets import load_dataset
import pandas as pd
from pydantic import ValidationError
from pymongo.mongo_client import MongoClient

from app.models import Listing

_ = load_dotenv(find_dotenv()) # read local .env file
MONGO_URI = os.environ.get("MONGO_URI")


dataset = load_dataset("MongoDB/airbnb_embeddings", streaming=True, split="train")
dataset = dataset.take(100)
dataset_df = pd.DataFrame(dataset)
records = dataset_df.to_dict(orient="records")


# To handle catch `NaT` values
for record in records:
    for key, value in record.items():
        # Check if the value is list-like; if so, process each element.
        if isinstance(value, list):
            processed_list = [None if pd.isnull(v) else v for v in value]
            record[key] = processed_list
        # For scalar values, continue as before.
        else:
            if pd.isnull(value):
                record[key] = None


try:
  # Convert each dictionary to a Movie instance
  listings = [Listing(**record).dict() for record in records]
  # Get an overview of a single datapoint
  print(listings[0].keys())
except ValidationError as e:
  print(e)

database_name = "airbnb_dataset"
collection_name = "listings_reviews"

def get_mongo_client(mongo_uri):
    """Establish connection to the MongoDB."""

    # gateway to interacting with a MongoDB database cluster
    client = MongoClient(mongo_uri, appname="devrel.deeplearningai.lesson1.python")
    print("Connection to MongoDB successful")
    return client

if not MONGO_URI:
    print("MONGO_URI not set in environment variables")

mongo_client = get_mongo_client(MONGO_URI)

# Pymongo client of database and collection
db = mongo_client.get_database(database_name)
collection = db.get_collection(collection_name)

# Delete any existing records in the collection
collection.delete_many({})

# The ingestion process might take a few minutes
collection.insert_many(listings)
print("Data ingestion into MongoDB completed")

