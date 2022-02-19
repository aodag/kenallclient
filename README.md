# kenallclient

## USAGE

### in your python programs

To use kenallclient in your program, create KenAllClient with api key and call get method.

#### initialize

`kenallclient` provides `KenAllClient` class.

```
>>> from kenallclient.client import KenAllClient
>>> API_KEY = "YOUR_API_KEY"
>>> client = KenAllClient(API_KEY)
```

#### methods

`get` method gets an address by postalcode.

```
>>> zipcode = "1008105"
>>> client.get(zipcode)
KenAllResult(version='2021-01-29', data=[KenAllResultItem(jisx0402='13101', old_code='100', postal_code='1008105', prefecture_kana='', city_kana='', town_kana='', town_kana_raw='', prefecture='東京都', city='千代田区', town='大手町', koaza='', kyoto_street='', building='', floor='', town_partial=False, town_addressed_koaza=False, town_chome=False, town_multi=False, town_raw='大手町', corporation=KenAllCorporation(name='チッソ\u3000株式会社', name_kana='チツソ\u3000カブシキガイシヤ', block_lot='２丁目２－１（新大手町ビル）', post_office='銀座', code_type=0))])
```

`search` method queries by freetext and facets.

```
>>> client.search(q="神奈川県 AND 日本郵便")
[('q', '神奈川県 AND 日本郵便'), ('offset', None), ('limit', None), ('facet', None)]
KenAllSearchResult(version='2022-01-31', data=[KenAllResultItem(jisx0402='14131', old_code='210', postal_code='2108797', prefecture_kana='', city_kana='', town_kana='', town_kana_raw='', prefecture='神奈川県', city='川崎市川崎区', town='榎町', koaza='', kyoto_street='', building='', floor='', town_partial=False, town_addressed_koaza=False, town_chome=False, town_multi=False, town_raw='榎町', corporation=KenAllCorporation(name='日本郵便\u3000株式会社\u3000南関東支社', name_kana='ニツポンユウビン\u3000カブシキガイシヤ\u3000ミナミカントウシシヤ', block_lot='１－２', block_lot_num='1-2', post_office='川崎港', code_type=0)), KenAllResultItem(jisx0402='14131', old_code='210', postal_code='2108796', prefecture_kana='', city_kana='', town_kana='', town_kana_raw='', prefecture='神奈川県', city='川崎市川崎区', town='榎町', koaza='', kyoto_street='', building='', floor='', town_partial=False, town_addressed_koaza=False, town_chome=False, town_multi=False, town_raw='榎町', corporation=KenAllCorporation(name='日本郵便\u3000株式会社\u3000神奈川監査室', name_kana='ニツポンユウビン\u3000カブシキガイシヤ\u3000カナガワカンサシツ', block_lot='１－２', block_lot_num='1-2', post_office='川崎港', code_type=0)), KenAllResultItem(jisx0402='14131', old_code='210', postal_code='2108793', prefecture_kana='', city_kana='', town_kana='', town_kana_raw='', prefecture='神奈川県', city='川崎市川崎区', town='榎町', koaza='', kyoto_street='', building='', floor='', town_partial=False, town_addressed_koaza=False, town_chome=False, town_multi=False, town_raw='榎町', corporation=KenAllCorporation(name='日本郵便\u3000株式会社\u3000南関東支社\u3000郵便事業本部\u3000（三種）', name_kana='ニホンユウビン\u3000カブシキガイシヤ\u3000ミナミカントウシシヤ\u3000ユウビンジギヨウホンブ\u3000（サンシユ）', block_lot='１－２', block_lot_num='1-2', post_office='川崎港', code_type=0))], query={'q': '神奈川県 AND 日本郵便', 't': None, 'prefecture': None, 'county': None, 'city': None, 'city_ward': None, 'town': None, 'kyoto_street': None, 'block_lot_num': None, 'building': None, 'floor_room': None}, count=3, offset=0, limit=100, facets=None)

```

`get_houjin` method gets an houjin by houjinbangou.

