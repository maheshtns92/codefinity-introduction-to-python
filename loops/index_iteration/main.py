prices = [29.99, 45.50, 12.75, 38.20]
discount_factor = [0.10, 0.20, 0.15, 0.05]
for index in range(len(prices)):
    newprices = prices[index] - prices[index] * discount_factor[index]
    prices[index] = newprices
    print(f"updated price for item {index}: ${newprices:.2f}")