import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_zenrows import ZenRowsRequest


class AntiBotBypassSpider(scrapy.Spider):
    name = "antibot_bypass_spider"

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
