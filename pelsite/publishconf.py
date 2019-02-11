#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://leinadtv.github.io'
RELATIVE_URLS = False

M_BLOG_NAME = 'Blogging shit away'
M_BLOG_URL = 'blog/'

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Libre+Baskerville:400,400i,700,700i%7CSource+Code+Pro:400,400i,600',
               '/static/m-light.css']
M_THEME_COLOR = '#cb4b16'

PLUGIN_PATHS = ['m.css/pelican-plugins']
PLUGINS = ['m.htmlsanity']

M_FINE_PRINT = SITENAME + """. Powered by `Pelican <https://getpelican.com>`_
    and `m.css <https://mcss.mosra.cz>`_."""

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""