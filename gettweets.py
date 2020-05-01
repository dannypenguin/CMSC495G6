import tweepy
from datetime import datetime

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = ""
consumer_secret = ""
access_key = "-"
access_secret = ""

# Function to extract tweets
def get_tweets02(username):
     # Authorization to consumer key and consumer secret
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

    # Calling api
    api = tweepy.API(auth)

    # hold tweets as python dicts
    data = []

    # Iterate thru tweets
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username, tweet_mode = 'extended').items(2):
        print(tweet.id)
        print(tweet.user.name)
        print(tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"))
        tweet_info = {
                    'tweet_id': tweet.id,
                    'name': tweet.user.screen_name,
                    #'screen_name': tweet.user.screen_name,
                    #'retweet_count': tweet.retweet_count,
                    'text': tweet.full_text,
                    #'time_read_at': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                    'created': tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                    #'favourite_count': tweet.favorite_count,
                    'source_url': tweet.source_url
                }
        data.append(tweet_info)
    return data