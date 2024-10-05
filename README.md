# ZenRows Middleware for Scrapy

This is a Scrapy middleware that allows easy integration with the ZenRows Scraper API for web scraping.

## Installation

```bash
pip install zenrows_scrapy_middleware
```

## Usage

- Sign up for free on [ZenRows](https://www.zenrows.com/) to open the Request Builder and copy your ZenRows API key and implement the middleware

- Add the ZenRows Scraper API middleware to your `DOWNLOADER_MIDDLEWARE` and specify your ZenRows API Key:

_settings.py_

```
DOWNLOADER_MIDDLEWARES = {
    "zenrows_scrapy_middleware.middleware.ZenRowsMiddleware": 543,
}

# ZenRows API Key
ZENROWS_API_KEY = "<YOUR_ZENROWS_API_KEY>"
```

## Use Premium Proxy Rotation Feature

The middleware will use premium proxy by default. So, `USE_ZENROWS_PROXY` is `True` by default and you don't have to do anything to use premium proxy mode. To turn off premium proxy, use `USE_ZENROWS_PROXY = False`:

_settings.py_

```
# ...

USE_ZENROWS_PROXY = False # to turn off premium proxy (True by default)
```

### Autoparse

`AUTOPARSE` is `False` by default. Setting `AUTOPARSE = True` uses our extraction algorithms to parse data in JSON format automatically:

_settings.py_

```
# ...

AUTOPARSE = True # False by default
```

**Note**: Using `AUTOPARSE = True` may throw an error `400` if used with an unsupported website.

Check out [how autoparsing works](https://docs.zenrows.com/scraper-api/features/output#auto-parsing) to learn more.

### Output Filter

You can also specify the data you want to scrape with the `OUTPUTS` settings option. Note that you don't need to include the OUTPUTS option if you don't need it.

For instance, to parse tables automatically:

_settings.py_

```
# ...

OUTPUTS = "tables"

# **Accepted options**: "tables", "emails", "phone_numbers", "headings", "images", "audios", "links, videos".
```

**Note**: Using `OUTPUTS = <option>` may throw an error `400` if used with an unsupported website.

Check the [output filters doc](https://docs.zenrows.com/scraper-api/features/output#output-filters) for more information.
