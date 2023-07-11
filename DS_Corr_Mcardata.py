#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn


# In[5]:


x=pd.read_csv('MLR_car_data.csv') # seling pric  is (y)label and other are(x) 
print(x)


# In[6]:


x.head()


# In[7]:


x.tail()


# In[8]:


b=x['Present_Price']
a=x['Selling_Price']


# In[9]:


plt.scatter(a,b)
plt.title('price')
plt.xlabel('Present_Price')
plt.ylabel('Selling_Price')
x.corr(numeric_only=True)#for numeric numbers


# In[17]:


c=x['Year']
d=x['Kms_Driven']


# In[37]:


plt.scatter(c,d)
plt.title('year')
plt.xlabel('Year')
plt.ylabel('Kms_Driven')
x.corr(numeric_only=True)


# In[11]:


x.shape


# # data processing

# In[12]:


f=x.drop('Car_Name',axis=1)


# In[13]:


f.head()


# In[14]:


f['Present_year']=2023


# In[16]:


f


# In[17]:


f['Age_of_thecar']=f['Present_year']-f['Year']


# In[18]:


f.head()


# In[20]:


f.drop(['Year','Present_year'],axis=1,inplace=True)


# In[22]:


f.head()


# In[23]:


f=pd.get_dummies(f)


# In[24]:


f.head()


# In[26]:


g=f.drop('Selling_Price',axis=1)


# # mulite colniariy

# In[27]:


plt.figure(figsize=(12,10))
sn.heatmap(g.corr(),annot=True)


# In[ ]:




