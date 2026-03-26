# creating a mini project using dictionary and conditional statements in python. this takes the order and gives the final bill
# define the menu of restauarant
menu = {
    'pizza':40,
    'pasta':50,
    'burger':50,
    'salad':60,
    'coffee':80,
}
#greet
print("welcome to our restaurant")
for key, value in menu.items():
    print(key,value)

order_total = 0

item_1 = input("enter the order you want = ");
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your {item_1} has been added to cart")
else:
     print(f"sorry your ordered {item_1} is not available rn")
another_item = input("do uh want to add another item? yes/no ")
if another_item == "yes":
    item_2 = input("enter ur second order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your {item_2} has been added to cart")
    else:
         print(f"sry {item_2} is not available rn")

print(f"ypur total bill is {order_total}")        


