from wsgiref.headers import tspecials
import requests
import pandas as pd
from time import time
import hashlib
import pandas as pd
import string

class utils:
    
    def __init__(self, public_key, private_key, address, hash):
        self.public_key = public_key
        self.private_key = private_key
        self.address = address
        self.hash = hash


    def create_hash(self):
        ts = '1'
        hash_param = ts + self.private_key + self.public_key
        hash_result = hashlib.md5(hash_param.encode()).hexdigest()

        return hash_result


    def authorization(self):
        """
        arguments: web service endpoint, public key, private key
        computes hash and returns the complete address and parameter dictionary
        """

        limit = 100 

        ts = '1'
        hash_param = ts + self.private_key + self.public_key
        hash_result = hashlib.md5(hash_param.encode())

        params = {"apikey": self.public_key, 
                    "ts": '1', 
                    "hash": hash_result.hexdigest(),
                    "limit": limit}

        return params

    
    def dataframe(self, params):
        """
        arguments: parameters dictionary, web api address
        returns a dataframe
        """
        start_char = list(string.ascii_lowercase + string.digits)
        start_char.remove('0')

        df = pd.DataFrame()

        for letter in start_char :
            print(letter)
            params["nameStartsWith"] = letter
            print(params)
            response = requests.get(self.address, params)
            print(response.json)
            temp_df = pd.json_normalize(response.json(), record_path=['data', 'results'])
            df = pd.concat([df, temp_df], ignore_index=True)
        
        df.drop(['modified', "resourceURI", "urls", "thumbnail.path", "thumbnail.extension", "comics.collectionURI", 
                        "series.items", "stories.collectionURI", "stories.items", "events.collectionURI", "events.items",
                        "comics.items", "series.collectionURI", "comics.returned", "series.returned", "stories.returned", 
                        "events.returned"], 
                    axis=1, inplace=True)
        return df

    
    def get_df(self, namestart):
        
        """
        returns a dataframe where character name starts with a specific string
        """
        try:
            params = {"apikey": self.public_key, "ts": '1', 
                    "hash": self.hash, "nameStartsWith": namestart,
                    "limit" : 100}

            response = requests.get(self.address, params)
            print(response.json)
            df = pd.json_normalize(response.json(), record_path=['data','results'])

            df.drop(['modified', "resourceURI", "urls", "thumbnail.path", "thumbnail.extension", "comics.collectionURI", 
                        "series.items", "stories.collectionURI", "stories.items", "events.collectionURI", "events.items",
                        "comics.items", "series.collectionURI", "comics.returned", "series.returned", "stories.returned", 
                        "events.returned"], 
                    axis=1, inplace=True)
            return df
        except:
            print("Hash and/or API key is incorrect")


    def filter_data(self, df, column, filter):

        """
        filters data based on column and filter provided. returns a dataframe
        """

        return df.query(column + filter)

    
