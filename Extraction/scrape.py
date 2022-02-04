from xmlrpc.client import _datetime
import snscrape.modules.twitter as twitterScrape
import json

scraper = twitterScrape.TwitterUserScraper("KMbappe")
tweets = []

for i,tweet in enumerate(scraper.get_items()):
    if i > 1000:
        break
    tweets.append({"id" : tweet.id, "Content": tweet.content , "Username" : tweet.user.username })
    
f = open("MbappeTweets.json","w")
j = json.dumps(tweets)
f.write(j)
f.close
#print(f"{i} content: {tweet.content}") pour afficher sur la console 
#tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) pour afficher  DateTime, tweet id, text, and username from the tweet object.