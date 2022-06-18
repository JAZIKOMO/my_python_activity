#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Brazil = {'States':['Acre', 'Alogoas', 'Amapa', 'Amazonas', 
                     'Bahia', 'Ceara', 'Distrito Federal', 
                     'Espirito Santo', 'Goiás', 'Maranhao', 
                     'Mato grosso', 'Mato grosso do sul', 
                     'Minas gerais', 'Para', 'Paraiba', 
                     'Parana', 'Pernambuco', 'Piaui', 
                     'Rio de Janeiro', 'Rio Grande do norte', 
                     'Rio Grande do Sul', 'Rondonia', 'Roraima', 
                     'Santa Catarina', 'Sao Paulo', 'Sergipe', 'Tocantins'],
          'Capitals': ['Rio Branco', 'Maceió', 'Macapá', 'Manaus', 
                     'Salvador', 'Fortaleza', 'Brasília', 'Vitória',
                     'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande',
                     'Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 
                     'Recife', 'Teresina', 'Rio de Janeiro', 'Natal', 
                     'Porto Alegre', 'Porto Velho', 'Boa Vista', 
                     'Florianópolis', 'São Paulo', 'Aracaju', 'Palmas']}


# In[2]:


Brazil_Fires = pd.DataFrame(Brazil)


# In[3]:


Brazil_Fires


# In[4]:


Brazil_2 = {'States': ['state1', 'state2'],
           'Capitals': ['capital1', 'capital2']}


# In[6]:


Brazil_Fires2 = pd.DataFrame(Brazil_2)


# In[8]:


Brazil_Fires2


# In[9]:


Brazil_Final = Brazil_Fires.append(Brazil_Fires2, ignore_index=True)


# In[10]:


Brazil_Final


# In[ ]:




