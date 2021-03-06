# Scrapy settings for nlaamap project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

BOT_NAME = 'nlaamap'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['nlaamap.spiders']
NEWSPIDER_MODULE = 'nlaamap.spiders'
DEFAULT_ITEM_CLASS = 'nlaamap.items.NlaamapItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

