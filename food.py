def get_order_category(avg_price):
    if avg_price >= 500:
        return "Premium Order"
    elif 350 <= avg_price <= 499:
        return "Gold Order"
    elif 200 <= avg_price <= 349:
        return "Silver Order"
    elif 100 <= avg_price <= 199:
        return "Regular Order"
    else:
        return "Basic Order"


def process_order(customer_name, restaurant_name, food_category, prices):
    avg_price = sum(prices) / len(prices)
    order_category = get_order_category(avg_price)

    order_details = {
        "Customer Name": customer_name,
        "Restaurant Name": restaurant_name,
        "Food Category": food_category,
        "Item Prices": prices,
        "Average Price": avg_price,
        "Order Category": order_category
    }
    return order_details


if __name__ == "__main__":
    customer_name = input("Enter customer name: ")
    restaurant_name = input("Enter restaurant name: ")
    food_category = input("Enter food category: ")

    prices = []
    for i in range(1, 4):
        price = float(input(f"Enter price of item {i}: "))
        prices.append(price)

    order = process_order(customer_name, restaurant_name, food_category, prices)

    print("\n--- Order Details ---")
    for key, value in order.items():
        print(f"{key}: {value}")
