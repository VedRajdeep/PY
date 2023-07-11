#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


x=pd.read_csv('Auto.csv')
print(x)


# In[12]:


x.head()


# In[13]:


x.tail()


# In[14]:


a=x['weight']
y=x['mpg']


# In[17]:


plt.scatter(a,y)
plt.title('Auto')
plt.xlabel('weight')
plt.ylabel('mpg')


# In[26]:


x.corr()


# In[24]:


from scipy.stats import pearsonr
corr,_=pearsonr(a,y)
print('Pearson correlation: %.3f' % corr)


# In[ ]:




