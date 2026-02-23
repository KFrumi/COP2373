def calculate_discount(price, discount_rate):
    """
    Calculate discount amount based on price and discount rate.
    """
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    return price * discount_rate


def apply_discount(price, discount_amount):
    """
    Apply discount to the original price.
    """
    if discount_amount > price:
        raise ValueError("Discount amount cannot exceed price.")

    return price - discount_amount


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2}, # intentionally kept for testing
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        try:
            # Convert and validate inputs
            price = float(product["price"])
            discount_rate = float(product["discount_rate"])

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {product['name']}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()

        except (ValueError, TypeError) as error:
            print(f"Error processing {product['name']}: {error}")
            print()


if __name__ == "__main__":
    main()
