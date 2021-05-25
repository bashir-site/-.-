import scrapy

# Федеральные новости
class FederalSpider(scrapy.Spider):
    name = 'federal'
    start_urls = [f'https://гибдд.рф/news/federal/{str(i+1)}/'for i in range(541)]

    def parse(self, response):
        for catalog in response.css('div.sl-item'):
            yield {
                'title': catalog.css('div.sl-item-title a::text').get(),
                'date': catalog.css('div.sl-item-date::text').get().strip(),
                # 'url':  catalog.css('sl-item-title a::attr(href)').get()
            }

        next_page = response.css('div.pages a::attr(href)').getall()

        if next_page is not None:
            yield response.follow(next_page, self.parse)


# Новости региона
class RegionNews(scrapy.Spider):
    name = 'region'
    start_urls = ['https://гибдд.рф/news/region/']

    def parse(self, response):
        for region in response.css('div.news-item sl-item clearfix'):
            yield {
                'title': region.css('div.sl-item-title a::text').get(),
                'date': region.css('div.sl-item-date::text').get().strip(),
            }
