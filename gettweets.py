import tweepy

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = ""
consumer_secret = ""
access_key = "-"
access_secret = ""

# Function to extract tweets


def get_tweets(username):

    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    # 200 tweets to be extracted
    number_of_tweets = 200

    # Page to start
    page = 1

      # flag
    stop = False

    # hold tweets as python dicts
    data = []

    while True:
        # Pull first page of user's recent tweets
        tweets = api.user_timeline(screen_name=username, page=page)

        for tweet in tweets:
                tweet_info = {
                    'tweet_id': tweet.id,
                    'name': tweet.user.name,
                    'screen_name': tweet.user.screen_name,
                    'retweet_count': tweet.retweet_count,
                    'text': tweet.full_text,
                    'mined_at': datetime.datetime.now(),
                    'created_at': tweet.created_at,
                    'favourite_count': tweet.favorite_count,
                    'hashtags': tweet.entities['hashtags'],
                    'status_count': tweet.user.statuses_count,
                    'location': tweet.place,
                    'source_device': tweet.source
                }

            if(datetime.datetime.now() - tweet.created_at).days > 2:
                flag = True
                data.append(tweet_info)
                return

        if not flag:
            page++
            data.append(tweet_info)

return data


# Driver code
if __name__ == '__main__':

    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("whitehouse")
