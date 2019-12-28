# -*- coding: utf-8 -*-

from typing import List
from itertools import chain

from .client import API
from .models import ItemInfo

class Supreme(API):
    async def items(self) -> List[ItemInfo]:
        json = await self.json_request("GET", "mobile_stock.json")
        return [ItemInfo(**item) for item in chain.from_iterable(json["products_and_categories"].values())]