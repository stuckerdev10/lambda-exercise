#!/usr/bin/env python
# coding: utf-8

# In[61]:


import csv
with open("911_Calls_for_Service_(Last_30_Days).csv") as f:
    a = [{x: y for x, y in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]


# In[62]:


print(a[6])


# In[70]:


clean_calls = list(filter((lambda x: x['neighborhood'] != '' and x['zip_code'] != ''                          and x['totalresponsetime'] != '' and x['totaltime'] != ''                          and x['dispatchtime'] != ''), a))


# In[64]:


len(clean_calls)


# In[65]:


from functools import reduce


# In[67]:


sum_totalresponsetime = reduce(lambda x, y: float(x) + float(y['totalresponsetime']), clean_calls, 0)
avg_totalresponsetime = sum_totalresponsetime / len(clean_calls)
print(avg_totalresponsetime)


# In[69]:


sum_totaltime = reduce(lambda x, y: float(x) + float(y['totaltime']), clean_calls, 0)
avg_totaltime = sum_totaltime / len(clean_calls)
print(avg_totaltime)


# In[73]:


neighborhood_list = []
for x in clean_calls:
    if x['neighborhood'] not in neighborhood_list:
        neighborhood_list.append(x['neighborhood'])


# In[78]:


neighborhood_stats = []
for n in neighborhood_list:
    sublist = list(filter(lambda x: x['neighborhood'] == n, clean_calls))
    avg_trt = (reduce(lambda x, y: x + float(y['totalresponsetime']), sublist, 0))/len(sublist)
    avg_dt = (reduce(lambda x, y: x + float(y['dispatchtime']), sublist, 0))/ len(sublist)
    avg_tt = (reduce(lambda x, y: x + float(y['totaltime']), sublist, 0))/len(sublist)
    
    stats_dict = {'neighborhood': n, 'avg_totalresponsetime': avg_trt,                 'avg_dispatchtime': avg_dt, 'avg_totaltime': avg_tt}
    neighborhood_stats.append(stats_dict)
    
    print('-------------------------------------------')
    print("Avg. total response time for {0}: {1:.2f}".format(n, avg_trt))
    print("Avg dispatch time for {0}: {1:.2f}".format(n, avg_dt))
    print("Avg total time for {0}: {1:.2f}".format(n, avg_tt))


# In[80]:


import json
json_file = open("detroit_stats.json", "w")
json_file = json.dump(neighborhood_stats, json_file)


# In[ ]:




