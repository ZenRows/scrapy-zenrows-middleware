import scrapy
from scrapy_zenrows import ZenRowsRequest


class SimpleTableParsingSpider(scrapy.Spider):
    name = "table_parsing_spider"

    def start_requests(self):
        url = "https://www.scrapingcourse.com/table-parsing"
        # request table parsing with JavaScript rendering
        yield ZenRowsRequest(
            url=url,
            callback=self.parse,
            params={
                "js_render": "true",
                "outputs": "tables",
            },
        )

    def parse(self, response):
        # print the parsed table data
        print("Response:")
        print(response.text)
