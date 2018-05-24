import json
from request
from requests_oauthlib import OAuth1Session

MAX_TWEETS = 100
BASE_URL = "https://api.twitter.com/1.1/search/tweets.json"


class MyTwitterSearchClient(object):
    # dados que pegamos na conta de deselvolvedor do twitter, única para cada API
    API_KEY = "NRuFvl2KkWxJ7tgvi29drHYkp"
    API_SECRET = "9anREniBRp97JuqyGqQoFpVruQKYXBsW3PNZ8WpMMXVHFQqple"
    ACCESS_TOKEN = "164438391-QpOwVPRMF95I6qT73iftvg0p1K2w05D8HjFyjd5x"
    ACCESS_TOKEN_SECRET = "RHVB2ruH0l2Zl28A1LTYLiTGOZJmOfvfkPQnGT195d0EU"

    def __init__(self):
        self.session = OAuth1Session(self.API_KEY,
                                     self.API_SECRET,
                                     self.ACCESS_TOKEN,
                                     self.ACCESS_TOKEN_SECRET)

    def get_tweets(self, keyword, n=15, max_id=None):
        if n > 0:
            url = BASE_URL + ("?q=%s&count=%d" % (keyword, n))
            if max_id is not None:
                url = url + "&max_id=%d" % (max_id)
            response = self.session.get(url)
            if response.status_code == 200:
                tweets = json.loads(response.content)
                #oldest_id = min(<!-- Invalid tweet id --> for tweet in tweets['statuses'])-1
                return tweets['statuses'] + \
                    self.get_tweets(keyword, n - MAX_TWEETS, oldest_id)
        return []