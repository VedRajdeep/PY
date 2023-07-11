#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import matplotlib.pyplot as plt


# In[30]:


x=pd.read_excel('Mothersweight.xlsx')


# In[31]:


print(x)


# In[32]:


x.head()


# In[33]:


x.tail()


# In[34]:


a=x['Mothers_weight']
b=x['Infants_birthweight']


# In[39]:


plt.scatter(a,b)
plt.title('Helth')
plt.xlabel('Mothers_weight')
plt.ylabel('Infants_birthweight')


# In[36]:


x.corr()


# In[40]:


x.info()


# In[41]:


x.isna().sum()


# In[42]:


x.isnull().sum()


# In[ ]:




