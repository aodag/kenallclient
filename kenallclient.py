import dataclasses
from typing import List, Optional
import urllib.request
import urllib.parse
import json

@dataclasses.dataclass()
class KenAllCorporation:
    name: str
    name_kana: str
    block_lot: str
    post_office: str
    code_type: int


@dataclasses.dataclass()
class KenAllResultItem:
    jisx0402: str
    old_code: str
    postal_code: str
    prefecture_kana: str
    city_kana: str
    town_kana: str
    town_kana_raw: str
    prefecture: str
    city: str
    town: str
    koaza: str
    kyoto_street: str
    building: str
    floor: str
    town_partial: bool
    town_addressed_koaza: bool
    town_chome: bool
    town_multi: bool
    town_raw: str
    corporation: Optional[KenAllCorporation]

    @classmethod
    def fromdict(self, i):
        if i["corporation"]:
            c = i["corporation"]
            corp = KenAllCorporation(**c)
            i["corporation"] = corp
        return KenAllResultItem(**i)


@dataclasses.dataclass()
class KenAllResult:
    version: str
    data: List[KenAllResultItem]

    @classmethod
    def fromdict(self, d):
        data = [KenAllResultItem.fromdict(i) for i in d["data"]]
        dd = dict(**d)
        dd["data"] = data
        return KenAllResult(**dd)


class KenAllClient:
    def __init__(self, api_key):
        self.api_key = api_key

    @property
    def authorization(self):
        auth = {"Authorization": f"Token {self.api_key}"}
        return auth

    def build_url(self, postal_code):
        url = urllib.parse.urljoin("https://api.kenall.jp/v1/postalcode/", postal_code)
        return url
    
    def create_request(self, postal_code):
        url = self.build_url(postal_code)
        req = urllib.request.Request(url, headers=self.authorization)
        return req

    def get(self, postal_code):
        req = self.create_request(postal_code)
        with urllib.request.urlopen(req) as res:
            if res.headers["Content-Type"].startswith("application/json"):
                d = json.load(res)
                print(KenAllResult.fromdict(d))
            else:
                print(res.read())