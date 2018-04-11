#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Roy G. Williams'
SITENAME = u'Roy G. Williams'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),
        )

# Social widget
SOCIAL = (
          ('twitter', 'http://www.twitter.com/roygwilliams'),
          ('You can add links in your config file', '#'),
          ('Another social link', '#'),
         )

DEFAULT_PAGINATION = 10
THEME = "pelican-theme"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['gravatar',]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# lannisport settings
SITELOGO = 'images/gravatar.jpeg'
SITETAGLINE = 'Father, Husband, Geek, and Firefighter'
SITEDESCR = 'By day I am I am the lonely Red Hatter of Southern WV. Outside of business hours, I advocate for FOSS, play with new tech, operate amature radios, and play firefighter--sometimes they even let me teach.'
GITHUB_URL = 'http://github.com/chopskxw'
LINKEDIN_URL = 'http://linkedin.com/in/roygwilliams'
TWITTER_URL = 'http://twitter.com/roygwilliams'
FACEBOOK_URL = 'http://facebook.com/roygwilliams'
LICENSE_NAME = 'GPL v3'
LICENSE_URL = 'https://github.com/chopskxw/chopskxw.github.io/blob/master/LICENSE'

# gravatar
AUTHOR_EMAIL = 'roygwilliams.kxw@gmail.com'
