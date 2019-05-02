# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:25:31 2019

@author: Garry
"""

import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data = []
tweets=[]
tweets_file = open('twitter_data1.txt', "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

for i in tweets_data:
  if 'text' in i:
    tweets.append(i['text'])



with open("rawdata3.txt", "w",encoding="utf-8") as file:
    file.write(str(tweets))



