#!/usr/bin/env python
# coding: utf-8

# # Import approprite libraries 

# In[3]:


import pandas as pd #manupulating & cleaning the data


# In[7]:


x=pd.read_csv("dirtydata.csv")


# In[8]:


print(x) # to ensure


# In[14]:


x.head(10) #fist 5 rows


# In[15]:


x.tail(10)#last 5 rwos


# # Removing Empty cells

# In[16]:


#method1
any=x.dropna()


# In[17]:


print(any)


# In[19]:


#Method 2
x.fillna(777,inplace=True)
print(x)


# In[21]:


#Method 3
x=pd.read_csv("dirtydata.csv")
x['Calories'].fillna(250,inplace=True)
print(x)


# # Wrong Format

# In[23]:


x=pd.read_csv("dirtydata.csv")
x['Date']=pd.to_datetime(x['Date'])


# In[24]:


print(x)


# # Wrong Data

# In[25]:


x=pd.read_csv("dirtydata.csv")
x.loc[7,' Duration ']=45


# In[26]:


print(x)


# # Duplicate Data

# In[27]:


x=pd.read_csv("dirtydata.csv")
x.drop_duplicates(inplace=True)


# In[28]:


print(x)


# In[29]:


x.isna().sum()


# In[31]:


x.info()


# In[ ]:




