"""Summarize shopping cart."""

def get_cart_total(cart):  # noqa: F811
    total = 0
    for item in cart:
        if isinstance(item, dict):
            total += item['price'] * item['quantity']
    return f'Total: ${total:.2f}'

def summarize_cart():
    """Return shopping cart summary."""
    cart = [{'name': 'Apple', 'price': 1.00, 'quantity': 5}, {'name': 'Banana', 'price': 0.25, 'quantity': 2}]
    return get_cart_total(cart)

if __name__ == "__main__":
    print(summarize_cart())
