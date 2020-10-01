import tweepy
import csv
import pandas as pd
consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('tweets.csv', 'a')
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search,q="#blacklivesmatter",count=50000,lang="en",since="2017-04-03").items(50000):
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
# Get your twitter developer account get a website then create app on twitter developer account 
# and you will have all 4(consumer_key= '',consumer_secret= '',access_token= '',access_token_secret= ''
# of your own and will able to run the code to scrape the tweets in tweets.csv as i did.  Enjoy the data....as now onwards data is money.....
