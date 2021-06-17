# -*- coding: utf-8 -*-
"""
Created on  Jun 21,2021

@author: RL
"""

#import re
import pandas as pd
#import numpy as np
#import os
#import matplotlib.pyplot as plt
#import seaborn as sns
#%matplotlib inline
import csv



# read input data


data = pd.read_csv('G:\DataScience\eon\interview_signup_.csv', sep=',')


data.head(10)

data.describe()
data.dtypes



# check mising values

def draw_missing_values_table(data):
    nullCount  = data.isnull().sum().sort_values(ascending=False)
    percentage = (data.isnull().sum().sort_values(ascending=False))*100/data.shape[0]
    missingTable = pd.concat([nullCount,percentage],axis=1,keys=['Total','Percentage'])
    return missingTable

draw_missing_values_table(data)

# Bundesland with 9 % missings

# bar chart Bundesland

data['bundesland'].value_counts().plot(kind='bar')

# bar chart Product Name

data['original_product_name'].value_counts().plot(kind='bar')


index = data.index
print(len(index))


# drop false product names

# In case that new products are introduced ...
# Please add new poduct name to the following list :

original_product_name = ['E.ON STROM', 'E.ON STROM 24', 'E.ON STROM ÖKO', 'E.ON STROM ÖKO 24', 'E.ON STROM PUR']
  
p_series = pd.Series(original_product_name)  
frame = { 'original_product_name': p_series}  
product = pd.DataFrame(frame)
  
print(product)


df1 = data

data = df1.merge(product, how='inner', left_on='original_product_name', right_on='original_product_name')

#check
data['original_product_name'].value_counts().plot(kind='bar')

# check rowcount
index = data.index
print(len(index))


#


# leading zero in postcode is missing, when lenght is 4 
# ".0" at the end of some postcodes 

 
                                    
                                    
data['postcode'] = data['postcode'].astype(str)

data['length_pc'] = 0

data['length_pc'] = data['postcode'].apply(len)

data.head(10)



data['length_pc'].value_counts().plot(kind='bar')

filter7 = data.loc[data['length_pc']  == 7]
filter6 = data.loc[data['length_pc']  == 6]
filter5 = data.loc[data['length_pc']  == 5]
filter4 = data.loc[data['length_pc']  == 4]



filter7.head(10)
filter6.head(10)
filter5.head(10)
filter4.head(10)

# check row count

index = data.index
index = filter4.index
print(len(index))


# postcode, delete ".0" 

filter7['postcode'] = filter7['postcode'].str.slice(start=0, stop=5)

filter6['postcode'] = filter6['postcode'].str.slice(start=0, stop=4)

# fill leading zero

filter6['postcode'] = filter6['postcode'].str.zfill(5)
filter4['postcode'] = filter4['postcode'].str.zfill(5)

# Kontrolle


filter7.head(10)

filter4.head(10)
filter6.head(10)


# concat

frames = [filter7, filter6, filter5, filter4]

df = pd.concat(frames)

print(frames)
df.shape


index = df.index
print(len(index))


df['length_pc'] = df['postcode'].apply(len)

#check lenght 

df['length_pc'].value_counts().plot(kind='bar')


###########################################

# add information "Bundesland" from external table 



land= pd.read_csv('G:\DataScience\eon\postcode_txt.txt', header = 0, dtype = "str")


result = df.merge(land, how='left', left_on='postcode', right_on='postcode')


result.head()
result.dtypes


index = result.index
print(len(index))


data = result

# final check completeness

def draw_missing_values_table(data):
    nullCount  = data.isnull().sum().sort_values(ascending=False)
    percentage = (data.isnull().sum().sort_values(ascending=False))*100/data.shape[0]
    missingTable = pd.concat([nullCount,percentage],axis=1,keys=['Total','Percentage'])
    return missingTable

draw_missing_values_table(data)


result.drop(columns=['length_pc'], inplace=True)   
result.drop(columns=['bundesland'], inplace=True)   

result.rename(columns={'Bundesland': 'bundesland'}, inplace=True)      


result.sort_values(by=['order_date'], inplace=True)

# save result table

result.to_csv('G:\DataScience\eon\interview_signup_fin.csv', sep = "," , 
           quoting=csv.QUOTE_NONNUMERIC,       doublequote=True,    index=False)




###########################


