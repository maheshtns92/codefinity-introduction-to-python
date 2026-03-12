# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]
def calculate_revenue(prices,quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue
product_revenue_list = calculate_revenue(prices,quantities_sold)
revenue_per_product = list(zip(products,product_revenue_list))
formatted_output = sorted(revenue_per_product)
for name,rev in formatted_output:
    print(f"{name} has total revenue of ${rev}")