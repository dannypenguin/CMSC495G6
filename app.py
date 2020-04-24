from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import gettweets

#initialize db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
data = []
# create db
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)# Tweet ID
    author = db.Column(db.String(50), nullable=False)# Twitter Username
    url = db.Column(db.String(500), nullable=False)# tweet url
    content = db.Column(db.String(200), nullable=False)# Tweet Content
    date_created = db.Column(db.DateTime, default=datetime.utcnow)# Date/time of tweet

    def __repr__(self):
        return '<Tweet %r>' % self.id

# Pull initial tweets
data = gettweets.get_tweets02("whitehouse")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        for tweet in data:
            new_tweet = Todo(id = tweet['tweet_id'], author = 'name', url = 'source_url', content = 'text', date_created = 'created_at')
            try:
                db.session.add(new_tweet)
                db.session.commit() # try adding all tweets and only doing one commit after loop
            except:
                return 'There was an issue adding your tweet'
        return redirect('/')
    
    else:
        tweets = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tweets=tweets)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
