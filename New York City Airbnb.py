#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv('F:\mahmoud ali\oasis project\Task2\AB_NYC_2019.csv')


# In[6]:


print(df.head())


# In[7]:


print(df.info())


# In[8]:


print(df.describe())


# In[9]:


print(df.isnull().sum())


# In[10]:


df['reviews_per_month'].fillna(df['reviews_per_month'].mean(), inplace=True)


# In[11]:


df.dropna(subset=['name'], inplace=True)


# In[12]:


print(df.duplicated().sum())


# In[13]:


df.drop_duplicates(inplace=True)


# In[18]:


plt.figure(figsize=(10, 6))
sns.boxplot(x=df['price']) 
plt.show()


# In[15]:


df = df[df['price'] < 500]


# In[16]:


df['last_review'] = pd.to_datetime(df['last_review'])
print(df['last_review'].sort_values())


# In[17]:


df.to_csv('cleaned_AB_NYC_2019.csv', index=False)


# Recommendations
# Based on the analysis of the rental data in New York City for 2019, we recommend the following:
# 
# Establish Clearer Pricing Guidelines:
# Given the presence of outliers in the rental prices, it is advisable to establish clearer and more transparent pricing guidelines to avoid large price discrepancies between similar properties.
# Regular Review of Properties with Unjustifiably High Prices:
# 
# Properties listed with unusually high prices compared to the general market rate in the same area should be regularly reviewed and evaluated. This may indicate inaccurate data or problems with excessive pricing.
# Improve Data Collection Quality:
# 
# Some missing or incomplete values were found in the dataset (such as "reviews_per_month"). It is recommended to improve the data collection mechanisms to ensure the accuracy and completeness of the information used in the analyses.
# Target Areas with Affordable Prices:
# 
# Based on the geographic analysis of prices, investment or marketing strategies can target areas that offer affordable rentals but are still close to high-demand neighborhoods such as Manhattan and Brooklyn.
# Enhance Property Features:
# 
# The analysis shows that properties with high ratings tend to perform better in terms of pricing. It is beneficial to improve the services and quality of the properties to gain higher positive reviews, which can boost market value.
# Expand Analysis of Seasonal Demand:
# 
# Additional analysis of seasonal demand for properties in New York would be useful, as rental prices and demand may fluctuate based on time periods (e.g., holiday seasons or tourism peaks).
# Evaluate the Impact of Reviews on Performance:
# 
# Properties with high user ratings achieve better financial performance. Implementing programs to incentivize property owners to improve guest services and obtain higher ratings could lead to increased revenue.
# These recommendations are based on an initial analysis of the data and could be further developed by expanding the scope of the analysis to include additional factors, such as population distribution, property types, or the impact of economic events.

# In[ ]:




