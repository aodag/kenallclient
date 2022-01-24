import json
import urllib.parse
import urllib.request
from typing import Dict

from kenallclient.model import KenAllResult


class KenAllClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    @property
    def authorization(self) -> Dict[str, str]:
        auth = {"Authorization": f"Token {self.api_key}"}
        return auth

    def create_request(self, postal_code: str) -> urllib.request.Request:
        url = urllib.parse.urljoin("https://api.kenall.jp/v1/postalcode/", postal_code)
        req = urllib.request.Request(url, headers=self.authorization)
        return req

    def fetch(self, req: urllib.request.Request) -> KenAllResult:
        with urllib.request.urlopen(req) as res:
            if not res.headers["Content-Type"].startswith("application/json"):
                raise ValueError("not json response", res.read())
            d = json.load(res)
            return KenAllResult.fromdict(d)

    def get(self, postal_code: str) -> KenAllResult:
        req = self.create_request(postal_code)
        return self.fetch(req)
