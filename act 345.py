#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import time
import requests
import pandas as pd
from pprint import pprint as pp
from asyncio.windows_events import NULL


# In[ ]:


def ch_gen(nameStartsWith,  hash_ , API_key):   #giving default value as null helps us in giving a clearer error message to the user



    address="http://gateway.marvel.com/v1/public/characters"   #url



    params={"apikey":API_key,"hash":hash_,"ts":int(time()),"limit":100,"nameStartsWith":nameStartsWith} #define all the parameters and keys
    
    response=requests.get(address,params) #we are using url alongwith api key(public) as well as hash key and also by inducing the parameters nameStartswith and limit
    print(response.json)    



    df = pd.json_normalize(response.json(), record_path=['data', 'results'])
    
    return df


# In[ ]:


api_url = "http://gateway.marvel.com/v1/public/"
public_key = input("enter your public key:")
private_key = input("enter your private key:")
resource = "characters"

limit = 100


# In[ ]:


ts = str(int(time()))
hash_param = ts+private_key+public_key
hash_result = hashlib.md5(hash_param.encode())

df = ch_gen(nameStartsWith = "Spider", hash_ = hash_result.hexdigest(), API_key = public_key)


# In[ ]:


#activity 4 
def ch_filter(df1,col,filter_condition):
    return df1.query(col+filter_condition)   #optimal method for the above code.

# def ch_filter1(df1,col,filter_condition):
#     total_condition = col+filter_condition;
#     res = (df1.query(total_condition));  #code to define and convert to df for a filter conditionbased on selected column and the condition on that column
#     return res 

result2= ch_filter(df1=result, col='name',filter_condition='.str.startswith("A")')
print("-----ACTIVITY: 4-----")
print("Result: Characters Starting with 'A'",result2)


# In[ ]:





# In[ ]:




