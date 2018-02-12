import scrapy


class QuotesSpider(scrapy.Spider):
    name = "hindustani"
    start_urls = ['http://www.hindustantimes.com/india-news/',
                  'http://www.hindustantimes.com/world-news/',
                  'http://www.hindustantimes.com/delhi-news/',
                  'http://www.hindustantimes.com/opinion/',
                  'http://www.hindustantimes.com/business-news/',
                  'http://www.hindustantimes.com/tech/',
                  'http://www.hindustantimes.com/education/',

    ]

    def parse(self, response):

        for quote in response.css('div.media div.media-heading.headingfour'):
            yield {
               # 'Date': quote.css('div.section-teaserlist div.
                # date::text').extract_first(),
                'date': quote.css('span.time-dt::text').extract_first(),             #date taken from <span class = "time-dt" of website

                'Headlines': quote.css('a::text').extract(),               # headlines is text
                'link': quote.css('a::attr(href)').extract_first(),       # to extract URL
            }







