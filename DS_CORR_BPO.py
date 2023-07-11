#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


x=pd.read_excel('BPO.xlsx')
print(x)


# In[7]:


x.head()


# In[8]:


x.tail()


# In[7]:


a=x['Cycle_time']
b=x['Hold_time']


# In[8]:


plt.scatter(a,b)
plt.title('Cycle')
plt.xlabel('Hold_time')
plt.ylabel('Cycle_time')
x.corr()


# In[ ]:




