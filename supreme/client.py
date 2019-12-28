# -*- coding: utf-8 -*-

import operator
from functools import partialmethod

from .utilities import SupremeSession

class API:
    def __init__(self):
        self._session = SupremeSession()

    async def _request(self, method: str, url: str, type: str, **kwargs):
        async with self._session.request(method, url, **kwargs) as response:
            return await operator.methodcaller(type)(response)

    json_request = partialmethod(_request, type="json")
    request = partialmethod(_request, type="text")

    async def close(self):
        await self._session.close()

    async def __aenter__(self) -> 'API':
        return self 
    
    async def __aexit__(self, *args):
        await self.close()