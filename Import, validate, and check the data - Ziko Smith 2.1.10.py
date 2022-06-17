#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
movies = pd.read_excel('movies.xlsx')
movies.head()


# In[2]:


ott = pd.read_csv('ott.csv')


# In[3]:


ott.head()


# In[4]:


print(movies.shape)
print(ott.shape)


# In[6]:


print(movies.head())
print(ott.head())


# In[7]:


print(movies.tail())


print(ott.tail())


# In[8]:


print(movies.dtypes)

print(ott.dtypes)


# In[ ]:




