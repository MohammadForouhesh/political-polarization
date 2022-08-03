import pandas as pd
import numpy as py

reply_df = pd.read_csv('reply_tweets_combined.csv', 'reply_tweets_combined',delimiter=',')
retweet_df = pd.read_csv('retweet_tweets_combined.csv', 'retweet_tweets_combined',delimiter=',')
mention_df = pd.read_csv('mention_tweets_combined.csv', 'mention_tweets_combined',delimiter=',')
tweet_df = pd.read_csv('regular_tweets_combined.csv', 'regular_tweets_combined',delimiter=',')

user_ver = []
reply = []
retweet = []
mention = []
for i in reply_df['user_verified']:
    if i == 1:
        user_ver.append("True")
    else:
        user_ver.append("False")
for i in reply_df['reply']:
    if i == 1:
        reply.append("True")
    else:
        reply.append("False")
for i in reply_df['retweet']:
    if i == 1:
        retweet.append("True")
    else:
        retweet.append("False")
for i in reply_df['mention']:
    if i == 1:
        mention.append("True")
    else:
        mention.append("False")
reply_df['user_verified'] = user_ver
reply_df['reply'] = reply
reply_df['retweet'] = retweet
reply_df['mention'] = mention
reply_df.head()

user_ver = []
reply = []
retweet = []
mention = []
for i in retweet_df['user_verified']:
    if i == 1:
        user_ver.append("True")
    else:
        user_ver.append("False")
for i in retweet_df['reply']:
    if i == 1:
        reply.append("True")
    else:
        reply.append("False")
for i in retweet_df['retweet']:
    if i == 1:
        retweet.append("True")
    else:
        retweet.append("False")
for i in retweet_df['mention']:
    if i == 1:
        mention.append("True")
    else:
        mention.append("False")
retweet_df['user_verified'] = user_ver
retweet_df['reply'] = reply
retweet_df['retweet'] = retweet
retweet_df['mention'] = mention
retweet_df.head()

user_ver = []
reply = []
retweet = []
mention = []
for i in mention_df['user_verified']:
    if i == 1:
        user_ver.append("True")
    else:
        user_ver.append("False")
for i in mention_df['reply']:
    if i == 1:
        reply.append("True")
    else:
        reply.append("False")
for i in mention_df['retweet']:
    if i == 1:
        retweet.append("True")
    else:
        retweet.append("False")
for i in mention_df['mention']:
    if i == 1:
        mention.append("True")
    else:
        mention.append("False")
mention_df['user_verified'] = user_ver
mention_df['reply'] = reply
mention_df['retweet'] = retweet
mention_df['mention'] = mention
mention_df.head()

user_ver = []
reply = []
retweet = []
mention = []
for i in tweet_df['user_verified']:
    if i == 1:
        user_ver.append("True")
    else:
        user_ver.append("False")
for i in tweet_df['reply']:
    if i == 1:
        reply.append("True")
    else:
        reply.append("False")
for i in tweet_df['retweet']:
    if i == 1:
        retweet.append("True")
    else:
        retweet.append("False")
for i in tweet_df['mention']:
    if i == 1:
        mention.append("True")
    else:
        mention.append("False")
tweet_df['user_verified'] = user_ver
tweet_df['reply'] = reply
tweet_df['retweet'] = retweet
tweet_df['mention'] = mention
tweet_df.head()

reply_df.to_csv('reply_tweets_final.csv', index=False)
retweet_df.to_csv('retweet_tweets_final.csv', index=False)
mention_df.to_csv('mention_tweets_final.csv', index=False)
tweet_df.to_csv('regular_tweets_final.csv', index=False)