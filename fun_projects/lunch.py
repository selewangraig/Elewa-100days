#I just got a new job and there's a really good kibandaski around.
#They sell a variety of stuff including:
#main dish - Rice, Chapati, Ugali
#side dish - Ndengu, Kamande, Peas
#soup
#greens - sukuma, spinach, cabbage
#meat - beef, Nyamchom!!!!!!!!!
#fruits - orange, mango, apple, passion
#fresh juice - Pineapple mint, Sugarcane, Mango, Passion, Tropical(i mean mixed lol)
#I want to write a program that will help me decide what to eat for lunch from monday to thursday.
#Friday ni siku ya sherehe, nakula ugali, greens na nyamachoma alafu ka pineapple mint hapo kando...

#so this program will take user input on available food in his/her region
#then output a random menu for each day of the week.

import random
def main():
    global main_dish, side_dish, soup, greens, meat, fruits, fresh_juice
    main_dish = []
    side_dish = []
    greens = []
    meat = []
    fruits = []
    fresh_juice = []
    while True:
        main = input("Enter the main dishes available eg 'rice': ")
        if main == "":
            break
        main_dish.append(main)
    while True:
        side = input("Enter the side dishes available eg 'ndengu': ")
        if side == "":
            break
        side_dish.append(side)
    while True:
        green = input("Enter the greens available eg 'sukuma': ")
        if green == "":
            break
        greens.append(green)
    while True:
        meat_ = input("Enter the meat available eg 'beef': ")
        if meat_ == "":
            break
        meat.append(meat_)
    while True:
        fruit = input("Enter the fruits available eg 'mango': ")
        if fruit == "":
            break
        fruits.append(fruit)
    while True:
        juice = input("Enter the fresh juices available eg 'pineapple mint': ")
        if juice == "":
            break
        fresh_juice.append(juice)

def get_menu():
    global main_dish, side_dish, soup, greens, meat, fruits, fresh_juice
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for day in days:
        main = random.choice(main_dish)
        side = random.choice(side_dish)
        green = random.choice(greens)
        meat_ = random.choice(meat)
        fruit = random.choice(fruits)
        juice = random.choice(fresh_juice)
        print(f"{day} - {main}, {side}, {green}, {meat_}, {fruit}, {juice} juice")
    
main()
get_menu()
