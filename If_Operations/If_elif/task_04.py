# Assignment 2 - Scenario 1: Running an Errand in the Bank
print("I need to run an errand in the bank.")
print("Choose your errand: (deposit/withdrawal/inquiry)")
errand_choice = input()

if errand_choice == "deposit":
    print("Go to the bank, fill out a deposit slip, and wait in line.")
elif errand_choice == "withdrawal":
    print("Go to the bank, fill out a withdrawal slip, and wait in line.")
elif errand_choice == "inquiry":
    print("Go to the bank, approach a bank teller, and inquire about your account.")
else:
    print("Invalid choice. Please select deposit, withdrawal, or inquiry.")
    exit()

print("Perform any mini-activities while at the bank.")