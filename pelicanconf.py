#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Roy G. Williams'
SITEURL = 'http://chopskxw.github.io'
SITENAME = 'Roy G. Williams'
SITETITLE = 'Roy G. Williams'
SITESUBTITLE = 'Father, Husband, Geek, and Firefighter'
SITELOGO = SITEURL + 'images/gravatar.jpeg'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2018

EXTRA_PATH_METADATA = {
}

MAIN_MENU = True

THEME = "pelican-theme"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['gravatar',]

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10
PATH = 'content'

# Social widget
SOCIAL = (
        ('twitter', 'http://twitter.com/roygwilliams'),
        ('facebook', 'https://www.facebook.com/roygwilliams'),
        ('linkedin', 'https://www.linkedin.com/in/roygwilliams'),
        ('github', 'http://github.com/chopskxw'),
    )

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# gravatar
#AUTHOR_EMAIL = 'roygwilliams.kxw@gmail.com'
