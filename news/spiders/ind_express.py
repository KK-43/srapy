import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.spider import BaseSpider,Rule
class QuotesSpider(scrapy.Spider):

    name = "express"          # name of spider to be called during execution

    start_urls = [
        'http://indianexpress.com/section/india/'
    ]
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.yt-uix-button-content a ::attr(href)')), callback="parse_page",
             follow=True),
    )

    def parse(self, response):



        for quote in response.css('div.articles'):                          # content taken from article(storyclass of manorama website
            yield {
                'Date': quote.css('div.date::text').extract_first(),    # date to be taken from section-teaserlist of website
                'Headlines': quote.css('div.title a::text').extract_first(),
                'link': quote.css('div.title a::attr(href)').extract()

               }

        NEXT_PAGE_SELECTOR = 'div.pagination a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        try:
            next_page = response.css('div.pagination a::attr(href)').extract()[0]

            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
        except IndexError:
            pass



