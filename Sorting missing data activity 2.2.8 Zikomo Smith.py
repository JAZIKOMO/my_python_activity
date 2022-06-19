#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
ott = pd.read_csv('ott.csv')


# In[9]:


import pandas as pd
movies = pd.read_excel('movies.xlsx')


# In[10]:


movies


# In[11]:


# Determine the sum of missing values
movies['Age'].isnull().sum()


# In[12]:


movies['Age'][movies['Age'].isna()] = "Others"


# In[15]:


movies


# In[16]:


movies['Directors'][movies['Directors'].isna()] = "Others"

movies['Genres'][movies['Genres'].isna()] = "Others"

movies['Country'][movies['Country'].isna()] = "Others"

movies['Language'][movies['Language'].isna()] = "Others"

movies


# In[17]:


print(movies['IMDb'].isnull().sum())

print(movies['Rotten Tomatoes'].isnull().sum())


# In[18]:


movies['IMDb'].fillna(movies['IMDb'].mean(),inplace=True)

movies['Rotten Tomatoes'].fillna(movies['Rotten Tomatoes'].mean(),inplace=True)


# In[19]:


print(movies['IMDb'].isnull().sum())

print(movies['Rotten Tomatoes'].isnull().sum())


# In[ ]:




