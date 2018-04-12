#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

TYPOGRIFY = True

AUTHOR = u'Roy G. Williams'
SITENAME = u'Roy G. Williams'
SITEURL = 'https://chopskxw.github.io'

# lannisport settings
SITELOGO = 'images/gravatar.jpeg'
SITETAGLINE = u'Father, Husband, Geek, and Firefighter'
SITEDESCR = u'By day I am I am the lonely Red Hatter of Southern WV. Outside of business hours, I advocate for FOSS, play with new tech, operate amature radios, and play firefighter--sometimes they even let me teach.'
GITHUB_URL = 'http://github.com/chopskxw'
LINKEDIN_URL = 'http://linkedin.com/in/roygwilliams'
TWITTER_URL = 'http://twitter.com/roygwilliams'
FACEBOOK_URL = 'http://facebook.com/roygwilliams'
LICENSE_NAME = 'GPL v3'
LICENSE_URL = 'https://github.com/chopskxw/chopskxw.github.io/blob/master/LICENSE'

THEME = "pelican-theme"
MAIN_MENU = True
#PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['gravatar',]

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10
#PATH = 'content'
STATIC_PATHS = [
    'files',
    'images',
    'cv',
]

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = ARCHIVES_URL + 'index.html'

CONTACT_URL = 'pages/contact/'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# gravatar
#AUTHOR_EMAIL = 'roygwilliams.kxw@gmail.com'
