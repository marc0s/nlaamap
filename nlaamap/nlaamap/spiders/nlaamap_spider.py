# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from nlaamap.items import PersonItem

import simplejson as json

class NlaamapSpider(BaseSpider):
    name = "nlaamap"
    allowed_domains = ['nolesayudesamandarmealparo.com']
    start_urls = ['http://www.nolesayudesamandarmealparo.com/index.php']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        people = hxs.select('//li')
        items = []
        stats = {}
        for person in people:
            _line = person.select('text()').extract()[0].split(',')
            item = PersonItem()
            item['name'] = _line[0].strip()
            item['occupation'] = _line[1].strip() or u'Sin profesión'
            items.append(item)
            # do stats (NOTE: check for empty occupation)
            if not stats.has_key(item['occupation']):
                stats[item['occupation']] = {'count': 0, } #'values': []}
            # stats[item['occupation']]['values'].append(item['name'])
            stats[item['occupation']]['count'] += 1
            fp = open('/tmp/nlaamap-stats.json', 'w')
            fp.write(json.dumps(stats, sort_keys=True, indent=2 * ' '))
            fp.close()
        return items

