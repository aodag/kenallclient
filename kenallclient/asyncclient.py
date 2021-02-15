import asyncio
import urllib.parse
import json
from typing import Dict

import aiohttp

from .model import KenAllResult


class AsyncKenAllClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()
        self.session = None

    @property
    def authorization(self) -> Dict[str, str]:
        auth = {"Authorization": f"Token {self.api_key}"}
        return auth

    async def get(self, postal_code) -> KenAllResult:
        url = urllib.parse.urljoin("https://api.kenall.jp/v1/postalcode/", postal_code)
        async with self.session.get(url, headers=self.authorization) as res:
            if res.status != 200:
                raise ValueError(await res.text())
            d = await res.json()
            return KenAllResult.fromdict(d)


async def main() -> None:
    import argparse
    import dataclasses
    import os
    from pprint import pprint

    parser = argparse.ArgumentParser()
    parser.add_argument("--apikey", default=os.environ.get("KENALL_APIKEY"))
    parser.add_argument("postalcode")
    args = parser.parse_args()
    async with AsyncKenAllClient(args.apikey) as client:
        pprint(dataclasses.asdict(await client.get(args.postalcode)))


if __name__ == '__main__':
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())