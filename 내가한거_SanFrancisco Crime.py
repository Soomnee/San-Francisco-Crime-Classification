#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[50]:


import os


# In[51]:


os.getcwd()


# In[52]:


os.chdir('C:\\Users\\USER\\Documents\\GitHub\\San Francisco Crime Kaggle')


# ## Load Dataset

# In[53]:


import pandas as pd


# In[54]:


train = pd.read_csv("train.csv")
print(train.shape)
train.head()


# ## Explore

# In[55]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import matplotlib.pyplot as plt


# ## Dates

# In[56]:


train["Dates"].dtype


# In[57]:


train["Dates"] = pd.to_datetime(train["Dates"])


# In[58]:


train["Dates"].dt.year


# In[59]:


train["Dates"].dt.month

train["Dates-year"] = train["Dates"].dt.year
train
# In[60]:


train["Dates-year"] = train["Dates"].dt.year
train


# In[61]:


train["Dates-month"] = train["Dates"].dt.month
train["Dates-day"] = train["Dates"].dt.day
train["Dates-hour"] = train["Dates"].dt.hour
train["Dates-minute"] = train["Dates"].dt.minute
train["Dates-second"] = train["Dates"].dt.second


# In[62]:


print(train.shape)
train.head()


# In[63]:


sns.countplot(data=train, x="Dates-year")


# In[64]:


figure, ((ax1, ax2, ax3), (ax4, ax5, ax6) ) = plt.subplots(nrows=2, ncols=3)
sns.countplot(data=train, x="Dates-year")


# In[ ]:





# In[65]:


figure, ((ax1, ax2, ax3), (ax4, ax5, ax6) ) = plt.subplots(nrows=2, ncols=3)
figure.set_size_inches(18,8)
sns.countplot(data=train, x="Dates-year", ax=ax1)
sns.countplot(data=train, x="Dates-month", ax=ax2)
sns.countplot(data=train, x="Dates-day", ax=ax3)
sns.countplot(data=train, x="Dates-hour", ax=ax4)
sns.countplot(data=train, x="Dates-minute", ax=ax5)
sns.countplot(data=train, x="Dates-second", ax=ax6)


# In[66]:


train[["X","Y"]]


# In[67]:


train.head()


# In[68]:


train[["X"]]

sns.lmplot(data=train, x="X", y="Y", fit_reg=False)
# In[69]:


sns.lmplot(data=train, x="X", y="Y", fit_reg=False)


# In[70]:


train["X"].max(), train["Y"].max()


# In[71]:


X_outliers = (train["X"]==train["X"].max())
Y_outliers = (train["Y"]==train["Y"].max())
Outliers = train[X_outliers & Y_outliers]

print(Outliers.shape)
Outliers


# In[72]:


trainwithoutoutliers= train[~(X_outliers & Y_outliers)]


# In[73]:


sns.lmplot(data=trainwithoutoutliers, x="X", y="Y", fit_reg = False)


# In[75]:


train.shape


# In[76]:


train.head()


# In[77]:


sns.countplot(data=train, x="DayOfWeek")


# In[103]:


figure, ((ax1, ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3)


# In[106]:


figure, ((ax1, ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3)
figure.set_size_inches(18,8)

dayofweek_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

target = train[train["PdDistrict"]=="Northern"]
sns.countplot(data=train, x="DayOfWeek",order = dayofweek_list, ax=ax1)

target = train[train["PdDistrict"]=="Park"]
sns.countplot(data=train, x="DayOfWeek",order = dayofweek_list, ax=ax2)

target = train[train["Category"]=="OTHER OFFENSES"]
sns.countplot(data=train, x="DayOfWeek",order = dayofweek_list, ax=ax3)

target = train[train["Category"]=="DRUG"]
sns.countplot(data=train, x="DayOfWeek",order = dayofweek_list, ax=ax4)

target = train[train["Category"]=="WARRANTS"]
sns.countplot(data=train, x="DayOfWeek",order = dayofweek_list, ax=ax5)

target = train[train["Category"]=="LARCENY/THEFT"]
sns.countplot(data=train, x="DayOfWeek",order = dayofweek_list, ax=ax6)


# In[102]:


plt.figure(figsize=(12,4))
dayofweek_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




