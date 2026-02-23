def calculate_discount(price, discount_rate):
    """
    Calculate the discount amount based on price and discount rate.
    """
    # Convert inputs to numeric types
    price = float(price)
    discount_rate = float(discount_rate)

    # Validate inputs
    if price < 0:
        raise ValueError("Price must be a non-negative number.")

    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    return price * discount_rate


def apply_discount(price, discount_amount):
    """
    Apply the discount to the original price.
    """
    return price - discount_amount


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        try:
            price = product["price"]
            discount_rate = product["discount_rate"]

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(float(price), discount_amount)

            print(f"Product: {product['name']}")
            print(f"Original Price: ${float(price)}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()

        except (ValueError, TypeError) as error:
            print(f"Error processing {product['name']}: {error}")
            print()


if __name__ == "__main__":
    main()


