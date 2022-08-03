#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


sen_df = pd.read_csv('senators_h.csv', 'senators_h',delimiter=',',)


# In[4]:


sen_df.head()


# In[5]:


senD_df = sen_df.drop(columns=['coordinates','created_at','hashtags','media','favorite_count','id','in_reply_to_screen_name','in_reply_to_status_id','in_reply_to_user_id','lang','place','possibly_sensitive','retweet_count','reweet_id','retweet_screen_name','source','user_created_at','user_default_profile_image','user_description','user_favourites_count','user_followers_count','user_friends_count','user_listed_count','user_location','user_statuses_count','user_time_zone','user_urls','user_verified'])


# In[6]:


senD_df.head()


# In[7]:


replyL = []
retweetL = []
mentionL = []
j = 0
#Assuming that Twitter Retweets cannot be Replies and vice versa
#Assuming that Twitter Mentions can be both Retweets and Replies
for i in senD_df['text']:
    if i[0] is "@":
        replyL.append(True)
        retweetL.append(False)
    elif i[0:2] == 'RT':
        replyL.append(False)
        retweetL.append(True)
    else:
        replyL.append(False)
        retweetL.append(False)
    if '@' in i[5:]:
        mlist = re.findall(r'@\w+',i)
        if len(mlist) is 0:
                mentionL.append(False)
                continue
        mentionL.append(True)
    else:
        mentionL.append(False)


print("Reply length =", len(replyL))
print()
print("Retweet length =", len(retweetL))
print()
print("Mention length =", len(mentionL))


# In[8]:


#sen_df = sen_df.drop(columns=['reply','retweet','mention'])
#inserting Reply/Retweet/Mention columns to original DataFrame
dfLen = len(sen_df.loc[0])
sen_df.insert(dfLen, "reply", replyL, False)
sen_df.insert(dfLen+1, "retweet", retweetL, False)
sen_df.insert(dfLen+2, "mention", mentionL, False)


# In[9]:


pd.set_option('display.max_columns', None)
sen_df.head(30)


# In[10]:


import re
dest_handle = []
extra_dest_handle = []
extra_rows = []
nullcount = 0
extracount = 0
#j = 1
#add twitter handles and political affiliation into hashtable
#for i in repD_df['user_screen_name']
for index, row in sen_df.iterrows():
    #print(j,row['text'][0:5])
    if row['retweet'] is True:
        #print("RETWEET OF:", row['retweet_screen_name'])
        dest_handle.append(row['retweet_screen_name'])
    elif row['reply'] is True:
        if row['mention'] is False:
            #print("REPLY TO:",row['text'].split()[0][1:])
            dest_handle.append(row['text'].split()[0][1:])
        elif row['mention'] is True:
           # print("REPLY AND MENTION")
           # print("REPLY TO:", row['text'].split()[0][1:])
            dest_handle.append(row['text'].split()[0][1:])
            mlist = re.findall(r'(?<=\W)@\w+',row['text'][1:])
            #print("REPLY ALSO MENTIONS:=====================")
            for i in mlist:
                extra_rows.append(row)
                extra_dest_handle.append(i[1:])
                #print(i[1:])
                extracount = extracount+1
    elif (row['reply'] is False) and (row['retweet'] is False) and (row['mention'] is True):
        mlist = re.findall(r'@\w+',row['text'])
        #print("MENTION OF:",mlist[0][1:])
        dest_handle.append(mlist[0][1:])
        if len(mlist)>1:
            #print("EXTRA MENTIONS:=======================")
            x=0
            for i in mlist:
                x=x+1
                if x is not 1:
                    extra_rows.append(row)
                    extra_dest_handle.append(i[1:])
                    #print(i[1:])
                    extracount = extracount+1
                    #print(row['id'])
    else:
        dest_handle.append(None)
        nullcount = nullcount+1
        
print("LENGTH:",len(dest_handle))
print("NULL COUNT:", nullcount)
nullct = 0
notnull = 0
print("NOT NULLS:", len(dest_handle)-nullcount)
print("EXTRA MENTIONS:", extracount)
print("EXTRA MENTIONS ARR LEN:", len(extra_dest_handle))
print("EXTRA MENTIONS ROW ARR LEN:", len(extra_rows))


# In[11]:


senD_df = sen_df.copy()


# In[12]:


sen_df = senD_df
dfLen = len(sen_df.loc[0])
sen_df.insert(dfLen, "destination_handle", dest_handle, False)


# In[13]:


sen_df.head(30)


# In[14]:


#adding in rows and columns for the extra mentions
senExtra_df = pd.DataFrame()
j = 0
for col in sen_df.columns:
    senExtra_df.insert(j, col, [], False)
    j = j+1
for row in extra_rows:
    senExtra_df = senExtra_df.append(row, ignore_index=True)
senD_df = senExtra_df.copy()


# In[15]:


senExtra_df.head()


# In[16]:


j = 0
senExtra_df = senExtra_df.drop(columns=['destination_handle'])
senExtra_df.insert(len(senExtra_df.loc[0]), 'destination_handle', extra_dest_handle) 


# In[17]:


senNew_df = pd.concat([sen_df, senExtra_df])
senNew_df.head()


# In[18]:


print("LENGTH OF ORIGINAL:", len(sen_df))
print("LENGTH OF EXTRA:", len(senExtra_df))
print("LENGTH CALCULATED:", len(sen_df) + len(senExtra_df))
print("LENGTH OF TOTAL :", len(senNew_df))


# In[19]:


senNew_df.to_csv('senators_updated.csv', index=False)

