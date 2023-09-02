# Variables
chores_list = ["Wash dishes", "Sweep the floor", "Take out the trash", "Mow the lawn"]
chores_status = {chore: 'not started' for chore in chores_list}
household_members = ["John", "Mary", "David", "Sarah"]

# Initialize variables
current_member_index = 0
total_chores = len(chores_list)

# Nested while loops to assign and update chores
while any(status != 'completed' for status in chores_status.values()):
    current_chore = chores_list[current_member_index % total_chores]
    current_member = household_members[current_member_index % len(household_members)]

    # Check if the chore is not completed
    if chores_status[current_chore] != 'completed':
        print(f"{current_member} is assigned to: {current_chore}")
        chores_status[current_chore] = 'in progress'

        # Simulate the chore being done (in real life, you'd have a process here)
        # For now, just mark it as completed after a simulated time
        input("Press Enter when the chore is completed...")
        chores_status[current_chore] = 'completed'

    current_member_index += 1

# Display the completed chores
print("\nChore assignments and status:")
for chore, status in chores_status.items():
    print(f"{chore}: {status}")