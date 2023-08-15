#Write a python program that will prompt the user to input their credit card information
#and check whether the information shared is a string or an integer
#credit cards have name, number, expiration date, cvv.


#import date module
from datetime import date

#function to prompt user to input credit card information
def credit_card_info():
    global user_name, card_num, exp_date_month, exp_date_year, exp_date_day, exp_date, card_cvv
    user_name = input("Enter the card holder's name: ")
    card_num = int(input("Enter credit card number: "))
    exp_date_year = int(input("Enter expiration date year: "))
    exp_date_month = int(input("Enter expiration date month: "))
    exp_date_day = int(input("Enter expiration date day: "))
    exp_date = date(exp_date_year, exp_date_month, exp_date_day)
    card_cvv = int(input("Enter your credit card cvv: "))

    return user_name, card_num, exp_date, card_cvv

#function to check whether the information shared is a string or an integer
def check_card_info():
    global user_name, card_num, exp_date, card_cvv
    card_info = [user_name, card_num, exp_date, card_cvv]
    for item in card_info:
        if type(item) == str:
            print(f"{item} is a string")
        elif type(item) == int:
            print(f"{item} is an integer")
        else:
            print(f"{item} is not a string or an integer")

#function call
credit_card_info()
print("\n")
check_card_info()