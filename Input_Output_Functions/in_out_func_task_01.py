#Write a python program to prompt the user to create a shopping list and calculate the total cost.
#function to prompt user to create shopping list.


def shopping_list():
    cost_item = float
    global shop_list
    shop_list = {}

    print("\n*****")
    print("This is your personal shopping list!")
    print("*****")
    print("When done, input 'done'")
    print("*****\n")

    while True:
        item = input("Enter Item to add to shopping list: ")
        cost_item = input("Enter the Cost of the item: ")
        if item == "done":
            break
        else:
            shop_list[item] = cost_item
    return shop_list

#function to calculate total cost of the items
def total_cost():
    global shop_list
    total = 0
    for value in shop_list:
        total += float(shop_list[value])
    
    shop_list.update({"total_cost" : total})
    print(f"\nThe total cost of the items in your shopping list is: $ {total}")

#function call
shopping_list()
total_cost()