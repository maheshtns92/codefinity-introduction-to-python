def apply_discount(product_prices):
    prices_copy = product_prices.copy()
    for product in range(len(prices_copy)):
        if prices_copy[product] > 2.0:
            prices_copy[product] -= prices_copy[product] * 0.10
    return prices_copy       
product_prices_list = [1.50, 2.50, 3.00, 0.99, 2.30]
updated_prices = apply_discount(product_prices_list)
print(f"Updated product prices: {updated_prices}")