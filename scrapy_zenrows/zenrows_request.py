from scrapy import Request
import copy


class ZenRowsRequest(Request):
    def __init__(
        self,
        url,
        params=None,
        headers=None,
        cookies=None,
        meta=None,
        *args,
        **kwargs,
    ):
        meta = copy.deepcopy(meta) or {}
        self.params = params or {}

        super(ZenRowsRequest, self).__init__(
            url,
            headers=headers,
            cookies=cookies,
            meta=meta,
            *args,
            **kwargs,
        )
