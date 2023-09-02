# Assignment 1 - Scenario 2: Choosing Weekend Activity
weekend_budget = float(input("Enter your weekend budget: "))  # Adjust the budget as needed
print("What would you like to do over the weekend? (movies/sport)")
weekend_activity = input()

if weekend_activity == "movies":
    movie_ticket_price = float(input("Enter the cost of a movie ticket: "))
    snacks_cost = float(input("Enter the cost of snacks at the movies: "))
    total_cost = movie_ticket_price + snacks_cost
elif weekend_activity == "sport":
    sports_event_cost = float(input("Enter the cost of attending a sports event: "))
    transportation_cost = float(input("Enter the cost of transportation to the sports event: "))
    total_cost = sports_event_cost + transportation_cost
else:
    print("Invalid choice. Please select movies or sport.")
    exit()

if total_cost <= weekend_budget:
    print("You can go to", weekend_activity, "for the weekend.")
    print("Remaining budget:", weekend_budget - total_cost)
else:
    print("Sorry, you cannot afford to go to", weekend_activity, "for the weekend.")