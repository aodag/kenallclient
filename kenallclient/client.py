import json
import urllib.parse
import urllib.request
from typing import Dict, List, Optional, Tuple

from kenallclient.model import HoujinResult, HoujinSearchResult, KenAllResult, KenAllSearchResult


class KenAllClient:
    api_url = "https://api.kenall.jp"

    def __init__(self, api_key: str, api_url: Optional[str] = None) -> None:
        self.api_key = api_key
        if api_url is not None:
            self.api_url = api_url

    @property
    def authorization(self) -> Dict[str, str]:
        auth = {"Authorization": f"Token {self.api_key}"}
        return auth

    def create_request(self, postal_code: str) -> urllib.request.Request:
        url = urllib.parse.urljoin(f"{self.api_url}/v1/postalcode/", postal_code)
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

        query = urllib.parse.urlencode([(k, v) for k, v in query_mapping if v is not None])
        url = f"{self.api_url}/v1/postalcode/?{query}"
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

    def create_houjin_request(self, houjinbangou: str) -> urllib.request.Request:
        url = f"{self.api_url}/v1/houjinbangou/{houjinbangou}"
        return urllib.request.Request(url, headers=self.authorization)

    def fetch_houjin_result(self, req: urllib.request.Request) -> HoujinResult:
        with urllib.request.urlopen(req) as res:
            if not res.headers["Content-Type"].startswith("application/json"):
                raise ValueError("not json response", res.read())
            d = json.load(res)
            return HoujinResult.fromdict(d)

    def get_houjin(self, houjinbangou: str) -> HoujinResult:
        req = self.create_houjin_request(houjinbangou)
        return self.fetch_houjin_result(req)

    def create_search_houjin_request(
            self, q: str,
            offset: Optional[int] = None,
            limit: Optional[int] = None,
            mode: Optional[str] = None,
            facet_area: Optional[str] = None,
            facet_kind: Optional[str] = None,
            facet_process: Optional[str] = None,
            facet_close_cause: Optional[str] = None,
    )-> urllib.request.Request:
        query_mapping: List[Tuple[str, Optional[str]]] = [
            ("q", q),
            ("offset", str(offset) if offset is not None else None),
            ("limit", str(limit) if limit is not None else None),
            ("mode", mode),
            ("facet_area", facet_area),
            ("facet_kind", facet_kind),
            ("facet_process", facet_process),
            ("facet_close_cause", facet_close_cause),
        ]

        query = urllib.parse.urlencode([(k, v) for k, v in query_mapping if v is not None])
        url = f"{self.api_url}/v1/houjinbangou?{query}"
        req = urllib.request.Request(url, headers=self.authorization)
        return req

    def fetch_search_houjin_result(self, req: urllib.request.Request) -> HoujinSearchResult:
        with urllib.request.urlopen(req) as res:
            if not res.headers["Content-Type"].startswith("application/json"):
                raise ValueError("not json response", res.read())
            d = json.load(res)
            return HoujinSearchResult.fromdict(d)
    
    def search_houjin(
            self, q: str,
            offset: Optional[int] = None,
            limit: Optional[int] = None,
            mode: Optional[str] = None,
            facet_area: Optional[str] = None,
            facet_kind: Optional[str] = None,
            facet_process: Optional[str] = None,
            facet_close_cause: Optional[str] = None,
    ) -> HoujinSearchResult:
        req = self.create_search_houjin_request(q, offset=offset, limit=limit, mode=mode, facet_area=facet_area, facet_kind=facet_kind, facet_process=facet_process, facet_close_cause=facet_close_cause)
        return self.fetch_search_houjin_result(req)
