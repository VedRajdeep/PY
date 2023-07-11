#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sn


# In[3]:


x=pd.read_csv('gapminder_full.csv')


# In[4]:


x.head()


# In[5]:


country=x.country
year=x.year
continent=x.continent
life_exp=x.life_exp
gdp_cap=x.gdp_cap


# In[6]:


sn.violinplot(x=life_exp)
plt.show()


# In[10]:


plt.figure(figsize=(10,10))
# sn.swarmplot(x=continent,y=life_exp)
sn.violinplot(x=continent,y=life_exp)
plt.show()


# In[ ]:




