import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_zenrows import ZenRowsRequest


class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["https://www.scrapingcourse.com/cloudflare-challenge"]

    custom_settings = {
        # put the following in your settings.py file
        "ZENROWS_API_KEY": "<YOUR_ZENROWS_API_KEY>",
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy_zenrows.ZenRowsMiddleware": 543,
        },
        "USE_ZENROWS_PREMIUM_PROXY": True,  # False by default
        "USE_ZENROWS_JS_RENDER": True,  # False by default
    }

    def start_requests(self):
        # use ZenRowsRequest for customization
        for url in self.start_urls:
            yield ZenRowsRequest(
                url=url,
                # overrides the settings config for this specific spider
                params={
                    "js_render": "true",  # enable JavaScript rendering (if needed)
                    "premium_proxy": "true",  # use the proxy (if needed)
                    "custom_headers": "true",  # to activate custom headers
                    "js_instructions": '[{"wait": 500}]',  # customize as required
                },
                # add a referer header (custome_headers must be true)
                headers={
                    "Referer": "https://www.google.com/",
                },
                cookies={
                    "currency": "USD",
                    "country": "UY",
                },
            )

    def parse(self, response):
        print(response.text)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()
