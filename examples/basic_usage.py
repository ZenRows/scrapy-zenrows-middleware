import scrapy
from scrapy.crawler import CrawlerProcess


class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["https://www.scrapingcourse.com/cloudflare-challenge"]

    custom_settings = {
        # put the following in your settings.py file
        "ZENROWS_API_KEY": "<YOUR_ZENROWS_API_KEY>",
        "DOWNLOADER_MIDDLEWARES": {
            "zenrows_scrapy_middleware.middleware.ZenRowsMiddleware": 543,
        },
        "USE_ZENROWS_PROXY": True,  # False by default
    }

    def parse(self, response):
        # extract product names and prices
        print(response.text)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()
