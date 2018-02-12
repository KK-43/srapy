import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.spider import BaseSpider,Rule
class QuotesSpider(scrapy.Spider):

    name = "expresst"          # name of spider to be called during execution

    start_urls = [
        'http://indianexpress.com/section/india/'
    ]
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('div.pagination a ::attr(href)')), callback="self.parse",
             follow=True),
    )

    def parse(self, response):



        for quote in response.css('div.articles'):                          # content taken from article(storyclass of manorama website
            yield {
                'Date': quote.css('div.date::text').extract_first(),    # date to be taken from section-teaserlist of website
                'Headlines': quote.css('div.title a::text').extract_first(),
                'link': quote.css('div.title a::attr(href)').extract()

               }