```
>>> client.get_houjin("2021001052596")
HoujinResult(version='2022-02-17', data={'published_date': '2022-01-31', 'sequence_number': '1409569', 'corporate_number': '2021001052596', 'process': '12', 'correct': '0', 'update_date': '2021-01-12', 'change_date': '2021-01-04', 'name': '株式会社オープンコレクター', 'name_image_id': None, 'kind': '301', 'prefecture_name': '東京都', 'city_name': '千代田区', 'street_number': '麹町３丁目１２－１４麹町駅前ヒルトップ８階', 'town': '麹町', 'kyoto_street': None, 'block_lot_num': '3-12-14', 'building': '麹町駅前ヒルトップ', 'floor_room': '8階', 'address_image_id': None, 'jisx0402': '13101', 'post_code': '1020083', 'address_outside': '', 'address_outside_image_id': None, 'close_date': None, 'close_cause': None, 'successor_corporate_number': None, 'change_cause': '', 'assignment_date': '2015-10-05', 'en_name': '', 'en_prefecture_name': 'Tokyo', 'en_address_line': '', 'en_address_outside': '', 'furigana': 'オープンコレクター', 'hihyoji': '0'})
```

`search_houjin` method queries by freetext and facets.

```
>>> client.search_houjin(q="name:オープンコレクター AND prefecture_name:東京都", limit=1)
HoujinSearchResult(version='2022-02-17', data=[{'published_date': '2022-01-31', 'sequence_number': '1409569', 'corporate_number': '2021001052596', 'process': '12', 'correct': '0', 'update_date': '2021-01-12', 'change_date': '2021-01-04', 'name': '株式会社オープンコレクター', 'name_image_id': None, 'kind': '301', 'prefecture_name': '東京都', 'city_name': '千代田区', 'street_number': '麹町３丁目１２－１４麹町駅前ヒルトップ８階', 'town': '麹町', 'kyoto_street': None, 'block_lot_num': '3-12-14', 'building': '麹町駅前ヒルトップ', 'floor_room': '8階', 'address_image_id': None, 'jisx0402': '13101', 'post_code': '1020083', 'address_outside': '', 'address_outside_image_id': None, 'close_date': None, 'close_cause': None, 'successor_corporate_number': None, 'change_cause': '', 'assignment_date': '2015-10-05', 'en_name': '', 'en_prefecture_name': 'Tokyo', 'en_address_line': '', 'en_address_outside': '', 'furigana': 'オープンコレクター', 'hihyoji': '0'}], query='name:オープンコレクター AND prefecture_name:東京都', count=1, offset=0, limit=1, facets=None)

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
usage: __main__.py search [-h] [--query QUERY] [--text TEXT] [--offset OFFSET] [--limit LIMIT] [--facet FACET]

optional arguments:
  -h, --help            show this help message and exit
  --query QUERY, -q QUERY
  --text TEXT, -t TEXT
  --offset OFFSET
  --limit LIMIT
  --facet FACET
```

```
python -m kenallclient --apikey="YOUR_API_KEY" search -q "神奈川県 AND 日本郵便"
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

### get by houjinbangou

```
$ python -m kenallclient get-houjin 2021001052596
{'data': {'address_image_id': None,
          'address_outside': '',
          'address_outside_image_id': None,
          'assignment_date': '2015-10-05',
          'block_lot_num': '3-12-14',
          'building': '麹町駅前ヒルトップ',
          'change_cause': '',
          'change_date': '2021-01-04',
          'city_name': '千代田区',
          'close_cause': None,
          'close_date': None,
          'corporate_number': '2021001052596',
          'correct': '0',
          'en_address_line': '',
          'en_address_outside': '',
          'en_name': '',
          'en_prefecture_name': 'Tokyo',
          'floor_room': '8階',
          'furigana': 'オープンコレクター',
          'hihyoji': '0',
          'jisx0402': '13101',
          'kind': '301',
          'kyoto_street': None,
          'name': '株式会社オープンコレクター',
          'name_image_id': None,
          'post_code': '1020083',
          'prefecture_name': '東京都',
          'process': '12',
          'published_date': '2022-01-31',
          'sequence_number': '1409569',
          'street_number': '麹町３丁目１２－１４麹町駅前ヒルトップ８階',
          'successor_corporate_number': None,
          'town': '麹町',
          'update_date': '2021-01-12'},
 'version': '2022-02-17'}
 ```
