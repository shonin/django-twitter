from random import randint
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache

import twitter

from normal.services.tweet_service import get_tweets

def rand_status(request):
    statuses = check_for_update()
    num_statuses = len(statuses)
    randnum = randint(0, num_statuses - 1)
    random = statuses[randnum]
    return render(request, 'idea/random.html', {'status': random} )

def check_for_update():
    now = datetime.now()
    twelve_hours_ago = now - timedelta(hours=12)
    cache_memory = cache.get('settings')

    if not cache_memory or cache_memory[1] <= twelve_hours_ago:
        """
        if there are no settings in the cache, or if the settings
        haven't been updated in more than 12 hours, fetch the new
        statuses, set them in the cache, return the statuses
        """
        twitter_results = get_tweets()

        cache.set('settings', [len(twitter_results), now])

        statuses = []
        for num, status in enumerate(twitter_results):
            cache.set(num, status.text)
            statuses.append(status.text)

        cache.close()
        return statuses
    else:
        num_statuses = cache_memory[0]
        i = 0
        list = []
        while i <= num_statuses:
           list.append(i)
           i += 1

        cached_results = cache.get_many(list)

        statuses = []
        for status in cached_results.values():
            statuses.append(status)

        cache.close()
        return statuses


def update_cache(request):
    try:
        api = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret,
                          access_token_key=access_token,
                          access_token_secret=access_token_secret)


        twitter_results = api.GetUserTimeline('normalidea')
        cache.set('settings', [len(twitter_results), datetime.now()])

        for num, status in enumerate(twitter_results):
            cache.set(num, status.text)

        cache.close()
        return HttpResponse('Cache Updated')

    except Exception as err:
        return HttpResponse('Unknown error:{err}').format(err = err)
