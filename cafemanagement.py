#Define the menu of restaurant
menu = {
    'Pizza: $15',
    'Burger: $25',
    'Pop: $5',
    'Salad: $10'
    
}
#Greet
print("Welcome to Anjana's Restaurant")
print("Pizza:$15\nSalad:$10\nPop:$5\nBurger:$25\n")

order_total =0
#25+5=30

item_1 =input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0+15(for pizza)
    print(f"Your item{item_1} has been added to your order ")
else:
    print(f"Ordered item {item_1} is not available yet ")
    
    
another_order =input("Doyou want to add another item?(Yes/No) ")
if another_order =="Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to the order")
    else:
        print(f"Ordered item {item_2} is not avilable")
print(f"The total amount of items to pay is {order_total} ")    