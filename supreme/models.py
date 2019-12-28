# -*- coding: utf-8 -*-

from typing import NamedTuple

class ItemInfo(NamedTuple):
    name: str
    id: int
    image_url: str 
    image_url_hi: str
    price: int
    sale_price: int
    new_item: bool
    position: int 
    category_name: str 
    price_euro: int
    sale_price_euro: int