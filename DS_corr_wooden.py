#!/usr/bin/env python
# coding: utf-8

# # importing lib

# In[10]:


import pandas as pd #Handlink the data
import matplotlib.pyplot as plt #visualization of scatter plot


# In[2]:


x=pd.read_csv('Woodenboard.csv')
print(x)


# In[3]:


x.head()


# In[4]:


x.tail()


# In[5]:


a=x['Density']
y=x['Stiffness']


# In[13]:


plt.scatter(a,y)
plt.title('Wooden board')
plt.xlabel('Density')
plt.ylabel('Stiffness')


# In[14]:


x.corr()


# In[ ]:




