#!/usr/bin/env python
# coding: utf-8

# # - Some Exercises

# In[ ]:


# The records are in a CSV called "credit_records.csv"
# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records =  pd.read_csv("credit_records.csv")

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())



# In[ ]:


# Use .info() to inspect the DataFrame credit_records
print(credit_records.info())



# In[ ]:


# Select the column item from credit_records
# Use brackets and string notation
items = credit_records['item']

# Display the results
print(items)



# In[ ]:


# DataFrame of missing puppies, which is loaded as mpr.
# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == 'Still Missing']
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)


