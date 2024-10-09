from scrapy import Request
from urllib.parse import urlencode


class ZenRowsRequest(Request):
    def __init__(
        self,
        url,
        params=None,
        headers=None,
        cookies=None,
        *args,
        **kwargs,
    ):
        self.params = params or {}
        self.cookies = cookies or {}

        # Set the cookies in the headers
        if headers is None:
            headers = {}

        cookie_string = self.process_cookies(self.cookies)
        if cookie_string:
            headers["Cookie"] = cookie_string

        super(ZenRowsRequest, self).__init__(
            url,
            headers=headers,
            *args,
            **kwargs,
        )

    @staticmethod
    def process_cookies(cookies):
        if isinstance(cookies, dict):
            return "; ".join(f"{k}={v}" for k, v in cookies.items())
        elif isinstance(cookies, str):
            return cookies
        return ""

    def build_zenrows_url(self, url, params):
        # Build the URL for ZenRows API
        payload = {"url": url}
        if params:
            payload.update(params)

        return f"https://api.zenrows.com/v1/?{urlencode(payload)}"
