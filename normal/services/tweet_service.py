import json
import twitter

def get_tweets():
    f = open('twitter_config.txt').read()
    twitter_settings = json.loads(f)

    api = twitter.Api(consumer_key=twitter_settings['consumer_key'],
                      consumer_secret=twitter_settings['consumer_secret'],
                      access_token_key=twitter_settings['access_token'],
                      access_token_secret=twitter_settings['access_token_secret'])

    twitter_results = api.GetUserTimeline(twitter_settings['twitter_user'])

    return twitter_results