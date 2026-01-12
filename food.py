class FoodOrder:
    def __init__(self, order_id, customer_name, items, prices):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.prices = prices
    def total_price(self):
        return sum(self.prices)
if __name__ == "__main__":
    items = []
    prices = []
    n = int(input("Enter number of items: "))
    for i in range(1, n + 1):
        item = input(f"Enter item {i} name: ")
        price = float(input(f"Enter price of item {i}: "))
        items.append(item)
        prices.append(price)
    order = FoodOrder(1, "User", items, prices)
    print("Total bill:", order.total_price())

