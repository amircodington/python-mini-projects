import sys
from random import randint


def game_number(start, stop):
    random_number = randint(int(start), int(stop))
    return random_number


def get_number():
    number = int(input('Guess a number: '))
    return number


correct_number = game_number(sys.argv[1], sys.argv[2])
user_guess = None
while user_guess != correct_number:
    try:
        user_guess = get_number()
        if user_guess > correct_number:
            print('It\'s big')
        elif user_guess < correct_number:
            print('It\'s small')
    except ValueError:
        print("Please enter number!!")
print("Bravoooo!!!")
