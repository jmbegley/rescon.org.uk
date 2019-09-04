# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'BCRC'
SITENAME = 'British Cave Rescue Council Conference'
#SITEURL = 'https://www.rescon.org.uk'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

THEME = 'pelican-plugins/pelican-bootstrap3'
BOOTSTRAP_THEME = 'lumen'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

#GITHUB_USER = 'jmbegley'
#GITHUB_SKIP_FORK = True

TWITTER_USERNAME = 'BCRCRescon'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tipue_search', 'filetime_from_git',
           'post_revision', 'i18n_subsites',
           'liquid_tags.img', 'liquid_tags.flickr']

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pygment highlighting scheme
PYGMENTS_STYLE = 'solarizeddark'

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = True
DISPLAY_BREADCRUMBS = True

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['extras', 'files', 'images']
EXTRA_PATH_METADATA = {}

FAVICON = 'extras/favicon.ico'
#BANNER = 'extras/banner.jpg'
#CUSTOM_CSS = 'extras/custom.css'

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# share posts
SHARIFF = True
SHARIFF_LANG = "en"
SHARIFF_SERVICES  = "[&quot;twitter&quot;,&quot;facebook&quot;,&quot;whatsapp&quot;]"
SHARIFF_THEME = "standard"
SHARIFF_ORIENTATION = "horizontal"

# Blogroll
LINKS = (('British Cave Rescue Council', 'https://www.caverescue.org.uk/'),
         ('Mendip Cave Rescue', 'https://www.mendipcaverescue.org/'),)

# Social widget
SOCIAL = (('buy tickets', 'https://rescon.eventbrite.co.uk', 'ticket'),
          ('facebook', 'https://www.facebook.com/ResCon19'),
          ('twitter', 'https://twitter.com/BCRCRescon'),
          ('rss', SITEURL + '/' + FEED_ALL_ATOM),
          ('email', 'mailto:james@rescon.org.uk', 'envelope'),)

DEFAULT_PAGINATION = 4

# post revision
GITHUB_URL = 'https://github.com/jmbegley/rescon.org.uk'
POST_REVISION_TEXT = "Post History:"
POST_HISTORY_MAX_COUNT = 3

# about me
SHOW_ABOUTME = True
AVATAR = "images/bcrc_logo.jpg"
ABOUT_ME = """
BCRC is the national representative body for voluntary cave rescue in the British Isles.
<br/><br/>
ResCon is the biennual BCRC cave rescue conference, with the next one to be held on Mendip in September 2019.
"""

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
