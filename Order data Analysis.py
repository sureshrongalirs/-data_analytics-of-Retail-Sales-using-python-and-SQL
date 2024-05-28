#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("D:/Projects/Retail-Orders Project (Python - SQL)/orders.csv")


# In[5]:


df.head()


# In[6]:


# Explore different kind of values in the column of Ship mode
df['Ship Mode'].unique()


# In[7]:


#Handle Null Values
#Here by defafult "nan" can be treated as NULL, But we have to consider "Not Available" and "Unique" as NULL 
# na_values paramater is helpful for make it values as nan
df = pd.read_csv("D:/Projects/Retail-Orders Project (Python - SQL)/orders.csv", na_values = ['Not Available','unknown'] )


# In[8]:


df['Ship Mode'].unique()


# In[19]:


#rename column names, make them lower case and replace space with underscore
#df.rename(columns = {"Order Id" : "order_id", "Order Date" : "order_date", "Ship Mode" : "ship_mode"})
#df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ","_")
df.head()


# In[24]:


#Create new column Discount
df["discount"] = df["cost_price"]*df["discount_percent"]*0.01
df.head()


# In[27]:


#create new column Sale Price
df["sale_price"] = df["cost_price"]-df["discount"]
df.head()


# In[29]:


#Create new column Profit
df["profit"] = df["sale_price"]-df["cost_price"]
df.head()


# In[31]:


#Changing data types of columns
df.dtypes


# In[34]:


#Convert order date from object data type to date time

df["order_date"] = pd.to_datetime(df["order_date"], format = "%Y-%m-%d")
df.dtypes


# In[35]:


#drop columns of cost price, list price and discount_percent 
df.drop(columns = ['cost_price', 'list_price', 'discount_percent'], inplace = True)


# In[36]:


df.head()


# In[37]:


#connecting to sql server
import sqlalchemy as sal
engine = sal.create_engine('mssql://APPLIED_GATE\APPLIED/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[38]:


#Load the data into sql server
df.to_sql('df_orders', con=conn, index=False, if_exists = 'replace')


# In[ ]:




