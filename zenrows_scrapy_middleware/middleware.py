from urllib.parse import urlencode
from scrapy.exceptions import NotConfigured


class ZenRowsMiddleware:
    def __init__(
        self,
        api_key,
        outputs,
        use_proxy=True,
        autoparse=False,
    ):
        self.api_key = api_key
        self.zenrows_url = "https://api.zenrows.com/v1"
        self.use_proxy = use_proxy
        self.autoparse = autoparse
        self.outputs = outputs

    @classmethod
    def from_crawler(cls, crawler):

        api_key = crawler.settings.get("ZENROWS_API_KEY")
        if not api_key:
            raise NotConfigured("ZenRows API Key is not configured")

        use_proxy = crawler.settings.getbool("USE_ZENROWS_PROXY", True)

        autoparse = crawler.settings.getbool("AUTOPARSE", False)

        outputs = crawler.settings.get("OUTPUTS")

        return cls(
            api_key=api_key,
            use_proxy=use_proxy,
            autoparse=autoparse,
            outputs=outputs,
        )

    def process_request(self, request, spider):
        api_url = self.get_zenrows_api_url(request.url)
        request._set_url(api_url)

    def get_zenrows_api_url(self, url):

        payload = {
            "url": url,
            "js_render": "true",
            "js_instructions": '[{"wait": 500}]',
        }

        if self.use_proxy:
            payload["premium_proxy"] = "true"

        if self.autoparse:
            payload["autoparse"] = "true"

        if self.outputs is not None:
            payload["outputs"] = self.outputs

        api_url = f"{self.zenrows_url}/?apikey={self.api_key}&{urlencode(payload)}"
        return api_url
