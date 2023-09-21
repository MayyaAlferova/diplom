# Майя Алфёрова, 08-а когорта — Финальный проект. Инженер по тестированию плюс

from copy import copy
from datetime import datetime, timedelta
from random import randrange

from requests import Response

import data
from send_request import create_new_order, get_order_details


def _positive_check(response: Response) -> None:
    assert response.status_code == 200


def test_create_order() -> None:
    order_data = copy(data.ORDER_DATA)
    order_data.update({
        "firstName": f"Test {randrange(100)}",
        "deliveryDate": (datetime.now() + timedelta(days=randrange(7))).date().isoformat(),
    })
    track = create_new_order(
        data=order_data
    )

    response: Response = get_order_details(track=track)

    _positive_check(response=response)
