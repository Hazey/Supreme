# -*- coding: utf-8 -*-

import asyncio
import operator

from supreme import Supreme

async def main():
    async with Supreme() as supreme:
        while True:
            items = await supreme.items()

            if any(map(operator.attrgetter("sale_price"), items)):
                print(items)

if __name__ == "__main__":
    asyncio.run(main())