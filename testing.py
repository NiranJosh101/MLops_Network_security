import pymongo
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

MONGODB_DB_URL = "mongodb+srv://niranjosh011:Admin100001@cluster0.tfxcqvh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(MONGODB_DB_URL)
db = client["NETWORKAI"]
collection = db["NetworkData"]

# Check count
print("✅ Document count:", collection.count_documents({}))

# Load a sample
df = pd.DataFrame(list(collection.find().limit(5)))

# Clean and print
if "_id" in df.columns:
    df.drop(columns=["_id"], inplace=True)

df.replace({"na": np.nan}, inplace=True)

print("📦 Sample from MongoDB:")
print(df.head())
print("✅ Shape:", df.shape)
