import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi # test certify our requests, so http flags the request as legit basically
ca=certifi.where() # store the trusted certificate authories.

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging



class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def cv_to_json_converter(self,file_path):
        try:

            # Read data from source
            data=pd.read_csv(file_path)

            # Drop initial dataset index
            data.reset_index(drop=True, inplace=True)

            # convert table formated dataset into json to store in mongo db
            records=list(json.loads(data.T.to_json()).values())
            return records
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            # create a 'client' so I can connect to the mongodb
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        


# Excute the ETL pipeline

if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="NETWORKAI"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)