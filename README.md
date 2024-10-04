# ZenRows Middleware for Scrapy

This is a Scrapy middleware that allows easy integration with the ZenRows Scraper API for web scraping.

## Installation

```bash
pip install zenrows_middleware
```

## Usage

- Sign up for free on ZenRows to open the Request Builder and copy your ZenRows API key and implement the middleware

- Add the ZenRows Scraper API middleware to your `DOWNLOADER_MIDDLEWARE` and specify your ZenRows API Key:

**Note**: The middleware will use premium proxy by default. So, `USE_ZENROWS_PROXY` is True by default and you don't have to do anything to use premium proxy mode. To turn off premium proxy, set `USE_ZENROWS_PROXY` to False.

settings.py

```
DOWNLOADER_MIDDLEWARES = {
    # "my_scraper.middlewares.ZenRowsMiddleware": 543,  # Set the priority appropriately
    "zenrows_scraper_api_middleware.middleware.ZenRowsMiddleware": 543,
}

# ZenRows API Key
ZENROWS_API_KEY = "<YOUR_ZENROWS_API_KEY>"

USE_ZENROWS_PROXY = False # to turn off premium proxy
```
