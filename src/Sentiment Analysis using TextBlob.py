#!/usr/bin/env python
# coding: utf-8

# In[12]:


from textblob import TextBlob
import pandas as pd


# In[13]:


reply_df = pd.read_csv('reply_tweets_final.csv', 'reply_tweets_combined',delimiter=',')
retweet_df = pd.read_csv('retweet_tweets_final.csv', 'retweet_tweets_combined',delimiter=',')
mention_df = pd.read_csv('mention_tweets_final.csv', 'mention_tweets_combined',delimiter=',')
tweet_df = pd.read_csv('regular_tweets_final.csv', 'regular_tweets_combined',delimiter=',')


# In[22]:


#analyzing the polarity and subjectivity of each twitter text per row
#putting them each in arrays
pol = [] #polarity
sub = [] #subjectivity
for tweet in reply_df['text']:
    analysis = TextBlob(tweet)
    pol.append(analysis.polarity)
    sub.append(analysis.subjectivity)


# In[23]:


dfLen = len(reply_df.loc[0])
reply_df.insert(dfLen, "polarity", pol, False)
reply_df.insert(dfLen+1, "subjectivity", sub, False)


# In[25]:


pol = []
sub = []
for tweet in retweet_df['text']:
    analysis = TextBlob(tweet)
    pol.append(analysis.polarity)
    sub.append(analysis.subjectivity)


# In[26]:


dfLen = len(retweet_df.loc[0])
retweet_df.insert(dfLen, "polarity", pol, False)
retweet_df.insert(dfLen+1, "subjectivity", sub, False)


# In[27]:


pol = []
sub = []
for tweet in mention_df['text']:
    analysis = TextBlob(tweet)
    pol.append(analysis.polarity)
    sub.append(analysis.subjectivity)


# In[28]:


dfLen = len(mention_df.loc[0])
mention_df.insert(dfLen, "polarity", pol, False)
mention_df.insert(dfLen+1, "subjectivity", sub, False)


# In[29]:


pol = []
sub = []
for tweet in tweet_df['text']:
    analysis = TextBlob(tweet)
    pol.append(analysis.polarity)
    sub.append(analysis.subjectivity)


# In[30]:


dfLen = len(tweet_df.loc[0])
tweet_df.insert(dfLen, "polarity", pol, False)
tweet_df.insert(dfLen+1, "subjectivity", sub, False)


# In[35]:


reply_df.to_csv('reply_tweets_sentiment.csv', index=False)
retweet_df.to_csv('retweet_tweets_sentiment.csv', index=False)
mention_df.to_csv('mention_tweets_sentiment.csv', index=False)
tweet_df.to_csv('regular_tweets_sentiment.csv', index=False)

