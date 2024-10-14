import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_zenrows import ZenRowsRequest


class AntiBotBypassSpider(scrapy.Spider):
    name = "antibot_bypass_spider"

    # configure settings for ZenRows API and middleware
    custom_settings = {
        "ZENROWS_API_KEY": "<YOUR_ZENROWS_API_KEY>",
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy_zenrows.ZenRowsMiddleware": 543,
        },
    }

    def start_requests(self):
        url = "https://www.scrapingcourse.com/antibot-challenge"
        yield ZenRowsRequest(
            url=url,
            callback=self.parse,
            params={
                "js_render": "true",  # enable JavaScript rendering
                "premium_proxy": "true",  # use premium proxy
                "custom_headers": "true",  # activate custom headers
                "js_instructions": '[{"wait": 500}]',  # wait 500ms after page load
            },
            # add custom referer header
            headers={
                "Referer": "https://www.google.com/",
            },
        )

    def parse(self, response):
        # log the response body
        self.logger.info("Body:")
        self.logger.info(response.text)


if __name__ == "__main__":
    # configure and start the crawler process
    process = CrawlerProcess(
        settings={
            "LOG_LEVEL": "INFO",
            "FEEDS": {
                "output.json": {"format": "json", "overwrite": True},
            },
        }
    )
    process.crawl(AntiBotBypassSpider)
    process.start()
