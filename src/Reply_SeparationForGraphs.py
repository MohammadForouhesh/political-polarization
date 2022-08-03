#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import numpy as py
reply_df = pd.read_csv('reply_tweets_sentiment.csv', 'reply_tweets_sentiment',delimiter=',')


# In[82]:


keepcols = ["source_handle", "source_affiliation", "destination_handle", "destination_affiliation", "polarity", "subjectivity"] 

for col in reply_df.columns:
    if col in keepcols:
        continue
    else:
        reply_df = reply_df.drop(columns=col)
dem_rep = reply_df.copy()
dem_dem = reply_df.copy()
rep_rep = reply_df.copy()
rep_dem = reply_df.copy()


# In[83]:


#list to drop all unnecessary rows; rows with dest_affil with nulls or Dems
rowdrop = []
rindex = 0
#j = 0
for d in dem_rep['destination_affiliation']:
    if d != 'Republican':
        #print(rindex, d)
        rowdrop.append(rindex)
    elif dem_rep['source_affiliation'][rindex] != 'Democrat':
        rowdrop.append(rindex)
    rindex = rindex+1
dem_rep = dem_rep.drop(rowdrop)


# In[84]:


#list to drop all unnecessary rows; rows with dest_affil with nulls or Dems
rowdrop = []
rindex = 0
#j = 0
for d in dem_dem['destination_affiliation']:
    if d != 'Democrat':
        #print(rindex, d)
        rowdrop.append(rindex)
    elif dem_dem['source_affiliation'][rindex] != 'Democrat':
        rowdrop.append(rindex)
    rindex = rindex+1
dem_dem = dem_dem.drop(rowdrop)


# In[85]:


#list to drop all unnecessary rows; rows with dest_affil with nulls or Dems
rowdrop = []
rindex = 0
#j = 0
for d in rep_rep['destination_affiliation']:
    if d != 'Republican':
        #print(rindex, d)
        rowdrop.append(rindex)
    elif rep_rep['source_affiliation'][rindex] != 'Republican':
        rowdrop.append(rindex)
    rindex = rindex+1
rep_rep = rep_rep.drop(rowdrop)


# In[86]:


#list to drop all unnecessary rows; rows with dest_affil with nulls or Dems
rowdrop = []
rindex = 0
#j = 0
for d in rep_dem['destination_affiliation']:
    if d != 'Democrat':
        #print(rindex, d)
        rowdrop.append(rindex)
    elif rep_dem['source_affiliation'][rindex] != 'Republican':
        rowdrop.append(rindex)
    rindex = rindex+1
rep_dem = rep_dem.drop(rowdrop)


# In[87]:


dem_rep = dem_rep.drop(columns = ['source_affiliation', 'destination_affiliation', 'subjectivity'])
dem_dem = dem_dem.drop(columns = ['source_affiliation', 'destination_affiliation', 'subjectivity'])
rep_rep = rep_rep.drop(columns = ['source_affiliation', 'destination_affiliation', 'subjectivity'])
rep_dem = rep_dem.drop(columns = ['source_affiliation', 'destination_affiliation', 'subjectivity'])


# In[88]:


dem_rep = dem_rep.rename(columns={'source_handle': 'Source', 'destination_handle':'Target', 'polarity':'regulation'})
dem_dem = dem_dem.rename(columns={'source_handle': 'Source', 'destination_handle':'Target', 'polarity':'regulation'})
rep_rep = rep_rep.rename(columns={'source_handle': 'Source', 'destination_handle':'Target', 'polarity':'regulation'})
rep_dem = rep_dem.rename(columns={'source_handle': 'Source', 'destination_handle':'Target', 'polarity':'regulation'})


# In[89]:


reg = []
for i in dem_rep['regulation']:
    if i < 0 and i > -0.3:
        reg.append(-0.3)
    elif i < -0.3 and i > -0.6:
        reg.append(-0.6)
    elif i < -0.6 and i > -1:
        reg.append(-1)
    elif i > 0 and i < 0.3:
        reg.append(0.3)
    elif i > 0.3 and i < 0.6:
        reg.append(0.6)
    elif i > 0.6 and i < 1:
        reg.append(1)
    else:
        reg.append(i)
dem_rep = dem_rep.drop(columns=['regulation'])
dem_rep.insert(2,"regulation",reg,False)


# In[90]:


reg = []
for i in dem_dem['regulation']:
    if i < 0 and i > -0.3:
        reg.append(-0.3)
    elif i < -0.3 and i > -0.6:
        reg.append(-0.6)
    elif i < -0.6 and i > -1:
        reg.append(-1)
    elif i > 0 and i < 0.3:
        reg.append(0.3)
    elif i > 0.3 and i < 0.6:
        reg.append(0.6)
    elif i > 0.6 and i < 1:
        reg.append(1)
    else:
        reg.append(i)
dem_dem = dem_dem.drop(columns=['regulation'])
dem_dem.insert(2,"regulation",reg,False)


# In[91]:


reg = []
for i in rep_rep['regulation']:
    if i < 0 and i > -0.3:
        reg.append(-0.3)
    elif i < -0.3 and i > -0.6:
        reg.append(-0.6)
    elif i < -0.6 and i > -1:
        reg.append(-1)
    elif i > 0 and i < 0.3:
        reg.append(0.3)
    elif i > 0.3 and i < 0.6:
        reg.append(0.6)
    elif i > 0.6 and i < 1:
        reg.append(1)
    else:
        reg.append(i)
rep_rep = rep_rep.drop(columns=['regulation'])
rep_rep.insert(2,"regulation",reg,False)


# In[92]:


reg = []
for i in rep_dem['regulation']:
    if i < 0 and i > -0.3:
        reg.append(-0.3)
    elif i < -0.3 and i > -0.6:
        reg.append(-0.6)
    elif i < -0.6 and i > -1:
        reg.append(-1)
    elif i > 0 and i < 0.3:
        reg.append(0.3)
    elif i > 0.3 and i < 0.6:
        reg.append(0.6)
    elif i > 0.6 and i < 1:
        reg.append(1)
    else:
        reg.append(i)
rep_dem = rep_dem.drop(columns=['regulation'])
rep_dem.insert(2,"regulation",reg,False)


# In[99]:


dem_rep.to_csv('reply_dem_rep.csv', index=False)
dem_dem.to_csv('reply_dem_dem.csv', index=False)
rep_rep.to_csv('reply_rep_rep.csv', index=False)
rep_dem.to_csv('reply_rep_dem.csv', index=False)

