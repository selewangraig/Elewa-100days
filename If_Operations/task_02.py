#Write a program that will help you decide on what will influence your career choice
#Career is influenced by? salary, satisfaction, location
#do this like a game.
#start with salary and satisfaction.
#if they choose salary, compare with location.
#if they choose salary again..
#store the ans in a list.
#compare location with satisfaction
#store whichever they choose as the second item in list and the other as last
#output the list stating that is how they choose their career


print("Welcome to Career Influencer.")
print("This game will help you figure out what matters most to you when choosing a career.")

preference_list = []
salary = 0
location = 0
satisfaction = 0

print("\n")
print("Would you rather?... ")
print("A. Have a 6 figure salary but be dissatisfied in your career")
print("B. Have extreme satisfaction with basic/average pay ")
choice1 = input("Enter your choice (letter only): ")

if choice1 == "a":
    salary += 1

    print("\n")
    print("Would you rather?... ")
    print("C. Have the 6 figure salary but work on-site.")
    print("D. Get the average pay but get to decide where you want to work. ")
    choice2 = input("Enter your choice (letter only): ")

    if choice2 == "c":
        salary += 1

        print("\n")
        print("Would you rather?... ")
        print("E. Work from anywhere but be extremely dissatisfied in your career.")
        print("F. Be extremely satisfied but have to work on-site.")
        choice3 = input("Enter your choice (letter only): ")
        
        if choice3 == "e":
            location += 1

            preference_list.append("Salary")
            preference_list.append("Location")
            preference_list.append("Satisfaction")

            print(preference_list)
        elif choice3 == "f":
            satisfaction += 1

            preference_list.append("Salary")
            preference_list.append("Satisfaction")
            preference_list.append("Location")

            print(preference_list)
        else:
            print("Invalid entry!")
    
    elif choice2 == "d": 
        location += 1
        
        preference_list.append("Location")
        preference_list.append("Salary")
        preference_list.append("Satisfaction")

        print(preference_list)
    else:
        print("Invalid entry!")

elif choice1 == "b":
    satisfaction += 1
    
    print("\n")
    print("Would you rather?... ")
    print("C. Work from anywhere but be extremely dissatisfied in your career.")
    print("D. Be extremely satisfied but have to work on-site.")
    choice4 = input("Enter your choice (letter only): ")

    if choice4 == "c":
        preference_list.append("Location")
        preference_list.append("Satisfaction")
        preference_list.append("Salary")

        print(preference_list)
    elif choice4 == "d":
        
        print("\n")
        print("Would you rather?... ")
        print("E. Have the 6 figure salary but work on-site.")
        print("F. Get the average pay but get to decide where you want to work.")
        choice5 = input("Enter your choice (letter only): ")

        if choice5 == "e":
            preference_list.append("Satisfaction")
            preference_list.append("Salary")
            preference_list.append("Location")

            print(preference_list)

        elif choice5 == "f":
            preference_list.append("Satisfaction")
            preference_list.append("Location")
            preference_list.append("Salary")
            
            print(preference_list)
        else:
            print("Invalid entry!")
    else:
        print("Invalid Entry!")
else:
    print("Invalid entry!")