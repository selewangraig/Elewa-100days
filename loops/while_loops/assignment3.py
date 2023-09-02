# a) Saving Money
saving_target = 2000  # Example saving target in your currency
current_savings = 0

while current_savings < saving_target:
    savings_increment = float(input("Enter your savings increment: "))  # You can manually enter how much you save each time
    current_savings += savings_increment

else:
    print("Congratulations! You have reached your saving target.")
    print(f"Your total savings: {current_savings}.")

# b) Electronics Selection
if current_savings >= 2000:
    print("You can now choose the electronics you want to buy.")
    electronics_choice = input("Enter '2' for 2 electronics or '3' for 3 electronics: ")

    if electronics_choice == '2':
        print("You have chosen to buy 2 electronics.")
        # Add code to select and purchase 2 electronics.
    elif electronics_choice == '3':
        print("You have chosen to buy 3 electronics.")
        # Add code to select and purchase 3 electronics.
    else:
        print("Invalid choice. Please enter '2' or '3' to select the number of electronics.")

else:
    print("You do not have sufficient savings to purchase electronics at this time.")