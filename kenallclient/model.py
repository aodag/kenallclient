import dataclasses
from typing import List, Optional, Any, Dict, Tuple


HOUJIN_KIND = {
    101: "国の機関",
    201: "地方公共団体",
    301: "株式会社",
    302: "有限会社",
    303: "合名会社",
    304: "合資会社",
    305: "合同会社",
    399: "その他の設立登記法人",
    401: "外国会社等",
    499: "その他",
}

HOUJIN_HIHYOJI = {
    0: "検索対象",
    1: "検索対象から除外",
}

HOUJIN_CLOSE_CAUSE = {
    "01": "精算の結了等",
    "11": "合併による解散等",
    "21": "登記官による閉鎖",
    "31": "その他の精算の結了等",
}

CORPORATION_CODE_TYPE = {
    0: "大口事業所",
    1: "私書箱",
}

@dataclasses.dataclass()
class HoujinResultItem:
    sequence_number: int
    corporate_number: str
    process: int
    correct: int
    update_date: str
    change_date: str
    name: str
    name_image_id: Optional[str]
    kind: int
    prefecture_name: str
    city_name: str
    published_date: str
    hihyoji: int
    furigana: str
    en_address_outside: Optional[str]
    en_address_line: Optional[str]
    en_prefecture_name: str
    en_name: str
    assignment_date: str
    change_cause: str
    successor_corporate_number: Optional[str]
    close_cause: Optional[str]
    close_date: Optional[str]
    address_outside_image_id: Optional[str]
    address_outside: str
    post_code: str
    jisx0402: str
    address_image_id: Optional[str]
    street_number: str

@dataclasses.dataclass()
class HoujinResult:
    version: str
    data: List[HoujinResultItem]

    @classmethod
    def fromdict(cls, i: Dict[str, Any]) -> "HoujinResult":
        return HoujinResult(**i)


@dataclasses.dataclass()
class HoujinSearchResult:
    version: str
    data: List[str]
    query: str
    count: int
    offset: int
    limit: int
    facets: List[Tuple[str, int]]

    @classmethod
    def fromdict(cls, i: Dict[str, Any]) -> "HoujinSearchResult":
        return HoujinSearchResult(**i)


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
