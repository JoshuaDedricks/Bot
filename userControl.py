import tweepy
def follow (tweepyApiObject, handle):
    try:
        tweepyApiObject.create_friendship(screen_name = handle)
    except tweepy.TweepError as e:
        print(e)
        return -1
    return 0
