import pandas as pd
import numpy as np

rep_df = pd.read_csv('representatives_updated_tweet_type.csv', 'representatives_updated_h',delimiter=',')

rep_df.head()

legis_df = pd.read_csv('legislators-current.csv', 'legislators-current',delimiter=',')

legisdict = {}
j = 0
for index, row in legis_df.iterrows():
    legisdict.update({row['full_name']: row['party']})
    legisdict.update({row['twitter']: row['party']})
    print(j)
    j = j+1
    print("Name:", row['full_name'])
    print("Handle:", row['twitter'])
    print("Party:", row['party'])
    print("------------------------")

print(len(legisdict))
print(len(legis_df))

for i in legisdict:
    print("Key:",i)
    print("Party:",legisdict[i])
    print("---------------------")

#testing dictionary
j = 0
source_affiliation = []
for i in rep_df['source_handle']:
    #print("Name:", rep_df['user_name'][j])
    #print("Twitter Handle:", i)
    if i in legisdict.keys():
        #print("Party:", legisdict[i])
        source_affiliation.append(legisdict[i])
    elif rep_df['user_name'][j][0:5] == "Rep. ":
            #print("Party:", legisdict[rep_df['user_name'][j][5:]])
            source_affiliation.append(legisdict[rep_df['user_name'][j][5:]])
    elif rep_df['user_name'][j] in legisdict.keys():
            #print("Party:", legisdict[rep_df['user_name'][j]])
            source_affiliation.append(legisdict[rep_df['user_name'][j]])
    else:
        print("Party: NO AFFILIATION FOUND")
        print(rep_df['user_name'][j][5:])

print(len(source_affiliation))
print(len(rep_df['source_handle']))

dfLen = len(rep_df.loc[0])
rep_df.insert(dfLen-1, "source_affiliation", source_affiliation, False)

rep_df.head()

print(rep_df['destination_handle'][0])
nvar = rep_df['destination_handle'][0]

j = 0
dest_affiliation = []
null_affiliation = []
for i in rep_df['destination_handle']:
    #print("Name:", rep_df['user_name'][j])
    #print("Twitter Handle:", i)
    if i is nvar:
        #print("Handle not legislator")
        dest_affiliation.append(None)
        null_affiliation.append(i)
    elif i in legisdict.keys():
        #print("Party:", legisdict[i])
        dest_affiliation.append(legisdict[i])
    else:
        #print("Party: NO AFFILIATION FOUND")
        dest_affiliation.append(None)
        null_affiliation.append(i)
        #print(i)
#print(null_affiliation)
#print(dest_affiliation)
#print(legisdict[rep_df['destination_handle'][0]])

print(len(dest_affiliation))
print(len(null_affiliation))

dfLen = len(rep_df.loc[0])
rep_df.insert(dfLen, "destination_affiliation", dest_affiliation, False)


rep_df.head(30)

rep_df.to_csv('representatives_affiliations.csv', index=False)

