from TwitterAPI import TwitterAPI
from config import ConfigValues 
import json

class TwitterApiRequest:
    def __init__(self):
        self.api = TwitterAPI(consumer_secret=ConfigValues.Twitter.consumer_secret_key,
                            consumer_key=ConfigValues.Twitter.consumer_key,
                            access_token_key=ConfigValues.Twitter.token,
                            access_token_secret=ConfigValues.Twitter.token_secret)
    def get_tweets(self,query):
        hash_query = query + 'jobs'
        r = self.api.request('search/tweets', {'q':f'{hash_query}', 'count':20})
        print(r.status_code)
        resconvert = json.loads(r.text)
        resdict = resconvert['statuses']
        tweets_result = []
        for item in resdict:
            if item['retweeted']==False:
                tweet_item =  {}
                tweet_item['id_tweet'] = item.get('id')
                tweet_item['name'] = item.get('user').get('name')
                tweet_item['username'] = item.get('user').get('screen_name')
                tweet_item['url_bg'] = item.get('user').get('profile_image_url_https')
                tweet_item['tweet_id'] = item.get('id')
                tweet_item['user'] = item.get('user').get('name')
                tweet_item['text'] = item.get('text')
                tweets_result.append(tweet_item)
           
        return tweets_result


    
