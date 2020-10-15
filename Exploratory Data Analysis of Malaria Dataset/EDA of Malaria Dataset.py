#!/usr/bin/env python
# coding: utf-8

# ## Malaria Dataset: Cases and Deaths from Different Countries(2000-2017)

# Malaria is a life-threatening disease caused by the Plasmodioum falciparum parasite. It can be transmitted through the bites of infected female Anopheles mosquitoes.
# 
# Worldwide, malaria causes over 400,000 deaths annually. The good news is that it is preventable and curable.
# 
# The WHO African Region carries a disproportionately high share of the global malaria burden and records more deaths than other regions.
# 
# In this notebook, I will analyse the WHO Malaria Report for the years 2000-2017. I will also answer insightful questions on geographical prevalence and progression of these events.

# In[1]:


# importing libraries

import pandas as pd                  # for data manipulation

import numpy as np                   # for statistical analysis

import matplotlib.pyplot as plt      # for plotting graphs
 
get_ipython().run_line_magic('matplotlib', 'inline')
# "%matplotlib inline" ensures commands in cells below the cell that outputs a plot does not affect the plot


# In[2]:


#loading the dataset

reported = pd.read_csv('reported_numbers.csv')


# previewing the data

reported.head()                     


# In[3]:


reported.shape                         # returns the no. of rows and columns


# ##### There are 5 columns and 1944 rows

# In[4]:


reported.describe(include = 'all')     # This is used to view basic statistical details like percentile, mean, std etc.


# ##### From the output of the .describe() query, we see that the data consists of 108 countries(unique) and 18 years report(freq).

# In[7]:


# Checking to see if any feature has empty/missing values

reported.isnull().sum()


# ##### 'No. of cases' & 'No. of deaths' columns both have null values. since the values for each countries differ greatly, it'll be impractical to use the mode/mean imputation technique.
# ##### In that case, the rows with missing values will be dropped, since we don't have sufficient information on that row.

# In[8]:


# dropping rows with null values

reported.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)


# In[9]:


# Let's confirm that there's no more null values

reported.isnull().sum()


# ##### Neat! No more null values, the data is clean. We can now start analysis.

# In[10]:


# Top 10 countries with the highest no of cases over the years?

danger_zones = reported[['Country', 'No. of cases', 'No. of deaths']].groupby('Country').sum().sort_values(by = 'No. of cases', ascending = False)
danger_zones.head(10)


# ##### Congo recorded the highest no. of cases and deaths in the world. That's serious.

# In[11]:


# Top 10 countries with the lowest no of cases over the years?

safe_countries = reported[['Country', 'No. of cases', 'No. of deaths']].groupby('Country').sum().sort_values(by = 'No. of cases', ascending = True)
safe_countries.head(10)


# ##### We see that about 8 countries have not recorded deaths due to malaria in 18 years! Impressive!

# ##### Let's see the stats for my country Nigeria

# In[12]:


nigeria = reported[reported.Country == 'Nigeria']
nigeria


# ##### Sighs! We still have a long way to go as a nation. Of the 18 years, Nigeria has just 4 years of complete data, too bad. 
# ##### The no of cases has  greatly increased, although the death rate has been reducing. There isn't enough data to make conclusions.

# ##### Let's see how malaria events has progressed over the years.

# In[14]:


# Progression of cases and deaths over the years

annual = reported.groupby('Year').sum()
annual


# In[17]:


# What years were the most deaths reported?

tough_years = reported.groupby('Year').sum().sort_values(by='No. of deaths', ascending=False)
tough_years.head()


# ##### 2010 has the highest number of deaths.
# ##### There seems to be some improvement though; the no. of cases reported in 2016 is the highest so far, yet, less people died from the disease than did in 2010.This may be due to technological advances that introduced the use of rapid diagnostic test kits. This makes testing easier and produces faster results.
# ##### This improvement can also be attributed to the generous funding provided to the research department. The mode of action of these parasites have been extensively studied and more antibiotics have been produced.

# In[20]:


# Are some region doing better than the others?

region = reported.groupby('WHO Region').sum().sort_values(by='No. of deaths', ascending=False)
region


# ##### Africa remains the region with the highest number of cases and deaths. 
# ##### Europe has the least number of cases and deaths, some european countries have also been able to eradicate the disease.

# #####  Interactive data visualizations were also carried out using Power BI

# ### Conclusion
# ##### Africa region needs all the help they can get, in form of funding, research support and materials.
# ##### Awareness should also be created on the effect of antibiotics abuse since this has resulted in resistant to once-effective antimalarial drugs.
# 

# In[ ]:


reported.to_csv('cleaned_reported.csv', index =False)

