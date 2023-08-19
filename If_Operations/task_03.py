#program that will help you choose a gift for someone.
#write code that will help you  find the best gift to give someone.

#function that will ask the user what the giftee likes
import random

def giftee():
    print("Gift Chooser")
    print("1 - Books")
    print("2 - Movies")
    print("3 - Games")

    global gift
    gift = input("What is their favourite thing? ")

    return gift

def books():
    global gift
    if gift == "1":
        print("\n")
        print("1. Motivational")
        print("2. Fantasy")
        print("3. Horror")
        book_choice =  input("What book genre do they like?")

        if book_choice == "1":
            motivation_list = ["'7 Habits of Highly Effective People' by Stephen R. Covey",
                               "'Awaken the Giant Within' by Tony Robbins",
                               "'Think and Grow Rich' by Napoleon Hill"]
            random_book = random.choice (motivation_list)
            print(f"\nYou should buy them: {random_book}")

        elif book_choice == "2":
            fantasy_list = ["'The Lord of the Rings' by J.R.R. Tolkien",
                            "'A Song of Ice and Fire' series by George R.R. Martin",
                            "'Harry Potter' series by J.K. Rowling"]
            random_book = random.choice(fantasy_list)
            print(f"\nYou should buy them: {random_book}")
        
        elif book_choice == "3":
            horror_list = ["'The Shining' by Stephen King",
                           "'The Haunting of Hill House' by Shirley Jackson",
                           "'The Exorcist' by William Peter Blatty"]
            random_book = random.choice(horror_list)
            print(f"\nYou should buy them: {random_book}")
        else:
            print("\nInvalid Choice!")
    else:
        print("\nInvalid Choice!")

def movies():
    global gift
    if gift == "2":
        print("\n")
        print("1. Action/Adventure")
        print("2. Comedy")
        print("3. Horror")
        movie_choice = input("Which type of film would they prefer?")

        if movie_choice == "1":
            actionadventure_list = ["Jumanji", "Jurassic Park", "Mad Max: Fury"]
            random_movie = random.choice(actionadventure_list)
            print(f"\nYou should buy them: {random_movie}") 
        
        elif movie_choice == "2":
            comedy_list = ["The Office", "Friends", "Big Bang Theory"]
            random_movie = random.choice(comedy_list)
            print(f"\nYou should buy them: {random_movie}")
        
        elif movie_choice == "3":
            horror_list = ["The Nun", "Annabelle", "Lights Out"]
            random_movie = random.choice(horror_list)
            print(f"\nYou should buy them: {random_movie}")
        
        else:
            print("\nInvalid Choice!")
    else:
        print("\nInvalid Choice!")

def games():
    global gift
    if gift == "3":
        print("\n")
        print("1. Board Games")
        print("2. Video Games")
        game_choice = input("What kind of game do they like?")

        if game_choice == "1":
            boardgame_list = ["Monopoly", "Chess"]
            random_game = random.choice(boardgame_list)
            print(f"\nYou should buy them: {random_game}")
        
        elif game_choice == "2":
            video_list = ["Call Of Duty", "Minecraft"]
            random_game = random.choice(video_list)
            print(f"\nYou should buy them: {random_game}")

        else:
            print("\nInvalid Choice")
    else:
        print("\nInvalid Choice")

def check_gift():
    global gift
    if gift == "1":
        books()
    elif gift == "2":
        movies()
    elif gift == "3":
        games()
    else:
        print('No Gift')
    
giftee()
check_gift()