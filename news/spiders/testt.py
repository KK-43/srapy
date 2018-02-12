import scrapy


class QuotesSpider(scrapy.Spider):
    name = "thehindu"
    start_urls = [
        'http://www.thehindubusinessline.com/economy/logistics/',
        'http://www.thehindubusinessline.com/economy/macro-economy/',
        'http://www.thehindubusinessline.com/economy/agri-business/',
        'http://www.thehindubusinessline.com/economy/policy/',
        'http://www.thehindubusinessline.com/money-and-banking/',
        'http://www.thehindubusinessline.com/companies/',
        'http://www.thehindubusinessline.com/markets/',
        'http://www.thehindubusinessline.com/news/',
        'http://www.thehindubusinessline.com/news/national/',
        'http://www.thehindubusinessline.com/news/science/',
        'http://www.thehindubusinessline.com/news/sports/',
        'http://www.thehindubusinessline.com/news/world/',
        'http://www.thehindubusinessline.com/news/variety/',
        'http://www.thehindubusinessline.com/news/education/',
        'http://www.thehindubusinessline.com/news/real-estate/'
    ]

    def parse(self, response):

        for quote in response.css('div.sub-headline'):      # data residing in sub-headline part
            yield {
                'Date': quote.css('div.section-teaserlist div.date::text').extract_first(),
                'Headlines': quote.css('a::text').extract_first(),     #selecting text content

                 'url' :quote.css('a::attr(href)').extract_first(),          # to extract URL

            }

        for quote in response.css('div.section-columns'):
            yield {
                'Date': quote.css('div.section-teaserlist div.date::text').extract_first(),

                'Headlines': quote.css('a::text').extract_first(),
                 'url': quote.css('a::attr(href)').extract_first(),

            }
