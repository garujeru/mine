#!/usr/bin/env python
# coding: utf-8

# In[1]:


twitter_consumer_key = "R1WOpaM9wfqtyYDHTT67QnERD"
twitter_consumer_secret = "y9LVJ5yjZqDsDKV6KzKlBn9JXb6Ho1l9Itc2HsKeBTZOls21rO"
twitter_access_token = "1588748986403655682-wPK0bNape69qdT1gxNyHeIDFGPaxzL"
twitter_access_secret = "9usIRtQcDotLJq5zK43ziiwooAOeeH4JGylwPQGyTrmqO"

import twitter

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                         consumer_secret=twitter_consumer_secret,
                         access_token_key=twitter_access_token,
                         access_token_secret=twitter_access_secret)


# In[6]:


account = "@sadd420"
statuses = twitter_api.GetUserTimeline(screen_name=account, count=5, include_rts=True, exclude_replies=False)

for status in statuses:
    print(status.text)


# In[7]:


account = "@seoul_metro"
statuses = twitter_api.GetUserTimeline(screen_name=account, count=200, include_rts=True, exclude_replies=False)

for status in statuses:
    print(status.text)


# In[ ]:




