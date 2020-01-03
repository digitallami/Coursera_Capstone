#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random # library for random number generation
import numpy as np # library for vectorized computation
import pandas as pd # library to process data as dataframes
import requests

import matplotlib.pyplot as plt # plotting library
# backend for rendering plots within the browser
get_ipython().run_line_magic('matplotlib', 'inline')

from bs4 import BeautifulSoup
from sklearn.cluster import KMeans 
from sklearn.datasets.samples_generator import make_blobs

import bs4 as bs
import urllib.request

print('Libraries imported.')


# # Start Notebook, Scrape Wiki Page, Create Dateframe

# In[2]:


source = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').read()
soup = bs.BeautifulSoup(source,'html.parser')

table = soup.find('table')
table_rows = table.find_all('tr')

l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text.strip() for tr in td if tr.text.strip()]
    if row:
        l.append(row)


# In[3]:


df = pd.DataFrame(l, columns=["PostalCode", "Borough", "Neighbourhood"])
df.head(12)


# Process Only those with Assigned Borough

# In[4]:


df = df[df.Borough != 'Not assigned']
df.head(12)


# In[5]:


df = df.groupby(['PostalCode', 'Borough']).agg(', '.join)
df = df.reset_index()
df.head(12)


# For cells without assigned neighbourhood, neighbourhood = assigned borough

# In[6]:


df.loc[df['Neighbourhood']=='Not assigned', ['Neighbourhood']] = 'Queen\'s Park'
df.head(12)


# In[7]:


df.shape


# In[ ]:




