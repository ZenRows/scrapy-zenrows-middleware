from urllib.parse import urlencode
from scrapy.exceptions import NotConfigured
from .zenrows_request import ZenRowsRequest
from .api_key_handler import HideApiKeyHandler
import logging
from scrapy import Request


class ZenRowsMiddleware:
    def __init__(self, api_key, use_proxy=False, js_render=False):
        self.api_key = api_key
        self.zenrows_url = "https://api.zenrows.com/v1"
        self.use_proxy = use_proxy
        self.js_render = js_render
        self.logger = logging.getLogger(__name__)

    @classmethod
    def from_crawler(cls, crawler):
        api_key = crawler.settings.get("ZENROWS_API_KEY")
        if not api_key:
            raise NotConfigured("ZenRows API Key is not configured")

        use_proxy = crawler.settings.getbool(
            "USE_ZENROWS_PREMIUM_PROXY",
            False,
        )
        js_render = crawler.settings.getbool(
            "USE_ZENROWS_JS_RENDER",
            False,
        )

        # add ZenRows to allowed domains by default
        spider = crawler.spider
        try:
            if spider.allowed_domains:
                if "api.zenrows.com" not in spider.allowed_domains:
                    spider.allowed_domains.append("api.zenrows.com")
        except Exception:
            pass

        cls.set_up_logging(crawler)

        return cls(
            api_key=api_key,
            use_proxy=use_proxy,
            js_render=js_render,
        )

    @staticmethod
    def set_up_logging(crawler):
        formatter = HideApiKeyHandler(
            "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
        )
        root = logging.getLogger()
        for handler in root.handlers:
            handler.setFormatter(formatter)

    def process_request(self, request, spider):
        if isinstance(request, ZenRowsRequest):

            use_proxy = request.params.get("premium_proxy", self.use_proxy)
            js_render = request.params.get("js_render", self.js_render)

            api_url = self.get_zenrows_api_url(
                request.url,
                request.params,
                use_proxy,
                js_render,
            )

            new_request = request.replace(
                cls=Request,
                url=api_url,
                meta=request.meta,
            )

            return new_request

    def process_response(self, request, response, spider):

        if response.status == 401:
            self.logger.error("Unauthorized: Invalid ZenRows API key provided.")
        elif response.status >= 400:
            try:
                error_response = response.json()
                error_title = error_response.get("title", "No title found")
            except Exception:
                error_title = "Unknown Error"
            self.logger.error(f"Error {response.status}: {error_title}")

        return response

    def get_zenrows_api_url(self, url, params, use_proxy, js_render):
        payload = {"url": url}

        if use_proxy:
            payload["premium_proxy"] = "true"
        if js_render:
            payload["js_render"] = "true"

        payload.update(params)

        api_url = f"{self.zenrows_url}/?apikey={self.api_key}&{urlencode(payload)}"
        return api_url
