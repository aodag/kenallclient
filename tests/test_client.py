import io
import pytest

class DummyResponse(io.StringIO):
    headers: dict = {}


def test_it():
    pass


@pytest.mark.parametrize(
    "api_url,expected",
    [
        pytest.param(None, "https://api.kenall.jp"),
        pytest.param("https://kenall.example.com", "https://kenall.example.com"),
    ],
)
def test_api_url(api_url, expected):
    from kenallclient.client import KenAllClient
    target = KenAllClient("testing-api-key", api_url=api_url)
    assert target.api_url == expected


def test_create_request():
    from kenallclient.client import KenAllClient

    target = KenAllClient("testing-api-key")
    result = target.create_request("9999999")
    assert result.full_url == "https://api.kenall.jp/v1/postalcode/9999999"
    assert result.headers == {"Authorization": "Token testing-api-key"}


def test_create_houjin_request():
    from kenallclient.client import KenAllClient

    target = KenAllClient("testing-api-key")
    result = target.create_houjin_request("1234323")
    assert result.full_url == "https://api.kenall.jp/v1/houjinbangou/1234323"
    assert result.headers == {"Authorization": "Token testing-api-key"}


def test_fetch(mocker, dummy_json):
    import json
    from kenallclient.client import KenAllClient

    dummy_response = DummyResponse(json.dumps(dummy_json))
    dummy_response.headers = {"Content-Type": "application/json"}
    mock_urlopen = mocker.patch("kenallclient.client.urllib.request.urlopen")
    mock_urlopen.return_value = dummy_response

    request = mocker.Mock()
    target = KenAllClient("testing-api-key")
    result = target.fetch(request)
    mock_urlopen.assert_called_with(request)
    assert result

def test_fetch_unexpected_content_type(mocker, dummy_json):
    import json
    from kenallclient.client import KenAllClient

    dummy_response = DummyResponse(json.dumps(dummy_json))
    dummy_response.headers = {"Content-Type": "plain/text"}
    request_body = dummy_response.getvalue()
    mock_urlopen = mocker.patch("kenallclient.client.urllib.request.urlopen")
    mock_urlopen.return_value = dummy_response

    request = mocker.Mock()
    target = KenAllClient("testing-api-key")
    with pytest.raises(ValueError) as e:
        target.fetch(request)
    assert e.value.args == ("not json response", request_body)


def test_fetch_houjin(mocker, dummy_houjinbangou_json):
    import json
    from kenallclient.client import KenAllClient

    dummy_response = DummyResponse(json.dumps(dummy_houjinbangou_json))
    dummy_response.headers = {"Content-Type": "application/json"}
    mock_urlopen = mocker.patch("kenallclient.client.urllib.request.urlopen")
    mock_urlopen.return_value = dummy_response

    request = mocker.Mock()
    target = KenAllClient("testing-api-key")
    result = target.fetch_houjin_result(request)
    mock_urlopen.assert_called_with(request)
    assert result


def test_fetch_search_houjin_result(mocker, dummy_houjinbangou_search_json):
    import json
    from kenallclient.client import KenAllClient

    dummy_response = DummyResponse(json.dumps(dummy_houjinbangou_search_json))
    dummy_response.headers = {"Content-Type": "application/json"}
    mock_urlopen = mocker.patch("kenallclient.client.urllib.request.urlopen")
    mock_urlopen.return_value = dummy_response

    request = mocker.Mock()
    target = KenAllClient("testing-api-key")
    result = target.fetch_search_houjin_result(request)
    mock_urlopen.assert_called_with(request)
    assert result
