#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
sen_df = pd.read_csv('senators_affiliations.csv', 'senators_affiliations',delimiter=',')


# In[2]:


sen_df.head()


# In[4]:


#Creating new dataframes for Reply/RT/Mention/Tweet
reply_df = pd.DataFrame()
retweet_df = pd.DataFrame()
mention_df = pd.DataFrame()
tweet_df = pd.DataFrame()
#Adding the correct column-name information to each DF
j = 0
for col in sen_df.columns:
    reply_df.insert(j, col, [], False)
    retweet_df.insert(j, col, [], False)
    mention_df.insert(j, col, [], False)
    tweet_df.insert(j, col, [], False)
    j = j+1
#checking column names
print(reply_df.head())


# In[5]:


#iterating through the dataframe for senators and adding each respective row to their respective DF 
#Separating by Reply/RT/Mention/Tweet
j = 2
for i, row in sen_df.iterrows():
    if row['reply'] == True:
        #print(j, "Reply")
        reply_df = reply_df.append(row, ignore_index=True)
    if row['retweet'] == True:
        #print(j, "Retweet")
        retweet_df = retweet_df.append(row, ignore_index=True)
    if row['mention'] == True:
        mention_df = mention_df.append(row, ignore_index=True)
        #print(j, "Mention")
    if row['reply'] == False and row['retweet'] == False and row['mention'] == False:
        tweet_df = tweet_df.append(row, ignore_index=True)
        #print(j, "Tweet Only")
print("Success")


# In[6]:


reply_df.head()


# In[7]:


retweet_df.head()


# In[8]:


mention_df.head()


# In[9]:


tweet_df.head()


# In[10]:


reply_df.to_csv('reply_tweets.csv', index=False)
retweet_df.to_csv('retweet_tweets.csv', index=False)
mention_df.to_csv('mention_tweets.csv', index=False)
tweet_df.to_csv('regular_tweets.csv', index=False)

