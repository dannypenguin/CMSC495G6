import tweepy
import datetime

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = ""
consumer_secret = ""
access_key = "-"
access_secret = ""

# Function to extract tweets
def get_tweets02(username):
     # Authorization to consumer key and consumer secret
    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    #auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    # hold tweets as python dicts
    data = []

    # Iterate thru tweets
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username, tweet_mode = 'extended').items(2):
        # limit age of tweet
       # if (datetime.datetime.now() - tweet.created_at.date).days > 2:
       #     break
        print(tweet.id)
        print(tweet.user.name)
        tweet_info = {
                    'tweet_id': tweet.id,
                    'name': tweet.user.screen_name,
                    #'screen_name': tweet.user.screen_name,
                    #'retweet_count': tweet.retweet_count,
                    'text': tweet.full_text,
                    #'time_read_at': datetime.datetime.now(),
                    #'created_at': tweet.created_at,
                    #'favourite_count': tweet.favorite_count,
                    #'hashtags': tweet.entities['hashtags'],
                    #'status_count': tweet.user.statuses_count,
                    #'location': tweet.place,
                    'source_url': tweet.source_url
                }
        data.append(tweet_info)
    return data