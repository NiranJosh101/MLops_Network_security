# Store code here for possible use later

from pymongo.mongo_client import MongoClient

# Connect to the mongodb database via the link below
uri = "mongodb+srv://niranjosh011:Admin100001@cluster0.tfxcqvh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)