backpack = []  # Initialize an empty backpack

for _ in range(5):  # You have 5 attempts to pack items
    item = input("Enter an item to pack: ")
    backpack.append(item)

    if len(backpack) >= 3:
        print("You have packed at least 3 items. You're ready for your trip!")
        break
else:
    print("You couldn't pack at least 3 items. Please try again later.")