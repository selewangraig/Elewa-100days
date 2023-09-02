# Variables
current_weight = float(input("Enter your current weight (kg): "))
goal_weight = float(input("Enter your goal weight (kg): "))

eating_routine = [
    {'food': 'vegetables', 'portion': 200},  # Example: 200 grams of vegetables
    {'food': 'lean protein', 'portion': 150},  # Example: 150 grams of lean protein
    {'food': 'fruit', 'portion': 100},  # Example: 100 grams of fruit
]

# Iterative Process
while current_weight > goal_weight:
    print("\nCurrent Weight:", current_weight, "kg")

    for item in eating_routine:
        food = item['food']
        portion = item['portion']
        print(f"Eat {portion} grams of {food}")

        # Adjust weight based on the routine
        current_weight -= 0.1  # Example: Gradually losing weight

    print("Weight after the routine:", current_weight, "kg")

# Goal reached
print("\nCongratulations! You have reached your goal weight:", goal_weight, "kg")