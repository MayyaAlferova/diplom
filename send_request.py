import requests
from requests import Response

import configuration
from data import HEADER_DATA


def get_url(path: str) -> str:
    return f'{configuration.URL_SERVICE}{path}'


def create_new_order(data: dict) -> int:
    response: Response = requests.post(
        url=get_url(configuration.PATH_CREATE_ORDER),
        headers=HEADER_DATA,
        json=data,
    )

    return response.json().get('track')


def get_order_details(track: int) -> Response:
    return requests.get(
        url=f'{get_url(configuration.PATH_GET_ORDER)}?t={track}'
    )
