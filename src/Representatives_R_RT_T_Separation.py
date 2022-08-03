import pandas as pd
import numpy as np
rep_df = pd.read_csv('representatives_affiliations.csv', 'representatives_affiliations',delimiter=',')

rep_df.head()


#Creating new dataframes for Reply/RT/Mention/Tweet
reply_df = pd.read_csv('reply_tweets.csv', 'reply_tweets',delimiter=',')
retweet_df = pd.read_csv('retweet_tweets.csv', 'retweet_tweets',delimiter=',')
mention_df = pd.read_csv('mention_tweets.csv', 'mention_tweets',delimiter=',')
tweet_df = pd.read_csv('regular_tweets.csv', 'regular_tweets',delimiter=',')
#Adding the correct column-name information to each DF
reply_df.head()

#iterating through the dataframe for senators and adding each respective row to their respective DF 
#Separating by Reply/RT/Mention/Tweet
j = 2
for i, row in rep_df.iterrows():
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


reply_df.head()

retweet_df.head()

mention_df.head()

tweet_df.head()

reply_df.to_csv('reply_tweets_combined.csv', index=False)
retweet_df.to_csv('retweet_tweets_combined.csv', index=False)
mention_df.to_csv('mention_tweets_combined.csv', index=False)
tweet_df.to_csv('regular_tweets_combined.csv', index=False)
