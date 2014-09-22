#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Carlos Jenkins'
SITENAME = u'carlos.jenkins.co.cr'
SITEURL = 'http://carlos.jenkins.co.cr'

GITHUB_URL = 'https://github.com/carlos-jenkins'
GITHUB_SITE_URL = (
    'https://raw.githubusercontent.com/carlos-jenkins/'
    'carlos.jenkins.co.cr/master/content/'
)
DISQUS_SITENAME = 'carlosjenkins'

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

DISPLAY_PAGES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
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

# SAVE AS
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CATEGORY_URL = 'c/{slug}'
CATEGORY_SAVE_AS = 'c/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 't/{slug}'
TAG_SAVE_AS = 't/{slug}/index.html'

MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
