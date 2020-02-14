from flask import Flask, render_template, request
import requests
import json
from twitter_api import TwitterApiRequest


app = Flask(__name__)



@app.route('/')
def index_start():
    return render_template('index.html')
    
@app.route('/dashboard', methods = ['POST'])
def dashboard_start():
    tag = request.form.get('search')
    print(tag)
    api = TwitterApiRequest()
    list_tags = api.get_tweets(tag)   
    return render_template('dashboard.html', list_tags=list_tags)


if __name__ == '__main__':
    from os import environ
    host = '0.0.0.0'
    app.run(host = host, port=environ.get("PORT", 5000))

