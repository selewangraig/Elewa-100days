# Imagine you are about to create a budget on what you will be spending for the month of September.

income = int(input("What is your monthly net income? "))

#calculate budget using 50/30/20 rule
needs = int(0.5 * income) #necessities
wants = int(0.3 * income) #enjoyment
savings = int(0.2 * income)

print(f"Your monthly budget for your needs is, {needs}")
print(f"Your monthly enjoyment budget is, {wants} ")
print(f"Your monthly savings budget is, {savings}")