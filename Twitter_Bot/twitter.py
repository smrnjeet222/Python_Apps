import tweepy
import confidential as co
import time

auth = tweepy.OAuthHandler(co.api_key ,co.api_secret_key)

auth.set_access_token(co.access_token, co.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify= True)

user = api.me()

search = 'Python'
notweets = 100

for tweet in tweepy.Cursor(api.search, search).items(notweets):
    try:
        print ('Tweet liked')
        tweet.favorite()
        time.sleep(20)
    except tweepy.TweepError as e:
        print (e.reason)
    except StopIteration:
        break
    