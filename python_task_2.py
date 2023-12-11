#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv(r"C:\tt\dataset-3.csv")


# In[3]:


df


# # Question 1: Distance Matrix Calculation

# In[4]:


import pandas as pd
import networkx as nx

def calculate_distance_matrix(df):
    # Create a graph using networkx
    G = nx.Graph()

    for _, row in df.iterrows():
        edge_attrs = {'distance': row['distance']}
        G.add_edge(row['id_start'], row['id_end'], **edge_attrs)

    distance_matrix = nx.floyd_warshall_numpy(G, weight='distance')

    distance_matrix = (distance_matrix + distance_matrix.T) / 2

    for i in range(len(distance_matrix)):
        distance_matrix[i, i] = 0

    result_df = pd.DataFrame(distance_matrix, index=G.nodes, columns=G.nodes)

    return result_df


# In[5]:


calculate_distance_matrix(df)


# In[ ]:





# # Question 2: Unroll Distance Matrix

# In[6]:


import pandas as pd

def unroll_distance_matrix(distance_matrix_df):
    unrolled_df = distance_matrix_df.stack().reset_index()

    unrolled_df.columns = ['id_start', 'id_end', 'distance']

    unrolled_df = unrolled_df[unrolled_df['id_start'] != unrolled_df['id_end']]

    unrolled_df.reset_index(drop=True, inplace=True)

    return unrolled_df


# In[7]:


distance_matrix_df = calculate_distance_matrix(df)


# In[8]:


unrolled_result = unroll_distance_matrix(distance_matrix_df)


# In[9]:


unrolled_result


# In[ ]:





# # Question 3: Finding IDs within Percentage Threshold

# In[10]:


import pandas as pd

def find_ids_within_ten_percentage_threshold(df, reference_value):
    # Filter the DataFrame for the given reference value
    reference_df = df[df['id_start'] == reference_value]

    # Calculate the average distance for the reference value
    avg_distance = reference_df['distance'].mean()

    # Calculate the lower and upper bounds of the threshold
    lower_bound = avg_distance * 0.9
    upper_bound = avg_distance * 1.1

    # Filter values within the 10% threshold
    within_threshold = df[(df['id_start'] != reference_value) & (df['distance'] >= lower_bound) & (df['distance'] <= upper_bound)]

    # Get the unique values from the 'id_start' column and sort them
    result_list = sorted(within_threshold['id_start'].unique())

    return result_list


# In[11]:


distance_matrix_df


# In[12]:


reference_value = 12


# In[13]:


result = find_ids_within_ten_percentage_threshold(unrolled_result, reference_value)


# In[ ]:




