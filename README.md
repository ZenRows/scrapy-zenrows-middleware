# ZenRows Middleware for Scrapy

This is a Scrapy middleware that allows easy integration with the ZenRows Scraper API for web scraping.

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
    "scrapy_zenrows.middleware.ZenRowsMiddleware": 543,
}

# ZenRows API Key
ZENROWS_API_KEY = "<YOUR_ZENROWS_API_KEY>"
```

#### Set Global Premium Proxy Rotation and JS Rendering

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
from scrapy_zenrows.zenrows_request import ZenRowsRequest

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

Check our [headers feature](https://docs.zenrows.com/scraper-api/features/headers) for more information on the accepted request headers and how to set them.
