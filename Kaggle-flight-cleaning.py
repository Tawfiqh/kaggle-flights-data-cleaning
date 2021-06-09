#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# load in the flights csv
df = pd.read_csv('flights.txt', sep="|")
print(df)


# In[2]:


# - what’s wrong with the `DIVERTED` column? It looks right at a glance, but what is the type of each entry? Look up how to cast a column to a different type in pandas
print(df['DIVERTED'])
print(df['DIVERTED'].unique())


# In[3]:


false_mask = df['DIVERTED'].isin(['False', 'F', '0', False])
true_mask = df['DIVERTED'].isin(['True', 'T', '1', True])

df['DIVERTED'][false_mask] = False
df['DIVERTED'][true_mask] = True

df['DIVERTED'] = df['DIVERTED'].astype(bool)

# display(df['DIVERTED'].unique())
display(df[true_mask])
display(df)


# In[15]:


# - find out what’s wrong with the distance column and fix it. Hint: what is the `.sum()` of the distance col?
# display(df['DISTANCE'].str.split(' ').str.get(1).unique()) # check they are all in miles

df['DISTANCE_miles'] = df['DISTANCE'].str.split(' ').str.get(0).astype(int)
display(df['DISTANCE_miles'])



# In[33]:


# - create a function that uses python’s datetime module to parse the “FLIGHTDATE” 
# to a python datetime object and map that column using the `.apply()` method
# display(df)
from datetime import datetime

df['FLIGHTDATE'] = df['FLIGHTDATE'].astype(str)
df['FLIGHTDATE_datetime'] = df['FLIGHTDATE'].apply(lambda flight_date: datetime.strptime(flight_date, '%Y%m%d'))

display(df)


# In[34]:


# - now replace that code with `pd.to_datetime()`

from datetime import datetime

# df['FLIGHTDATE'] = df['FLIGHTDATE'].astype(str)
df['FLIGHTDATE_datetime_pd'] = pd.to_datetime(df['FLIGHTDATE'], format='%Y%m%d')

display(df)


# In[38]:


# - use the `.duplicated()` method to count how many exact duplicates there are in the dataset
duplicated = df.duplicated(keep='last')
display(df[duplicated])

# No duplicates found?


# In[39]:


# - we might want to remove rows that are not exact duplicates, 
#  but are duplicates across some subset of columns. 
# For example, if we have duplicate users in a table 
#  with the same user_id, but maybe different bios, they should probably be marked as duplicate. 

# Use the `subset` kwarg in the `.duplicated()` method 
#  to check for entries that are matched exactly at the following columns

       # - `“ORIGAIRPORTNAME”, “DESTAIRPORTNAME”, “AIRLINECODE”, “FLIGHTDATE”, “CRSDEPTIME”, “DEPTIME”, “ARRTIME”`
duplicate_columns_to_check = ["ORIGAIRPORTNAME", "DESTAIRPORTNAME", "AIRLINECODE", "FLIGHTDATE", "CRSDEPTIME", "DEPTIME", "ARRTIME"]
duplicated = df.duplicated(subset=duplicate_columns_to_check)

display(df[duplicated])


# In[44]:


# - what are the different values for the `keep` kwarg? What do they do? Which do you want to use here?
# - look up how to use the `.sort_values()` method and sort the dataframe

duplicate_columns_to_check = ["ORIGAIRPORTNAME", "DESTAIRPORTNAME", "AIRLINECODE", "FLIGHTDATE", "CRSDEPTIME", "DEPTIME", "ARRTIME"]
# duplicated = df.duplicated(subset=duplicate_columns_to_check, keep=False)
# display(df[duplicated][duplicate_columns_to_check].sort_values(['FLIGHTDATE','ORIGAIRPORTNAME']))

# - use the `.drop_duplicates()` method to remove the duplicates
df_duplicates_removed = df.drop_duplicates(subset=duplicate_columns_to_check)

display(df)
display(df_duplicates_removed)




# In[47]:


# - look up how to use the `.unique()` method and check the ‘TAILNUM’ column. 
# Notice anything that shouldn’t be there?
display(df['TAILNUM'])
print(list(df['TAILNUM'].unique()) )
display(df_duplicates_removed)

# - replace


# In[ ]:


# - use the `.value_counts()` method to count the different values in the “CANCELLED” column. There is definitely something wrong. Check out the `.replace()` method and fix it. What are the types of arguments that `.replace()` can take in?
# - where appropriate, convert numerical columns into categories

