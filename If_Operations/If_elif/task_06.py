# Assignment 2 - Scenario 3: Event Planning as Committee Chair
event_date = "August 29"
print(f"As the chair of the event committee, plan the event for {event_date}.")

while True:
    print("Choose the flow of events: (opening ceremony/games/performances/closing ceremony)")
    event_choice = input().lower()

    if event_choice == "opening ceremony":
        print("Plan the opening ceremony details.")
    elif event_choice == "games":
        print("Plan the games and activities for participants.")
    elif event_choice == "performances":
        print("Plan the performances and entertainment.")
    elif event_choice == "closing ceremony":
        print("Plan the closing ceremony details.")
    elif event_choice == "done":
        break
    else:
        print("Invalid choice. Please select from the provided options.")

print(f"Event planning for {event_date} is complete.")