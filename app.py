from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import gettweets
import os

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "umuccmsc495group6project")
app.config["TWITTER_OAUTH_CLIENT_KEY"] = os.environ.get("TWITTER_OAUTH_CLIENT_KEY")
app.config["TWITTER_OAUTH_CLIENT_SECRET"] = os.environ.get("TWITTER_OAUTH_CLIENT_SECRET")

# testing
OAUTH_CLIENT_KEY = os.environ.get("TWITTER_OAUTH_CLIENT_KEY")
OAUTH_CLIENT_SECRET = os.environ.get("TWITTER_OAUTH_CLIENT_SECRET")

#initialize db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
data = [] # holds data to be input into the db

# create db
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)# db ID
    tweet_id = db.Column(db.Integer, nullable=False) # tweet id
    author = db.Column(db.String(50), nullable=False)# Twitter Username
    content = db.Column(db.String(200), nullable=False)# Tweet Content
    date_created = db.Column(db.String(50), nullable=False)# Date/time of tweet
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)# Date/time tweet is pulled into db

    def __repr__(self):
        return '<Tweet %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # call gettweets, need to add a list of users to iterate over
        data = gettweets.getTweets(OAUTH_CLIENT_KEY, OAUTH_CLIENT_SECRET)
        # iterate over each tweet stored in data and store in DB
        for tweet in data:
            # New row of data for DB
            new_tweet = Todo(tweet_id = tweet['tweet_id'], 
                            author = tweet['name'], 
                            content = tweet['text'],  
                            date_created = tweet['created'])
            try:
                db.session.add(new_tweet)
                db.session.commit() # try adding all tweets and only doing one commit after loop
                delete(90)# number of tweets
            except:
                print('ERROR: Database may be unavailable. There was an issue adding your tweet')
                #return 'ERROR: Database may be unavailable. There was an issue adding your tweet'
                return redirect('/')
        return redirect('/')
    
    else:
        tweets = Todo.query.order_by(Todo.id).all()
        return render_template('index.html', tweets = tweets)

@app.route('/', methods=['POST', 'GET'])
def delete(limit):
    row_count = Todo.query.count()
    while row_count > limit:
        first_tweet = Todo.query.order_by(Todo.timestamp.asc()).first()
        db.session.delete(first_tweet)
        db.session.commit()
        row_count = Todo.query.count()
    
if __name__ == "__main__":
    app.run(debug=True)
