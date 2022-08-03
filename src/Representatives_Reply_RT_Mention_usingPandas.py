import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

get_ipython().run_line_magic('matplotlib', 'inline')

rep_df = pd.read_csv('representatives_h.csv', 'representatives_h',delimiter=',',)

rep_df.head()

for col in rep_df.columns:
    print(col)

rep_df.drop(columns=['coordinates','created_at','hashtags','media','favorite_count','id','in_reply_to_screen_name','in_reply_to_status_id','in_reply_to_user_id','lang','place','possibly_sensitive','retweet_count','reweet_id','retweet_screen_name','source','user_created_at','user_default_profile_image','user_description','user_favourites_count','user_followers_count','user_friends_count','user_listed_count','user_location','user_statuses_count','user_time_zone','user_urls','user_verified']).head()

repD_df = rep_df.drop(columns=['coordinates','created_at','hashtags','media','favorite_count','id','in_reply_to_screen_name','in_reply_to_status_id','in_reply_to_user_id','lang','place','possibly_sensitive','retweet_count','reweet_id','retweet_screen_name','source','user_created_at','user_default_profile_image','user_description','user_favourites_count','user_followers_count','user_friends_count','user_listed_count','user_location','user_statuses_count','user_time_zone','user_urls','user_verified'])

repD_df.head()

for i, j in repD_df.iterrows():
    print(i, j)
    break


#Testing DataFrame column codes
#Check to see if it outputs a string
print(isinstance(repD_df['text'][1], str))
j=0
for i in repD_df['text']:
    print(j,":",i)
    print()
    j = j+1
    if j == 30:
        break

replyL = []
retweetL = []
mentionL = []
j = 0
#Assuming that Twitter Retweets cannot be Replies and vice versa
#Assuming that Twitter Mentions can be both Retweets and Replies
for i in repD_df['text']:
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

#rep_df = rep_df.drop(columns = ['reply','retweet','mention'])
#inserting Reply/Retweet/Mention columns to original DataFrame

dfLen = len(rep_df.loc[0])
rep_df.insert(dfLen, "reply", replyL, False)
rep_df.insert(dfLen+1, "retweet", retweetL, False)
rep_df.insert(dfLen+2, "mention", mentionL, False)
repD_df = rep_df.copy()

rep_df.head(258)

pd.set_option('display.max_columns', None)
rep_df.head(30)

print()

rep_handles = {}
dest_handle = []
source_rep = []
extra_dest_handle = []
extra_rows = []
nullcount = 0
extracount = 0
#j = 1
#add twitter handles and political affiliation into hashtable
#for i in repD_df['user_screen_name']
for index, row in rep_df.iterrows():
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
        #print("NULL------------------------")
        dest_handle.append(None)
        nullcount = nullcount+1
    #if j is 257:
    #    break
    #j=j+1
    
#print(dest_handle)
print("LENGTH:",len(dest_handle))
print("NULL COUNT:", nullcount)
nullct = 0
notnull = 0
print("NOT NULLS:", len(dest_handle)-nullcount)
print("EXTRA MENTIONS:", extracount)
print("EXTRA MENTIONS ARR LEN:", len(extra_dest_handle))
print("EXTRA MENTIONS ROW ARR LEN:", len(extra_rows))

rep_df = repD_df
dfLen = len(rep_df.loc[0])
rep_df.insert(dfLen, "destination_handle", dest_handle, False)

rep_df.head(30)

#adding in rows and columns for the extra mentions
repExtra_df = pd.DataFrame()
j = 0
for col in rep_df.columns:
    repExtra_df.insert(j, col, [], False)
    j = j+1
for row in extra_rows:
    repExtra_df = repExtra_df.append(row, ignore_index=True)
repD_df = repExtra_df.copy()

repExtra_df.head()

j = 0
repExtra_df = repExtra_df.drop(columns=['destination_handle'])
repExtra_df.insert(len(repExtra_df.loc[0]), 'destination_handle', extra_dest_handle) 


repExtra_df.head()

repExtra_df['user_verified'].replace([1.0, 0.0], [True, False])
repExtra_df['reply'].replace([1.0, 0.0], [True, False])
repExtra_df['retweet'].replace([1.0, 0.0], [True, False])
repExtra_df['mention'].replace([1.0, 0.0], [True, False])

repExtra_df.head()

repNew_df = pd.concat([rep_df, repExtra_df])
repNew_df.head()

print("LENGTH OF ORIGINAL:", len(rep_df))
print("LENGTH OF EXTRA:", len(repExtra_df))
print("LENGTH CALCULATED:", len(rep_df) + len(repExtra_df))
print("LENGTH OF TOTAL :", len(repNew_df))

repNew_df.to_csv('representatives_updated.csv')
