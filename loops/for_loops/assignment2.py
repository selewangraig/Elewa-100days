# Variables
num_guests = int(input("Enter the number of guests: "))
utensils_needed = {
    'plates': num_guests,
    'forks': 2 * num_guests,  # Assuming 2 forks per guest
    'knives': 2 * num_guests,  # Assuming 2 knives per guest
    'spoons': 2 * num_guests,  # Assuming 2 spoons per guest
    'cups': num_guests,
    'napkins': 2 * num_guests,  # Assuming 2 napkins per guest
}

shopping_list = []

# Iterative Process
for utensil, quantity in utensils_needed.items():
    current_quantity = int(input(f"Enter the current quantity of {utensil}: "))
    if current_quantity < quantity:
        shortage = quantity - current_quantity
        shopping_list.append(f"{shortage} {utensil}")

# Check if everything is available or if you need to shop
if not shopping_list:
    print("You have enough utensils for the event!")
else:
    print("You need to buy the following items:")
    for item in shopping_list:
        print(item)