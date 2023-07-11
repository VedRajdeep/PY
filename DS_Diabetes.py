#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt


# In[8]:


x=pd.read_csv('diabetes.csv')


# In[9]:


x.head()


# In[18]:


x.hist(figsize=(10,10))
plt.show()


# In[ ]:




