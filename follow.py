import tweepy
import time
from userControl import follow

CONSUMER_KEY = 'R1PrxYTZ95iysyEbIdIWLPEZt'
CONSUMER_SECRET = '6N4fUwtdZcNPLX1tzqVarKEGfjFwqac1LBxVqFM1AvU9WJMlmC'
ACCESS_KEY = '1213366426557304834-iZEEbda4mMcn8UDNx6I0gxtflmxbdN'
ACCESS_SECRET = 'n93PNFB099yW5a3XOjqbZNe8y77jjWgTwbCECTZME6yGS'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def main():
    try:
        for follower in tweepy.Cursor(api.followers).items(10):
            if follower.follow_request_sent == False:
                follow(api, follower.screen_name)
    except tweepy.TweepError as e:
        print(e)
    time.sleep(45)
    main()
main()
