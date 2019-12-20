from flask import Flask, render_template, request, Response, jsonify
import numpy as np
import pickle
import os
import time
import pandas as pd


app = Flask(__name__)

# define the route
@app.route('/')
# create the controller
def home():
   # return the view
   return render_template('index.html', result_Css = '', result_logo = 'twitter-logo', result_message = 'No Emergency')


@app.route('/data')
# create the controller
def data():
    tweets = pd.read_csv(os.getcwd() + '/assets/alert_classifications.csv')
    tweets_list = []
    for i in range(len(tweets)):
        tweet_dict = {}
        tweet_dict['time'] = tweets.iloc[i,0]
        tweet_dict['emergency'] = str(tweets.iloc[i,1])
        tweets_list.append(tweet_dict)
    return jsonify(tweets_list)


@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

if __name__ == "__main__":
    app.run(debug=True)
