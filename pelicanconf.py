#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Metadata
AUTHOR = 'Carlos Jenkins'
SITENAME = 'carlos.jenkins.co.cr'
SITEURL = 'http://carlos.jenkins.co.cr'

# Basic config
PATH = 'content'
DEFAULT_LANG = 'en'
TIMEZONE = 'America/Costa_Rica'

# GitHub config
GITHUB_URL = 'https://github.com/carlos-jenkins'
GITHUB_SITE_URL = (
    'https://raw.githubusercontent.com/carlos-jenkins/'
    'carlos.jenkins.co.cr/master/content/'
)

# Basic theme config
LINKS = ()
SOCIAL = ()
DEFAULT_PAGINATION = 20
DISPLAY_PAGES_ON_MENU = False

# Hauntr config
THEME = 'hauntr'
DIRECT_TEMPLATES = (('index', 'archives', '404'))

# Entities save options
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CATEGORY_URL = 'c/{slug}'
CATEGORY_SAVE_AS = 'c/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 't/{slug}'
TAG_SAVE_AS = 't/{slug}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

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

# Publish options
RELATIVE_URLS = True
FEED_ATOM = None
FEED_RSS = None

# Disqus
DISQUS_SITENAME = ''
