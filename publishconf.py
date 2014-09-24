#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

from .pelicanconf import *  # noqa

# Publish options
RELATIVE_URLS = False
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'

# Disqus
DISQUS_SITENAME = 'carlosjenkins'

# Google analytics
#GOOGLE_ANALYTICS = ""

# Publish extra plugins
PLUGINS.append('minify')
PLUGINS.append('sitemap')

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily',
    }
}
