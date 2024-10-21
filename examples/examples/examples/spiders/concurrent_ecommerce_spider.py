import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_zenrows import ZenRowsRequest
from scrapy.utils.log import configure_logging
import logging


class ConcurrentEcommerceSpider(scrapy.Spider):
    name = "concurrent_ecommerce_spider"

    # define multiple URLs to scrape concurrently
    start_urls = [
        "https://www.scrapingcourse.com/ecommerce/page/1/",
        "https://www.scrapingcourse.com/ecommerce/page/2/",
        "https://www.scrapingcourse.com/ecommerce/page/3/",
        "https://www.scrapingcourse.com/ecommerce/page/4/",
        "https://www.scrapingcourse.com/ecommerce/page/5/",
    ]

    # configure settings for concurrent requests, delays, and ZenRows
    custom_settings = {
        "CONCURRENT_REQUESTS": 5,  # set number of concurrent requests
        "DOWNLOAD_DELAY": 1,  # add delay between requests
    }

    def start_requests(self):
        for url in self.start_urls:
            # yield ZenRows request for each URL
            yield ZenRowsRequest(
                url=url,
                callback=self.parse,
                params={
                    "js_render": "true",
                    "premium_proxy": "true",
                    "custom_headers": "true",
                },
                meta={"url": url},  # pass URL to parse method
            )

    def parse(self, response):
        url = response.meta["url"]
        self.logger.info(f"Parsing URL: {url}")

        # extract product information
        products = response.css("ul.products li.product")
        data = []

        for product in products:
            product_name = product.css("h2.woocommerce-loop-product__title::text").get()
            price = product.css("bdi::text").get()
            data.append({"product_name": product_name, "price": price})

        self.logger.info(f"Extracted {len(data)} products from {url}")
        yield {"url": url, "products": data}
