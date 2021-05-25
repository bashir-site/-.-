 pip install scrapy

# 1. news - парсер для "Новостей региона" по ссылке https://гибдд.рф/news/region
 запускается парсер коммандой scrapy crawl regions -o regions.json
 
 
# 2. allnews - парсер для "Новости регионов" по ссылке https://гибдд.рф/news/regional
 запускается парсер коммандой scrapy crawl allregions -o allregions.json
 
# 3. federal - парсер для "Федеральные новости" по ссылке https://гибдд.рф/news/federal
 запускается парсер коммандой scrapy crawl federal -o federal.json
 
