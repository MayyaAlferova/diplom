from datetime import datetime, timedelta

HEADER_DATA: dict = {"Content-Type": "application/json"}

ORDER_DATA: dict = {
    "firstName": "User",
    "lastName": "Test",
    "address": "г. Москва, ул. Шарикоподшипниковская, 7/2, 37",
    "metroStation": "Дубровка",
    "phone": "+79101234567",
    "rentTime": 3,
    "deliveryDate": (datetime.now() + timedelta(days=1)).date().isoformat(),
    "comment": "Test comment",
    "color": ["BLUE"]
}
