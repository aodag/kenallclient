from kenallclient import model


def test_fromdict(dummy_json):
    result = model.KenAllResult.fromdict(dummy_json)
    assert result == model.KenAllResult(
        version="2020-11-30",
        data=[
            model.KenAllResultItem(
                jisx0402="13101",
                old_code="100",
                postal_code="1008105",
                prefecture_kana="",
                city_kana="",
                town_kana="",
                town_kana_raw="",
                prefecture="東京都",
                city="千代田区",
                town="大手町",
                koaza="",
                kyoto_street="",
                building="",
                floor="",
                town_partial=False,
                town_addressed_koaza=False,
                town_chome=False,
                town_multi=False,
                town_raw="大手町",
                corporation=model.KenAllCorporation(
                    name="チッソ　株式会社",
                    name_kana="ﾁﾂｿ ｶﾌﾞｼｷｶﾞｲｼﾔ",
                    block_lot="２丁目２－１（新大手町ビル）",
                    post_office="銀座",
                    code_type=0,
                ),
            )
        ],
    )
