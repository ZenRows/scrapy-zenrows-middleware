import scrapy
from scrapy_zenrows import ZenRowsRequest


class PaginationSpider(scrapy.Spider):
    name = "pagination_spider"
    start_urls = ["https://www.scrapingcourse.com/ecommerce/"]
    handle_httpstatus_list = [404]  # handle 404 status codes
    page_count = 1

    def start_requests(self):
        for url in self.start_urls:
            # send initial request with ZenRows parameters
            yield ZenRowsRequest(
                url=url,
                callback=self.parse,
                params={
                    "js_render": "true",
                },
            )

    def parse(self, response):
        status = response.status

        # stop if 404 error (end of pagination)
        if status == 404:
            self.logger.info(
                f"Reached the end of pagination. Stopping at URL: {response.url}"
            )
            return

        # extract product data
        products = response.css("ul.products li.product")
        data = []

        for product in products:
            product_name = product.css("h2.woocommerce-loop-product__title::text").get()
            price = product.css("bdi::text").get()
            data.append({"product_name": product_name, "price": price})

        self.logger.info(f"Scraped {len(data)} products from page {self.page_count}")
        yield {"page": self.page_count, "products": data}

        # move to next page
        self.page_count += 1
        next_page = f"{self.start_urls[0]}page/{self.page_count}/"

        # request next page
        yield ZenRowsRequest(
            url=next_page,
            callback=self.parse,
            params={
                "js_render": "true",
                "premium_proxy": "true",
            },
        )
