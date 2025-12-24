import certifi
import os
import sys
import json
import certifi
import pandas as pd
from dotenv import load_dotenv
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


load_dotenv()


MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


ca = certifi.where()


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(inplace=True, drop=True)
            records = list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def instert_to_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.database = self.client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return f"{len(self.records)} record was inserted successfully"

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e


if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "NetworkSecurity"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.instert_to_mongodb(
        records=records, database=DATABASE, collection=Collection
    )
    print(no_of_records)
