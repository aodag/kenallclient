import dataclasses
from typing import List, Optional, Any, Dict, Tuple


@dataclasses.dataclass()
class KenAllCorporation:
    name: str
    name_kana: str
    block_lot: str
    block_lot_num: Optional[str]
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
    def fromdict(cls, i: Dict[str, Any]) -> "KenAllResultItem":
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
    def fromdict(cls, d: Dict[str, Any]) -> "KenAllResult":
        data = [KenAllResultItem.fromdict(i) for i in d["data"]]
        dd = dict(**d)
        dd["data"] = data
        return KenAllResult(**dd)


@dataclasses.dataclass()
class KenAllSearchResult:
    version: str
    data: List[KenAllResultItem]
    query: str
    count: int
    offset: Optional[int]
    limit: Optional[int]
    facets: Optional[List[Tuple[str, int]]]

    @classmethod
    def fromdict(cls, d: Dict[str, Any]) -> "KenAllSearchResult":
        data = [KenAllResultItem.fromdict(i) for i in d["data"]]
        dd = dict(**d)
        dd["data"] = data
        if dd["facets"] is not None:
            dd["facets"] = [tuple(f) for f in dd["facets"]]
        return KenAllSearchResult(**dd)
