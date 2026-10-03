print("=====CREATING STORE ITEM AND STORE=====\n")

items = ["Pencil", "Eraser", "Notebook", "Glue"]
stock_count = [12, 0, 8, 5, 3]

print(items)
print(stock_count)

print("\n=====PAIRING ITEMS WITH STOCK COUNT INTO A DICTIONARY=====")
inventory = {item:count for item, count in zip(items, stock_count)}
print("Full Inventory:", inventory)

print("\n=====FILTER ITEMS THAT ARE STILL IN STOCK=====")
in_stock_items = [item for item in items if inventory[items] > 0]
print("Items in stock: ", in_stock_items)
print()

print("\n=====ASKING SHOPPER WHICH ITEM THEY WANT TO BUY AND STOP FUNCTION EARLY IF ITEM IS OUT OF STOCK=====")

chosen_item = input("\nWhick Item do you want to buy?")

if chosen_item not in inventory or inventory[chosen_item]== 0:
    print(chosen_item, "is out of stock!")
    exit()

    print("\n=====CREATE PRICES AND MARK UP AMOUNT=====")

    prices = [10, 5, 40, 15, 20]

markup = int(input("Enter the markup amount to add to every price: "))

marked_up_prices = list(map(lambda p: p + markup, prices))

print("Marked Up Prices:", marked_up_prices)

# PART 8: Find the marked up price of the chosen item

item_index = items.index(chosen_item)

chosen_price = marked_up_prices[item_index]

print("Price of", chosen_item, "after markup:", chosen_price)

# PART 9: Reduce the stock count after the purchase

inventory[chosen_item] = inventory[chosen_item] - 1

print(chosen_item, "purchased! Remaining stock:", inventory[chosen_item])