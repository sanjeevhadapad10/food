import pytest
from food import get_order_category, process_order


pytest.mark.parametrize("avg_price,expected", [
    (550, "Premium Order"),
    (400, "Gold Order"),
    (250, "Silver Order"),
    (150, "Regular Order"),
    (50, "Basic Order"),
])
def txt_get_order_category(avg_price, expected):
    assert get_order_category(avg_price) == expected


def txt_process_order():
    order = process_order(
        "Alice",
        "Food Hub",
        "Italian",
        [300, 400, 500]
    )
    assert order["Order Category"] == "Gold Order"
    assert order["Average Price"] == 400
