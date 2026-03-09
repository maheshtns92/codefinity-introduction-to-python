grocery_inventory = {"Milk": ("Diary", 3.50, 8), "Eggs" : ("Diary", 5.50, 8), "Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.50, 50)}
category,price_eggs,stock = grocery_inventory["Eggs"]
price_eggs = grocery_inventory["Eggs"][1]
if price_eggs > 5:
    print("Eggs are too Expensive, reducing the price by $1.")
    new_price_eggs = price_eggs - 1
    grocery_inventory["Eggs"] = (category,new_price_eggs,stock)
else:
    print("The price of Eggs is reasonable")
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
stock_milk = grocery_inventory["Milk"][2]
if stock_milk < 10:
    print("milk needs to be restocked. increasing stock by 20 units.")
    stock_milk_new = stock_milk + 20
    category,price_milk,stock_milk = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (category,price_milk,stock_milk_new)
else:
    print("Milk has sufficient stock.")
apple_price = grocery_inventory["Apples"][1]
if apple_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from the inventory due to high price.")
print("Updated inventory:", grocery_inventory)
    