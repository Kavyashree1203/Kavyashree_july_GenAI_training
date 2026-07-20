def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


# Part C
def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"Error: {e}")
        # tuple immutable, athanala item assign panna mudiyadhu


def calculate_total(cart):
    subtotal = sum(item["price"] * item["qty"] for item in cart["items"])
    discount_amount = subtotal * (cart["discount"] / 100)
    return subtotal - discount_amount


def main():
    cart1 = create_cart("Ravi", discount=10)
    cart2 = create_cart("Meena")

    add_to_cart(cart1, "Rice", 60, qty=5)
    add_to_cart(cart1, "Milk", 25, qty=2)

    add_to_cart(cart2, "Bread", 40, qty=1)

    print("Ravi's cart:", cart1)
    print("Meena's cart:", cart2)
    print("Ravi's total:", calculate_total(cart1))
    print("Meena's total:", calculate_total(cart2))

    price_info = ("Rice", 60)
    update_price(price_info, 65)


if __name__ == "__main__":
    main()