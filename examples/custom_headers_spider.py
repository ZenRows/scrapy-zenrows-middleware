import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_zenrows import ZenRowsRequest
import json


class SimpleCustomHeadersSpider(scrapy.Spider):
    name = "custom_headers_spider"

    # configure ZenRows API key and middleware
    custom_settings = {
        "ZENROWS_API_KEY": "<YOUR_ZENROWS_API_KEY>",
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy_zenrows.ZenRowsMiddleware": 543,
        },
    }

    def start_requests(self):
        url = "https://httpbin.io/headers"
        # send request with custom headers and cookies
        yield ZenRowsRequest(
            url=url,
            callback=self.parse,
            params={
                # "js_render": "true",
                "custom_headers": "true",
            },
            headers={
                "Referer": "https://www.google.com/",
            },
            cookies={"session_id": "123456", "user_id": "abcdef"},
        )

    def parse(self, response):
        # parse JSON response
        headers_received = json.loads(response.text)
        headers = headers_received.get("headers", {})

        # print custom headers received by the server
        print("Custom headers received by the server:")
        print(f"Referer: {headers.get('Referer')}")
        print(f"Cookie: {headers.get('Cookie')}")


if __name__ == "__main__":
    # start the crawler process
    process = CrawlerProcess()
    process.crawl(SimpleCustomHeadersSpider)
    process.start()
