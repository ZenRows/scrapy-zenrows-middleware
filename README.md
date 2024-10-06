# ZenRows Middleware for Scrapy

This is a Scrapy middleware that allows easy integration with the ZenRows Scraper API for web scraping.

## Installation

```bash
pip install zenrows_scrapy_middleware
```

## Usage

- Sign up for free on [ZenRows](https://www.zenrows.com/) to open the Request Builder and copy your ZenRows API key and implement the middleware.

- Add the ZenRows Scraper API middleware to your `DOWNLOADER_MIDDLEWARE` and specify your ZenRows API Key:

_settings.py_

```python
DOWNLOADER_MIDDLEWARES = {
    "zenrows_scrapy_middleware.middleware.ZenRowsMiddleware": 543,
}

# ZenRows API Key
ZENROWS_API_KEY = "<YOUR_ZENROWS_API_KEY>"
```

## Use Premium Proxy Rotation Feature

The middleware will not use premium proxy by default. So, `USE_ZENROWS_PROXY` is `False` by default. To turn on premium proxy, set `USE_ZENROWS_PROXY = True`:

_settings.py_

```python
# ...

USE_ZENROWS_PROXY = True # to turn on premium proxy (False by default)
```
