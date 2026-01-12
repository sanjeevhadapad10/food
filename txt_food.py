from food import FoodOrder
def test_total_price():
    order = FoodOrder(1, "Sanjeev", ["Burger", "Pizza"], [100, 200])
    assert order.total_price() == 300
