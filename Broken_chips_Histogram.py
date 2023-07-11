#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


x=pd.read_excel('Histogram.xlsx')


# In[3]:


x.head(20)


# In[4]:


plt.hist(x)
plt.show()


# In[6]:


plt.boxplot(x)
plt.show()


# In[ ]:




