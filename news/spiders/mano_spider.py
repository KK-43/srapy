import scrapy


class QuotesSpider(scrapy.Spider):

    name = "manorama"          # name of spider to be called during execution

    start_urls = [
        'http://english.manoramaonline.com/news.html',
        'http://english.manoramaonline.com/sports.html',
        'http://english.manoramaonline.com/business.html',
        'http://english.manoramaonline.com/wellness.html',
        'http://english.manoramaonline.com/lifestyle.html',
        'http://english.manoramaonline.com/entertainment.html',
        'http://travel.manoramaonline.com/travel.html',
        'http://english.manoramaonline.com/women.html'
    ]

    def parse(self, response):

        for quote in response.css('article.storyclass1'):                          # content taken from article(storyclass of manorama website
            yield {
                'Date': quote.css('div.section-teaserlist div.date::text').extract_first(),    # date to be taken from section-teaserlist of website
                'Headlines': quote.css('a::text').extract(),
                 'link': quote.css('a::attr(href)').extract()
                  }



