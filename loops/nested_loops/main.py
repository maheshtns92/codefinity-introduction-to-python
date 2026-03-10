produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce, dairy]
for section in groceries:
    for items in section:
        print(f"Item name:{items}")