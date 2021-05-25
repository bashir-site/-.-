from datetime import datetime
import scrapy
import json
import math


class AllNews(scrapy.Spider):
    name = 'allregions'

    headers = {
        "x-requested-with": "xmlhttprequest"
    }

    def start_requests(self):
        urls = ['https://xn--90adear.xn--p1ai/news/regional?perPage=20&page=1&region=77']
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)


    def parse(self, response):
        raw_json = response.body
        data = json.loads(raw_json)
        pag = data["paginator"]
        total_pages = math.ceil(pag["total"] / pag["perPage"])
        for page in range(total_pages):
            yield scrapy.Request(
                f"https://xn--90adear.xn--p1ai/news/regional?perPage=20&page={page+1}&region=77",
                callback=self.parse_news,
                headers=self.headers,
            )

    def parse_news(self, response):
        data = json.loads(response.body)
        for d in data["data"]:
            yield {
                'Title': d['title'],
                'Date': datetime.fromtimestamp(d['datetime']).strftime('%m-%d-%Y'),
                'Link': f'https://xn--90adear.xn--p1ai/r/68/news/item/{d["id"]}',
            }