# -*- coding: utf-8 -*-

from yarl import URL
from aiohttp import ClientSession

class SupremeSession(ClientSession):
    BASE_URL = URL("https://www.supremenewyork.com")

    async def _request(self, method: str, url: str, **kwargs):
        return await super()._request(method, self.BASE_URL.join(URL(url)), **kwargs)