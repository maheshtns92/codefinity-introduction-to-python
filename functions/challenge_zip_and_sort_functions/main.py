products = ["Banana", "Apple", "Mango", "Cherry"]
prices = [1.20, 0.50, 2.50, 1.75]
quantities_sold = [50, 100, 25, 40]
combined_list = []
combined_list = list(zip(products,prices,quantities_sold))
sorted_products = sorted(combined_list)
for i, j, k in sorted_products:
    print(f"Product: {i}, Price:{j} , Quantity Sold: {k}")