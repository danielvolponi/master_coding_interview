#!usr/bin/env python3
"""Twitter
Imagine that you are working on twitter and you have to do
a feature that you click a button and retrive their most 
recent tweet and oldest tweet.

1. Find first and Find nth (last tweet)...
2. Compare the dates of the tweets 
"""

tweets = [{
    'tweet': 'hi',
    'date': 2012
    }, {
    'tweet': 'my',
    'date': 2014
    }, {
     'tweet': 'teddy',
    'date': 2018
     }]

# 1
print(tweets[0]) # O(1)
print(tweets[-1]) # O(1)
print("-" * 30)
# 2
# O(n^2) nested loops
for tweet_1 in tweets:
    print(tweet_1)
    for tweet_2 in tweets:
        if tweet_2["date"] > tweet_1["date"]: 
            print(tweet_2["date"] - tweet_1["date"])
