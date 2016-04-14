from __future__ import unicode_literals

import tweepy

from blank import get_structure
from image import generate_image
from secrets import app_key, app_secret, token_key, token_secret


auth = tweepy.OAuthHandler(app_key, app_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)


def tweet():
    structure = get_structure()
    status = 'i am {}'.format(' '.join((unicode(s) for s in structure)))
    image = generate_image([segment.context() for segment in structure])
    api.update_with_media(image, status=status)


if __name__ == '__main__':
    tweet()