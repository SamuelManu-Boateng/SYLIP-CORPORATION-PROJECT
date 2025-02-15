#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt


# In[24]:


df= pd.read_excel(r"C:\Users\sarah\Desktop\DATA ANALYST CLASS MAT\SYLIP CORPORATION SALES DATA.xlsx")
df


# In[25]:


pd.set_option('display.max.rows', 101)
pd.set_option('display.max.columns',14)


# In[26]:


#Information about the dataset


df.info()


# In[27]:


#Viewing Data
df


# # DATA CLEANING

# In[28]:


#Deleting Duplicates
df= df.drop_duplicates()
df


# In[29]:


#Dropping irrelevant columns
df = df.drop(columns = ['Sales Channel','Order Priority'])
df


# In[30]:


#Extracting theyears from the order date column

df['Year']=df['Order Date'].dt.year
df


# In[31]:


#Dropping Order date and Ship Date column
df= df.drop(columns =['Order Date', 'Ship Date'])
df


# In[32]:


#Rearraging the columns
new_columns= ['Region','Country','Item Type','Order ID','Year','Units Sold','Unit Price','Unit Cost','Total Revenue','Total Cost','Total Profit']
df = df[new_columns]
df


# In[33]:


#View cleaned data
df


# # KEY PERFORMANCE INDICATORS

# ###### KPI 1: PROFIT FROM ALL REGIONS.

# In[59]:


KPI1 = df.groupby('Region')[['Total Profit']].sum(numeric_only =True).sort_values(by= 'Total Profit', ascending = True)
KPI1


# ###### KPI 2 : REVENUE MADE ANUALLY. 

# In[63]:


KPI2 = df.groupby('Year')[['Total Revenue']].sum(numeric_only=True)
KPI2


# ###### KPI 3 : UNITS SOLD ANNUALLY. 

# In[36]:


KPI3 = df.groupby('Year')[['Units Sold']].sum(numeric_only=True)
KPI3


# ###### KPI 4 : RATE OF TOTAL REVENUE ACHIEVED ANNUALLY. 

# In[37]:


Total_Revenue = df['Total Revenue'].sum()
KPI2['Rate Of Total Revenue'] = ((KPI2['Total Revenue']/ Total_Revenue)*100).round(2)
KPI4= KPI2.drop(columns='Total Revenue')
KPI4


# ###### KPI 5 : AVERAGE AMOUNT OF PROFIT ACHIEVED ANNUALLY 

# In[38]:


KPIM = df.groupby('Year')[['Total Profit']].mean(numeric_only=True)
KPI5 = KPIM.rename(columns={'Total Profit':'Average Profit'})
KPI5


# ###### KPI 6 :  COUNT OF ITEM TYPES SOLD IN EACH REGION.

# In[39]:


KPI6 = df.groupby('Region')[['Item Type']].count().sort_values(by= 'Item Type', ascending=True)
KPI6


# ###### KPI 7 : TOP 4 COUNTRIES WITH HIGHEST REVENUE. 

# In[40]:


KPI7 = df.groupby('Country')[['Total Revenue']].sum(numeric_only=True).sort_values(by='Total Revenue',ascending =False
                                                                                  ).head(4)
KPI7


# ###### KPI 8 : TOP 4 COUNTRIES WITH LOWEST REVENUE. 

# In[41]:


KPI8 =df.groupby('Country')[['Total Revenue']].sum(numeric_only=True).sort_values(by='Total Revenue', ascending=False
                                                                                 ).tail(4)
KPI8


# ###### KPI 9 : TOP 5 COUNTRIES WITH LOWEST UNITS SOLD BELOW THE BENCH MARKET TARGET OF 50000 UNITS. 

# In[42]:


Benchmark = 50000
KPIB = df.groupby('Country')[['Units Sold']].sum(numeric_only=True).sort_values(by='Units Sold',ascending=True).head(5)
KPI9= KPIB.loc[KPIB['Units Sold']< Benchmark,['Units Sold']].sort_values(by= 'Units Sold', ascending=False)
KPI9


# # DATA VISUALIZATION

# ###### KPI 1: PROFIT FROM ALL REGIONS.

# In[71]:


KPI1.plot.barh(figsize =(10,5))


# ###### KPI 2: REVENUE MADE ANNUALLY. 

# In[70]:


KPI2.plot.area(figsize = (10,5))


# ###### KPI 3 : UNITS SOLD ANNUALLY. 

# In[73]:


KPI3.plot(kind= 'bar', stacked =True, figsize = (10,5))


# ###### KPI 4 : RATE OF TOTAL REVENUE ACHEIVED ANNUALLY .

# In[77]:


KPI4.plot.pie(y = 'Rate Of Total Revenue', figsize=(10,10))


# ###### KPI 5 : AVERAGE AMOUNT OF PROFIT ACHIEVED ANNUALLY.  

# In[85]:


KPI5.plot(kind ='line', figsize =(10,5))


# ###### KPI 6 : COUNT OF ITEM TYPES SOLD IN EACH REGION. 

# In[79]:


KPI6.plot(kind = 'bar', stacked =True,figsize =(10,5))


# ###### KPI 7 : TOP 4 COUNTRIES WITH HIGHEST REVENUE. 

# In[84]:


KPI7.plot.barh(figsize =(10,5))


# ###### KPI 8 : TOP 4 COUNTRIES WITH LOWEST REVENUE.  

# In[82]:


KPI8.plot.barh(figsize =(10,5))


# ###### KPI 9 : TOP 5 COUNTRIES WITH LOWEST UNITS SOLD BELOW THE BENCH MARKET TARGET OF 50000 UNITS. 

# In[83]:


KPI9.plot.barh(figsize =(10,5))


# In[ ]:




