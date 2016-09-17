# Django-Twitter

This Django app is built to serve a pseudo-random tweet on the home page from a 
single twitter account of your choice.

As long as you want to use a cache to store your tweets this should be 
simple to modify to get it to do all sorts of things relating to serving tweets.
Let me know if you do something with this!

Django-Twitter stores all tweets in a redis cache. When a user visits the homepage,
it will check to see if it has updated the cache in the past 12 hours.

If it hasn't, it makes an api call to twitter to update the cache, and
then serves a pseudo-random tweet. If the cache has been updated lately, 
it will check to see how many tweets are in the cache, pick a random one, 
fetch it, and serve it in the ui. 

if you visit `/updateCache` in a browser it will make an api call and update
the cache. Useful if you have some recent tweets that you want to be thrown 
into the mix. 

## Setup

#### env vars:
* 'ENVIRONMENT' == ('prod', 'test', or 'dev') defaults to prod
* 'REDIS_URL' == your full redis url, no default
* 'SECRET_KEY' == a secret key, this will default to the one in the 
source code, so be sure that you change it. 

#### twitter config
* go to apps.twitter.com and make a new app
* edit `twitter_config_example.txt` to have keys
* rename to `twitter_config.txt`

## to do
* pick an open source license for this app and attach it
* serve a tweet from the cache if the api call fails
* require a password-like url param to hit `/updateCache`
* serve static assets from s3
* cache templates
* get twitter config values from env vars
