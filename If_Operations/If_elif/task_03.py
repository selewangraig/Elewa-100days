# Assignment 1 - Scenario 3: Cleaning Your House
chores_list = ["Sweep the floor", "Wash dishes", "Dust furniture", "Clean the bathroom"]
index = 0

while index < len(chores_list):
    current_chore = chores_list[index]
    print("Perform", current_chore)
    done = input(f"Is {current_chore} done? (yes/no): ")
    
    if done.lower() == "yes":
        print("Great! Move on to the next chore.")
    else:
        print(f"Finish {current_chore} before moving on to the next chore.")
    
    index += 1

print("All chores are done. Your house is clean!")