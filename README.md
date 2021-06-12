# kenallclient

## USAGE

To use kenallclient in your program, create KenAllClient with api key and call get method.

```
>>> from kenallclient.client import KenAllClient
>>> API_KEY = "YOUR_API_KEY"
>>> zipcode = "1008105"
>>> client = KenAllClient(API_KEY)
>>> client.get(zipcode)
KenAllResult(version='2021-01-29', data=[KenAllResultItem(jisx0402='13101', old_code='100', postal_code='1008105', prefecture_kana='', city_kana='', town_kana='', town_kana_raw='', prefecture='東京都', city='千代田区', town='大手町', koaza='', kyoto_street='', building='', floor='', town_partial=False, town_addressed_koaza=False, town_chome=False, town_multi=False, town_raw='大手町', corporation=KenAllCorporation(name='チッソ\u3000株式会社', name_kana='チツソ\u3000カブシキガイシヤ', block_lot='２丁目２－１（新大手町ビル）', post_office='銀座', code_type=0))])
```

To use kenallclient in command line, call kenallclient module.

```
python -m kenallclient --apikey="YOUR_API_KEY" 1008105
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
