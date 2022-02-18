import json
import urllib.parse
import urllib.request
from typing import Dict, List, Optional, Tuple

from kenallclient.model import KenAllResult, KenAllSearchResult


class KenAllClient:
    api_url = "https://api.kenall.jp/v1/postalcode/"

    def __init__(self, api_key: str, api_url: Optional[str] = None) -> None:
        self.api_key = api_key
        if api_url is not None:
            self.api_url = api_url

    @property
    def authorization(self) -> Dict[str, str]:
        auth = {"Authorization": f"Token {self.api_key}"}
        return auth

    def create_request(self, postal_code: str) -> urllib.request.Request:
        url = urllib.parse.urljoin(self.api_url, postal_code)
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

    def create_search_request(self, q: Optional[str] = None, t: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, facet: Optional[str] = None) -> urllib.request.Request:
        query_mapping: List[Tuple[str, Optional[str]]] = [
            ("q", q),
            ("t", t),
            ("offset", str(offset) if offset is not None else None),
            ("limit", str(limit) if limit is not None else None),
            ("facet", facet),
        ]
        print(query_mapping)
        query = urllib.parse.urlencode([(k, v) for k, v in query_mapping if v is not None])
        url = f"{self.api_url}?{query}"
        req = urllib.request.Request(url, headers=self.authorization)
        return req

    def fetch_search_result(self, req: urllib.request.Request) -> KenAllSearchResult:
        with urllib.request.urlopen(req) as res:
            if not res.headers["Content-Type"].startswith("application/json"):
                raise ValueError("not json response", res.read())
            d = json.load(res)
            return KenAllSearchResult.fromdict(d)

    def search(self, *, q: Optional[str], t: Optional[str], offset: Optional[int] = None, limit: Optional[int] = None, facet: Optional[str] = None) -> KenAllSearchResult:
        req = self.create_search_request(q, t, offset, limit, facet)
        return self.fetch_search_result(req)
