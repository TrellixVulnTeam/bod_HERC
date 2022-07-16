import tweepy

# token for twitter developers
client = tweepy.Client(
    bearer_token="<bearer_token>",
    consumer_key="<consumer_key>",
    consumer_secret="<consumer_secret>",
    access_token="<access_token>",
    access_token_secret="<access_token_secret>",
)

# find tweet by id
def tweet_downloader(id):
    tweet = client.get_tweet(id=id)
    return tweet
