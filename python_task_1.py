#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv(r"C:\tt\dataset-1.csv")


# In[3]:


df


# # Question 1: Car Matrix Generation

# In[4]:


import pandas as pd

def generate_car_matrix():
    df = pd.read_csv(r"C:\tt\dataset-1.csv")

    df = df.pivot(index='id_1', columns='id_2', values='car')

    for i in range(min(df.shape)):
        df.iloc[i, i] = 0
    return df


# In[5]:


generate_car_matrix()


# # Question 2: Car Type Count Calculation

# In[6]:


import pandas as pd

def get_type_count(df):
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    type_counts = df['car_type'].value_counts().to_dict()
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts


# In[7]:


get_type_count(df)


# In[8]:


56+196+89


# # Question 3: Bus Count Index Retrieval

# In[9]:


import pandas as pd

def get_bus_indexes(df):
    bus_mean = df['bus'].mean()

    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    bus_indexes.sort()

    return bus_indexes


# In[10]:


get_bus_indexes(df)


# # Question 4: Route Filtering

# In[11]:


def filter_routes(df):
    route_avg_truck = df.groupby('route')['truck'].mean()

    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    selected_routes.sort()

    return selected_routes


# In[12]:


filter_routes(df)


# # Question 5: Matrix Value Modification

# In[13]:


def multiply_matrix(input_df):
    
    modified_df = input_df.copy()

    modified_df[modified_df > 20] *= 0.75
    modified_df[modified_df <= 20] *= 1.25

    modified_df = modified_df.round(1)

    return modified_df


# In[14]:


result_df = generate_car_matrix()


# In[15]:


modified_result = multiply_matrix(result_df)


# In[16]:


modified_result 


# # Question 6: Time Check

# In[17]:


df2=pd.read_csv(r"C:\tt\dataset-2.csv")


# In[18]:


df2


# In[ ]:





# In[ ]:




