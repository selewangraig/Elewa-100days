# Assignment 1 - Scenario 1: Preparing Dinner with a Budget
budget = 1500  # shillings
print("What would you like to have for dinner?")
dinner_choice = input()

if dinner_choice == "pasta":
    pasta_cost = 300
elif dinner_choice == "pizza":
    pizza_cost = 600
elif dinner_choice == "salad":
    salad_cost = 200
else:
    print("Invalid choice. Please select pasta, pizza, or salad.")
    exit()

total_cost = sum([pasta_cost, pizza_cost, salad_cost])
if total_cost <= budget:
    print("You can afford to have", dinner_choice, "for dinner.")
    print("Remaining budget:", budget - total_cost)
else:
    print("Sorry, you cannot afford to have", dinner_choice, "for dinner.")