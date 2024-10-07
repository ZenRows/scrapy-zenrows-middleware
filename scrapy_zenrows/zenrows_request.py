from scrapy import Request
from urllib.parse import urlencode


class ZenRowsRequest(Request):
    def __init__(
        self,
        url,
        params=None,
        headers=None,
        *args,
        **kwargs,
    ):
        # store params as a request attribute
        self.params = params or {}
        # initialize the request with the original Request class
        super(ZenRowsRequest, self).__init__(
            url,
            headers=headers,
            *args,
            **kwargs,
        )

    def build_zenrows_url(self, url, params):
        # Build the URL for ZenRows API
        payload = {"url": url}
        if params:
            payload.update(params)

        return f"https://api.zenrows.com/v1/?{urlencode(payload)}"
