
from calculator import calculate_total


def get_order_total(price, quantity):
    return calculate_total(price, quantity)


def get_customer_total(price, quantity):
    return calculate_total(price, quantity)


def create_order(user_id, price, quantity):
    total = calculate_total(price, quantity)

    return {
        "user_id": user_id,
        "price": price,
        "quantity": quantity,
        "total": total
    }
