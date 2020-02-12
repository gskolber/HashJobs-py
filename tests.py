import unittest
import re
from twitter_api import TwitterApiRequest

class TestGetTweets(unittest.TestCase):
    def setUp(self):
        self.tweets = ['teste gabriel' ,'GabrieL outro teste']
        self.twitter_api = TwitterApiRequest()
    def test_get_tweets(self):
        regex_string = re.compile('(?i)(gabriel.*?)')
        for tweet in self.tweets:
            self.assertRegex(tweet, regex_string, 'No matches found')
    def test_api_request(self):
        request = self.twitter_api.get_tweets('Gremio')
        self.assertIsNotNone(request)
        



    

    


if __name__ == '__main__':
    unittest.main()