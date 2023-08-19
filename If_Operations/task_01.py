#Program that will help you decide the budget of the things you want to shop for
#and determine how many items you get to buy with that budget.

#first thing is to ask what he wants to buy
#then ask how much he has to spend
#then tell him how many things, out of that budget, he can buy.

#this function will ask the user what he wants to buy
def what_buy():
    global shop_list
    shop_list = {}

    while True:
        item = input("What do you want to buy?: ")
        price = input("What is the price of the item?: ")
        if item == "done":
            break
        else:
            shop_list[item] = price
    return shop_list

def budget():
    global total, shop_list
    total = float(0)
    for value in shop_list:
        total += float(shop_list[value])

    shop_list.update({"total_cost": total})    
    print(f"The total cost of the items is {total}")

def ask_budget():
    global total, shop_list
    spend = float(input("How much are you willing to spend?: "))

    if spend <= total:
        print("The items in your list are over your budget.")
    else:
        print("You can afford the items in your list, Happy Shopping!")

what_buy()
budget()
ask_budget()