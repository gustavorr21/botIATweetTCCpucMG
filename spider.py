import tweepy
import json
import csv
import time

bearer_token = 'bearer_token'
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = []
search = '#ViraViraCIRO OR #17Neles OR #EleNão OR #FraudeNasUrnasEletrônicas OR #LulaNoPrimeiroTurno OR #Lula2022 -filter:retweets'
c = tweepy.Cursor(api.search_tweets, q=search,since='2022-01-01', tweet_mode='extended', until='2022-12-31', count=100, wait_on_rate_limit = True, wait_on_rate_limit_notify=True).items(10000)

while True:
    try:
        t = c.next()._json
        tweets.append(t)
    except tweepy.TwitterServerError:
        time.sleep(60)
        continue
    except StopIteration:
        break

with open('twitter.json','w') as f:
    f.write(json.dumps(tweets))
