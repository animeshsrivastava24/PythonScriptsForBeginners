#!/usr/bin/env python
# coding: utf-8

# In this assignment, I'll be using what I've learnt about numpy, pandas and matplotlib to analyze and visualize the Chinook database.
# The Chinook database contains information about the media in their store, their customers and employees, and their invoice.

# In[1]:


#importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ## 1. Which city has the best customers?

# ##### This is the city with the highest sum of invoice totals. It'll be an ideal place for a promotional music festival

# In[3]:


#loading invoice data

invoice = pd.read_csv("Invoice.csv")
print(invoice)


# In[4]:


# This returns the city name and sum total of the city with the highest sum of invoice totals.
 
best_city = invoice[['BillingCity', 'Total']].groupby('BillingCity').sum().sort_values(by = 'Total', ascending = False)

print(best_city.head(1))


# In[133]:


# a bar chart showing total invoice from each city

plt.figure(figsize=(20,30))
plt.barh('BillingCity', 'Total', data=invoice)
plt.xlabel('Invoice Totals')
plt.ylabel('City')
plt.title('Invoice Total by City')
plt.show()


# ##### From the bar plot, we see that Prague is the city with the best customers, hence the music festival should be held there.

# ## 2. Which countries have the most Invoices?

# In[134]:


# This return a table of BillingCountry and Invoices ordered by the number of invoices for each country.
# The country with the most invoices will appear first. 

best_country = invoice['BillingCountry'].value_counts()
print(best_country)


# In[ ]:


#### The top 5 countries with the most invoices are USA, Canada, France, Brazil and Germany.


# ## 3. Who is the best customer?
# 
# ##### The best customer is the customer who has spent the most money.

# In[135]:


#loading customer data

customers = pd.read_csv('Customer.csv')
customers.head()


# In[136]:


# The customer who has spent the most money

best_customer = invoice[['CustomerId', 'Total']].groupby('CustomerId')['Total'].sum().sort_values(ascending = False).head(1)
print(best_customer)


# In[137]:


#Details of customer with ID no 6

customers[customers['CustomerId'] == 6]


# #### The best customer is from Prague, her name is Helena Holy

# ## 4. Details of customers who listen to rock music

# In[138]:


#loading the Genre data

genre = pd.read_csv('Genre.csv')
genre.head()


# In[139]:


#loading Track data

tracks = pd.read_csv('Track.csv')
tracks.head()


# In[140]:


#loading Invoiceline data

invoice_line = pd.read_csv('InvoiceLine.csv')
invoice_line.head()


# In[141]:


# merging genre and track dataframes 

genre_tracks = pd.merge(tracks[['TrackId', 'GenreId']], genre, on = 'GenreId', how = 'right')
genre_tracks.head()


# #####  We can now use data on customer ID to get the kind of track they purchased.

# In[142]:


# merging invoice line data and invoive data to get each customer ID with invoice details

purchases = pd.merge(invoice_line[['InvoiceId', 'TrackId']], invoice[['InvoiceId', 'CustomerId']], on = 'InvoiceId', how = 'left')
purchases.head()


# In[143]:


# merging purchases with genre_tracks to get the name of track corresponding to each customer's purchase 

genre_category = pd.merge(purchases, genre_tracks, on = 'TrackId', how = 'left')
genre_category.head()


# In[144]:


# getting customers details, we can then use their ID to get the genre of tracks each customer purchased.

customer_details = customers[['CustomerId', 'Email', 'FirstName', 'LastName', 'City', 'Country']]
customer_details.head()


# In[145]:


# category of genre purchased by eash customer

customer_genre = pd.merge(genre_category[['CustomerId', 'Name']], customer_details, on = 'CustomerId', how = 'left')
customer_genre.head()


# In[146]:


# This returns contact details of all Rock Music listeners in alphabetical order(Email)
# This is done by selecting rows with logic 

customer_genre[customer_genre['Name'] == 'Rock'].sort_values(by = 'Email', ascending = True)


# ## 5. Most popular music genre for each country
# 
# #### The most popular genre is the genre with the highest amount of purchases.

# In[147]:


# merging invoice lines data with invoice data so we can match invoice line items to customers

customer_purchase = pd.merge(invoice_line, invoice[['InvoiceId', 'CustomerId', 'BillingCountry']], on = 'InvoiceId', how = 'left')
customer_purchase.head()


# ##### The dataframe can now be completed by adding the genre for each track purchased.

# In[148]:


# Adding genre of track purchased to customer_purchase data

customer_purchase = pd.merge(customer_purchase, genre_tracks, on = 'TrackId', how = 'left')
customer_purchase.head()


# In[149]:


# Calculating the amount of purchases made in each country based on genre of track purchased.

genre_totals = pd.DataFrame(customer_purchase.groupby(['BillingCountry', 'Name'], as_index=False)['UnitPrice'].sum())
genre_totals.head()


# ##### We can now find the highest revenue from a single genre for each country.

# In[150]:


#  This returns the genre with the highest amount of purchases for each country.

max_purchase = pd.DataFrame(genre_totals.groupby('BillingCountry')['UnitPrice'].max())
max_purchase.head()


# In[151]:


# Most popular genre by country

pd.merge(max_purchase, genre_totals, on = ['UnitPrice', 'BillingCountry'], how = 'left')

