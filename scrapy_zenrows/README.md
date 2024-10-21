# Scrapy_ZenRows Middleware

This is a Scrapy middlware that provides an interface for interacting with the ZenRows® Scraper API in your Scrapy spiders. It lets you enjoy all the features of the ZenRows® Scraper API while using scrapy.

## Introduction

The ZenRows® Scraper API is an all-in-one toolkit designed to simplify and enhance the process of extracting data from websites. Whether you’re dealing with static or dynamic content, our API provides a range of features to meet your scraping needs efficiently.

With Premium Proxies, ZenRows gives you access to over 55 million residential IPs from 190+ countries, ensuring 99.9% uptime and highly reliable scraping sessions. Our system also handles advanced fingerprinting, header rotation, and IP management, **enabling you to scrape even the most protected sites without needing to manually configure these elements**.

ZenRows makes it easy to bypass complex anti-bot measures, handle JavaScript-heavy sites, and interact with web elements dynamically — all with the right features enabled.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

  - [Global Settings](#global-settings)
    - [Set Global Premium Proxy and JS Rendering](#set-global-premium-proxy-and-js-rendering)
    - [Override Global Settings for Specific Requests](#override-global-settings-for-specific-requests)
    - [Other Request Parameters](#other-request-parameters)
    - [Using Custom Headers](#using-custom-headers)
    - [Adding the Cookies Header](#adding-the-cookies-header)

- [Usage Examples](#usage-examples)

## Installation

```bash
pip install scrapy-zenrows
```

## Usage

- Sign up for free on [ZenRows](https://www.zenrows.com/) to open the Request Builder and copy your ZenRows API key and implement the middleware.

### Global Settings

- Add the ZenRows Scraper API middleware to your `DOWNLOADER_MIDDLEWARE` and specify your ZenRows API Key:

_settings.py_

```python
DOWNLOADER_MIDDLEWARES = {
    "scrapy_zenrows.ZenRowsMiddleware": 543,
}

# ZenRows API Key
ZENROWS_API_KEY = "<YOUR_ZENROWS_API_KEY>"
```

#### Set Global Premium Proxy and JS Rendering

The middleware will not use premium proxy and JS rendering by default. So, `USE_ZENROWS_PREMIUM_PROXY` and `USE_ZENROWS_JS_RENDER` are `False` by default. To turn on premium proxy and JS rendering globally, set both parameters to `True`:

_settings.py_

```python
# ...

USE_ZENROWS_PREMIUM_PROXY = True # to turn on premium proxy (False by default)
USE_ZENROWS_JS_RENDER = True # to turn on JS rendering (False by default)
```

### Override Global Settings for Specific Requests

If you have multiple spiders and don't want to apply global premium proxy and JS rendering for all, you can apply the middleware to specific ones by using `ZenRowsRequest` in `start_requests`.

`ZenRowsRequest` accepts the URL, request params, and headers options.

For example, to set Premium Proxy and JS Rendering for a specific request:

```python
# pip install scrapy-zenrows
from scrapy_zenrows import ZenRowsRequest

class YourSpider(scrapy.Spider):
    # ...

    def start_requests(self):
        # use ZenRowsRequest for customization
        for url in self.start_urls:
            yield ZenRowsRequest(
                url=url,
                # overrides the settings config for this specific spider
                params={
                    "js_render": "true",  # enable JavaScript rendering (if needed)
                    "premium_proxy": "true",  # use the proxy (if needed)
                },
            )

    def parse(self, response):
        # ...
```

#### Other Request Parameters

In addition to `js_render` and `premium_proxy`, the `ZenRowsRequest` accepts other parameters accepted by the ZenRows Scraper API:

```python
# ...
class YourSpider(scrapy.Spider):
    # ...

    def start_requests(self):
        # use ZenRowsRequest for customization
        for url in self.start_urls:
            yield ZenRowsRequest(
                url=url,
                params={
                    # ...,
                    "proxy_country": "ca", # use proxy from a specific country
                    "js_instructions": '[{"wait": 500}]', # pass JS instructions
                    "autparse": "true", # for supported websites
                    "outputs": "tables" # extract specific data,
                    'css_extractor': '{"links":"a @href","images":"img @src"}'
                    ""
                },
            )
```

For more information and supported parameters, check out our [Scraper API features](https://docs.zenrows.com/scraper-api/features/).

#### Using Custom Headers

You must set the `custom_headers` parameter to true in your request to use customized headers. This tells ZenRows to include your custom headers while managing critical browser-based headers.

For example, the following adds the referer header:

```python
# ...
class YourSpider(scrapy.Spider):
    # ...

    def start_requests(self):
        # use ZenRowsRequest for customization
        for url in self.start_urls:
            yield ZenRowsRequest(
                url=url,
                # overrides the settings config for this specific spider
                params={
                    "custom_headers": "true",  # to use custom headers
                },
                # add a referer header
                headers={
                    "Referer": "https://www.google.com/",
                },
            )
```

#### Adding the Cookies Header

Pass Cookies as a meta parameter (separated from the `headers`) just as specified by Scrapy. However, `custome_headers` must also be set to true.

```python
# ...
class YourSpider(scrapy.Spider):
    # ...

    def start_requests(self):
        # use ZenRowsRequest for customization
        for url in self.start_urls:
            yield ZenRowsRequest(
                url=url,
                # overrides the settings config for this specific spider
                params={
                    "custom_headers": "true",  # to use custom headers
                },
                cookies={
                    "currency": "USD",
                    "country": "UY",
                },
            )
```

Check our [headers feature](https://docs.zenrows.com/scraper-api/features/headers) for more information on the accepted request headers and how to set them.

## Usage Examples

Here are example spider demonstrating how to use the `scrapy_zenrows` middleware:

- **[antibot_bypass_spider](https://github.com/ZenRows/scrapy-zenrows-middleware/blob/main/examples/examples/examples/spiders/antibot_bypass_spider.py)**: Demonstrates the basic usage of the ZenRows Scraper API for bypassing anti-bots.
- **[concurrent_ecommerce_spider](https://github.com/ZenRows/scrapy-zenrows-middleware/blob/main/examples/examples/examples/spiders/concurrent_ecommerce_spider.py)**: Scraping concurrently with Scrapy while using `ZenRowsRequest`.
- **[custom_headers_spider](https://github.com/ZenRows/scrapy-zenrows-middleware/blob/main/examples/examples/examples/spiders/custom_headers_spider.py)**: Shows how to specify custom headers, including Cookies while using `ZenRowsRequest`.
- **[pagination_spider](https://github.com/ZenRows/scrapy-zenrows-middleware/blob/main/examples/examples/examples/spiders/pagination_spider.py)**: Shows how to implement pagination in Scrapy while using `ZenRowsRequest`.
- **[screenshot_spider](https://github.com/ZenRows/scrapy-zenrows-middleware/blob/main/examples/examples/examples/spiders/screenshot_spider.py)**: Demonstrates how to add screenshot capability to Scrapy with the ZenRows Scraper API.
- **[table_parsing_spider](https://github.com/ZenRows/scrapy-zenrows-middleware/blob/main/examples/examples/examples/spiders/table_parsing_spider.py)**: Examples showing how to parse a table using the `outputs` feature of the ZenRows Scraper API. Check the [supported outputs](https://docs.zenrows.com/scraper-api/features/output) for more information.

Examples directory: [examples](https://github.com/ZenRows/scrapy-zenrows-middleware/blob/main/examples/examples/examples/spiders/)

👉🏼 **[Official scrapy-zenrows integration documentation](https://docs.zenrows.com/scraping-api/integrations/scrapy)**
