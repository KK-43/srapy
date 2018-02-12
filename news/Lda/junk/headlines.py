# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from news.news.spiders.items import NewsItem
from scrapy.selector import Selector

class HeadlinesSpider(scrapy.Spider):
    name = 'headlines'                                       #Name of spider
    allowed_domains = ['www.thehindu.com']
    start_urls = ['http://www.thehindu.com/']


    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse(self, response):
        hxs = Selector(response)

        discovery = hxs.xpath('//div[@class="nextPage"]/table/tr[2]/td/a[contains(@title,"Next")]')  # to connect to the next link
        print len(discovery)

        print "Starting the actual file"
        items = hxs.xpath('//div[@class="resultCell"]')
        count = 0
        for newsItem in items:
            print newsItem

            url = newsItem.xpath('a/@href').extract()
            name = newsItem.xpath('a/text()').extract()
            count = count + 1
            print count
            print url[0]
            print name[0]

            print "\n"

        pass

    def parse_item(self, response):
        print('Processing..' + response.url)

        item_links = response.css('.large > .detailsLink::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)   # calling back parse function if the link is present

    def parse_detail_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
        source = response.css('.strong::text').extract()[0]

        item = NewsItem()
        item['title'] = title
        item['source'] = source
        item['url'] = response.url
        yield item

