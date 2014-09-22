#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Carlos Jenkins'
SITENAME = u'carlos.jenkins.co.cr'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Costa_Rica'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins/', ]
PLUGINS = [
    'assets',
    'pelican_fontawesome',
    #'extract_toc',
    #'pelican_gist',
    #'pelican_vimeo',
    #'pelican_youtube',
]

# HAUNTR CONFIG
THEME = 'hauntr'
DIRECT_TEMPLATES = (('index', 'archives', '404'))
