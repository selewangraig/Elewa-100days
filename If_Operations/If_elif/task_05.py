# Assignment 2 - Scenario 2: Preparing for Sibling's Back-to-School Shopping
shopping_budget = 35000  # shillings
shopping_list = []

print("What do you need to buy for your small sibling's back-to-school?")
item = input()

while item.lower() != "done":
    item_price = float(input(f"Enter the price of {item}: "))
    
    if item_price <= shopping_budget:
        shopping_list.append(item)
        shopping_budget -= item_price
        print(f"Added {item} to the shopping list.")
    else:
        print(f"Not enough budget for {item}.")
    
    item = input("What else do you need to buy? (Enter 'done' when finished): ")

print("Your shopping list for your small sibling:")
print(shopping_list)
