from urllib.parse import urlencode
from scrapy.exceptions import NotConfigured
from .zenrows_request import ZenRowsRequest


class ZenRowsMiddleware:
    def __init__(
        self,
        api_key,
        use_proxy=False,
        js_render=False,
    ):
        self.api_key = api_key
        self.zenrows_url = "https://api.zenrows.com/v1"
        self.use_proxy = use_proxy
        self.js_render = js_render

    @classmethod
    def from_crawler(cls, crawler):
        api_key = crawler.settings.get("ZENROWS_API_KEY")
        if not api_key:
            raise NotConfigured("ZenRows API Key is not configured")

        use_proxy = crawler.settings.getbool("USE_ZENROWS_PROXY", False)

        js_render = crawler.settings.getbool("JS_RENDER", False)

        return cls(
            api_key=api_key,
            use_proxy=use_proxy,
            js_render=js_render,
        )

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
            request._set_url(api_url)

    def get_zenrows_api_url(self, url, params, use_proxy, js_render):
        payload = {"url": url}

        if self.use_proxy:
            payload["premium_proxy"] = "true"

        if self.js_render:
            payload["js_render"] = "true"

        payload.update(params)

        api_url = f"{self.zenrows_url}/?apikey={self.api_key}&{urlencode(payload)}"
        return api_url
