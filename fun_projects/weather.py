#This is a simple command-line program that will;
#The program will take user input on the clothes they have in their wardrobe
#and depending on the weather, the program will then randomly output the perfect outfit for that weather.
#The program will also output the temperature and the weather forecast for the day.

import random

def get_clothes():
    global tshirts, shirts, pants, shorts, sweaters
    tshirts = []
    shirts = []
    pants = []
    shorts = []
    sweaters = []
    while True:
        tshirt = input("Enter the tshirts in your wardrobe eg 'black t-shirt': ")
        if tshirt == "":
            break
        tshirts.append(tshirt)
    while True:
        shirt = input("Enter the shirts in your wardrobe eg 'black shirt': ")
        if shirt == "":
            break
        shirts.append(shirt)
    while True:
        pant = input("Enter the pants in your wardrobe eg 'black pants': ")
        if pant == "":
            break
        pants.append(pant)
    while True:
        short = input("Enter the shorts in your wardrobe eg 'black shorts': ")
        if short == "":
            break
        shorts.append(short)
    while True:
        sweater = input("Enter the sweaters in your wardrobe eg 'black sweater': ")
        if sweater == "":
            break
        sweaters.append(sweater)

def get_weather():
    global tshirts, shirts, pants, shorts, sweaters
    weather = input("Enter the weather for today eg 'sunny': ")
    if weather == "sunny":
        sunny_tshirt = random.choice(tshirts)

        preference = input("Do you prefer shorts or pants? ")

        if preference == "shorts":
            sunny_shorts = random.choice(shorts)
            print(f"You should put on a {sunny_tshirt} and a {sunny_shorts}")
        elif preference == "pants":
            sunny_pants = random.choice(pants)
            print(f"You should put on a {sunny_tshirt} and a {sunny_pants}")
        else:
            print("Please enter either 'shorts' or 'pants'")
    elif weather == "rainy":
        rainy_sweater = random.choice(sweaters)
        rainy_pants = random.choice(pants)
        print(f"You should put on a {rainy_sweater} and a {rainy_pants}. Don't forget an umbrella :)")
    elif weather == "cloudy":
        cloudy_shirt = random.choice(shirts)
        cloudy_pants = random.choice(pants)
        cloudy_sweater = random.choice(sweaters)
        print(f"You should put on a {cloudy_shirt} and a {cloudy_pants}. Probably carry a {cloudy_sweater}")
    else:
        print("Please enter either 'sunny', 'rainy' or 'cloudy'")

print("Welcome to my Wardrobe Program!")
print("This program will help you decide what to wear based on the weather.")
get_clothes()
get_weather()