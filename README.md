# kenallclient

## USAGE

### in your python programs

To use kenallclient in your program, create KenAllClient with api key and call get method.

#### initialize

`kenallclient` provides `KenAllClient` class.

```
>>> from kenallclient.client import KenAllClient
>>> API_KEY = "YOUR_API_KEY"
>>> zipcode = "1008105"
>>> client = KenAllClient(API_KEY)
```

`get` method gets an address by postalcode.

```
>>> client.get(zipcode)
KenAllResult(version='2021-01-29', data=[KenAllResultItem(jisx0402='13101', old_code='100', postal_code='1008105', prefecture_kana='', city_kana='', town_kana='', town_kana_raw='', prefecture='東京都', city='千代田区', town='大手町', koaza='', kyoto_street='', building='', floor='', town_partial=False, town_addressed_koaza=False, town_chome=False, town_multi=False, town_raw='大手町', corporation=KenAllCorporation(name='チッソ\u3000株式会社', name_kana='チツソ\u3000カブシキガイシヤ', block_lot='２丁目２－１（新大手町ビル）', post_office='銀座', code_type=0))])
```

`search` method queries by freetext and facets.

```
>>> client.search(q="神奈川県 AND 日本郵便")
[('q', '神奈川県 AND 日本郵便'), ('offset', None), ('limit', None), ('facet', None)]
KenAllSearchResult(version='2022-01-31', data=[KenAllResultItem(jisx0402='14131', old_code='210', postal_code='2108797', prefecture_kana='', city_kana='', town_kana='', town_kana_raw='', prefecture='神奈川県', city='川崎市川崎区', town='榎町', koaza='', kyoto_street='', building='', floor='', town_partial=False, town_addressed_koaza=False, town_chome=False, town_multi=False, town_raw='榎町', corporation=KenAllCorporation(name='日本郵便\u3000株式会社\u3000南関東支社', name_kana='ニツポンユウビン\u3000カブシキガイシヤ\u3000ミナミカントウシシヤ', block_lot='１－２', block_lot_num='1-2', post_office='川崎港', code_type=0)), KenAllResultItem(jisx0402='14131', old_code='210', postal_code='2108796', prefecture_kana='', city_kana='', town_kana='', town_kana_raw='', prefecture='神奈川県', city='川崎市川崎区', town='榎町', koaza='', kyoto_street='', building='', floor='', town_partial=False, town_addressed_koaza=False, town_chome=False, town_multi=False, town_raw='榎町', corporation=KenAllCorporation(name='日本郵便\u3000株式会社\u3000神奈川監査室', name_kana='ニツポンユウビン\u3000カブシキガイシヤ\u3000カナガワカンサシツ', block_lot='１－２', block_lot_num='1-2', post_office='川崎港', code_type=0)), KenAllResultItem(jisx0402='14131', old_code='210', postal_code='2108793', prefecture_kana='', city_kana='', town_kana='', town_kana_raw='', prefecture='神奈川県', city='川崎市川崎区', town='榎町', koaza='', kyoto_street='', building='', floor='', town_partial=False, town_addressed_koaza=False, town_chome=False, town_multi=False, town_raw='榎町', corporation=KenAllCorporation(name='日本郵便\u3000株式会社\u3000南関東支社\u3000郵便事業本部\u3000（三種）', name_kana='ニホンユウビン\u3000カブシキガイシヤ\u3000ミナミカントウシシヤ\u3000ユウビンジギヨウホンブ\u3000（サンシユ）', block_lot='１－２', block_lot_num='1-2', post_office='川崎港', code_type=0))], query={'q': '神奈川県 AND 日本郵便', 't': None, 'prefecture': None, 'county': None, 'city': None, 'city_ward': None, 'town': None, 'kyoto_street': None, 'block_lot_num': None, 'building': None, 'floor_room': None}, count=3, offset=0, limit=100, facets=None)

```

### module command

To use kenallclient in command line, call kenallclient module.

#### get by postal code

`get` subcommand calls [郵便番号API](`search` subcommand calls [郵便番号逆引き検索API](https://kenall.jp/docs/API/postalcode/#get-postalcodeqoffsetlimitfacet).

```
python -m kenallclient --apikey="YOUR_API_KEY" get 1008105
{'data': [{'building': '',
           'city': '千代田区',
           'city_kana': '',
           'corporation': {'block_lot': '２丁目２－１（新大手町ビル）',
                           'code_type': 0,
                           'name': 'チッソ\u3000株式会社',
                           'name_kana': 'チツソ\u3000カブシキガイシヤ',
                           'post_office': '銀座'},
           'floor': '',
           'jisx0402': '13101',
           'koaza': '',
           'kyoto_street': '',
           'old_code': '100',
           'postal_code': '1008105',
           'prefecture': '東京都',
           'prefecture_kana': '',
           'town': '大手町',
           'town_addressed_koaza': False,
           'town_chome': False,
           'town_kana': '',
           'town_kana_raw': '',
           'town_multi': False,
           'town_partial': False,
           'town_raw': '大手町'}],
 'version': '2021-01-29'}
 ```

#### search by query

`search` subcommand calls [郵便番号逆引き検索API](https://kenall.jp/docs/API/postalcode/#get-postalcodeqoffsetlimitfacet).

```
$ python -m kenallclient search --help
usage: __main__.py search [-h] [--offset OFFSET] [--limit LIMIT] [--facet FACET] q

positional arguments:
  q

optional arguments:
  -h, --help       show this help message and exit
  --offset OFFSET
  --limit LIMIT
  --facet FACET
```

```
python -m kenallclient --apikey="YOUR_API_KEY" search "神奈川県 AND 日本郵便"
[('q', '神奈川県 AND 日本郵便'), ('offset', None), ('limit', None), ('facet', None)]
{'count': 3,
 'data': [{'building': '',
           'city': '川崎市川崎区',
           'city_kana': '',
           'corporation': {'block_lot': '１－２',
                           'block_lot_num': '1-2',
                           'code_type': 0,
                           'name': '日本郵便\u3000株式会社\u3000南関東支社',
                           'name_kana': 'ニツポンユウビン\u3000カブシキガイシヤ\u3000'
                                        'ミナミカントウシシヤ',
                           'post_office': '川崎港'},
           'floor': '',
           'jisx0402': '14131',

...

           'town': '榎町',
           'town_addressed_koaza': False,
           'town_chome': False,
           'town_kana': '',
           'town_kana_raw': '',
           'town_multi': False,
           'town_partial': False,
           'town_raw': '榎町'}],
 'facets': None,
 'limit': 100,
 'offset': 0,
 'query': {'block_lot_num': None,
           'building': None,
           'city': None,
           'city_ward': None,
           'county': None,
           'floor_room': None,
           'kyoto_street': None,
           'prefecture': None,
           'q': '神奈川県 AND 日本郵便',
           't': None,
           'town': None},
 'version': '2022-01-31'}
```
