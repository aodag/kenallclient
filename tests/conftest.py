import os
import pytest

here = os.path.dirname(__file__)

@pytest.fixture
def dummy_json():
    import json

    with open(os.path.join(here, "postalcode_get.json")) as f:
        return json.load(f)


@pytest.fixture
def dummy_search_json():
    import json

    with open(os.path.join(here, "postalcode_search.json")) as f:
        return json.load(f)


@pytest.fixture
def dummy_houjinbangou_json():
    import json

    with open(os.path.join(here, "houjinbangou.json")) as f:
        return json.load(f)


@pytest.fixture
def dummy_houjinbangou_search_json():
    import json

    with open(os.path.join(here, "houjinbangou_search.json")) as f:
        return json.load(f)
    
