from datetime import datetime

import pytest
import responses

from luchanos.BasicPart3.my_functions.web_client import AvitoClient


@responses.activate
def test_web_client():
    valid_json_response = {
        'lastActionTime': 16810611581,
        'timeDiff': 79917
    }
    responses.add(method=responses.GET, url='http://www.avito.ru/web/user/get-status/177068588',
                  json=valid_json_response, status=200)
    client = AvitoClient(url='http://www.avito.ru')
    res = client.get_user_last_action_time("177068588")

    assert res == datetime.fromtimestamp(valid_json_response['lastActionTime'] - valid_json_response['timeDiff'])


@responses.activate
def test_web_client_for_error():
    valid_json_response = {
        "errors": [
            "Not found"
        ]
    }

    responses.add(method=responses.GET, url='http://www.avito.ru/web/user/get-status/177068588-',
                   json=valid_json_response,status=404)

    with pytest.raises(NameError):
        client = AvitoClient(url='http://www.avito.ru')
        res = client.get_user_last_action_time("177068588-")
