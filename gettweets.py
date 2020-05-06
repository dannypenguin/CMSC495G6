import tweepy
from datetime import datetime

usernamelist = ["GovLarryHogan", "GavinNewsom", "CDCgov", "WHO", "WhiteHouse", "NIAIDNews"]
numberOfTweets = 10

# hold tweets as python dicts
data = []

def getTweets(CLIENT_KEY, CLIENT_SECRET):
    '''
    user id list: Governor Larry Hogan, Gavin Newsom, CDC, World Health Organization (WHO), 
    The White House, NIAID News, NIH, HHSGov, CDCemergency
    '''

    try:
        # Authorization to consumer key and consumer secret
        auth = tweepy.AppAuthHandler(CLIENT_KEY, CLIENT_SECRET)
        # Calling api
        api = tweepy.API(auth)
    except:
        print("Error: Missing API keys")

    # holds user ids
    useridlist = [2987671552, 11347122, 146569971, 
                    14499829, 822215673812119553, 59769395,
                    15134240, 44783853, 19658936]
    # Iterate thru Users
    for userid in useridlist: 
            # Iterate thru tweets
        for tweet in tweepy.Cursor(api.user_timeline, user_id = userid, tweet_mode = 'extended').items(numberOfTweets):
            
            tweet_info = {
                    'tweet_id': tweet.id,
                    'name': tweet.user.screen_name,
                    'text': tweet.full_text,
                    'created': tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S")
                }
            data.append(tweet_info)
    return data
        

