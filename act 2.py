#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json


# In[ ]:


import hashlib
from time import time 


# In[ ]:


public = "93c09fe4da776c46ae95a1c0c804d923"
address= "http://gateway.marvel.com/v1/public/characters"


# In[ ]:


ts= str(int(time()))
public_key = input ()
private_key =input()
hash = ts + private_key + public_key
hash_result = hashlib.md5(hash.encode())


# In[ ]:


api_url = "http://gateway.marvel.com/v1/public/"
public_key = input()
private_key = input()
resource = "characters"
limit = 100
ts = str(int(time()))

hash_param = ts+private_key+public_key

hash_result = hashlib.md5(hash_param.encode())

address = api_url + resource

param = {"apikey": '93c09fe4da776c46ae95a1c0c804d923',

            "ts": int(time()),

            "hash": hash_result.hexdigest(),

            "limit": limit}


# In[ ]:


df = pd.DataFrame()
import string

start_char = list(string.ascii_lowercase + string.digits)

start_char.remove('0')

for letter in start_char :

    param["nameStartsWith"] = letter

    response = requests.get(address, param)

    temp_df = pd.json_normalize(response.json(), record_path=['data', 'results'])

    df = pd.concat([df, temp_df])

    del param["nameStartsWith"]


# In[ ]:





# In[ ]:





# In[ ]:




