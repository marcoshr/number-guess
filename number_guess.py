"""
The program should do the following:

Roll a pair of dice.
Add the values of the roll.
Ask the user to guess a number.
Compare the user's guess to the total value.
Determine the winner (user or computer).
"""
from random import randint
from time import sleep

def get_user_guess():
    guess = int(input("Guess please: "))
    return guess

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides*2
    print ('Number of sides is {0}'.format(max_val))

    guess = get_user_guess()
    if guess > max_val:
        print ("ups, more than max")
    else:
        print ("Rolling...")
        sleep(2)
        print ('First is {0}'.format(first_roll))
        sleep(1)
        print ('Second is {0}'.format(second_roll))
        sleep(1)
        total_roll = first_roll + second_roll
        print ('Total is {0}'.format(total_roll))
        print ("Result...")
        sleep(1)
        if guess == total_roll:
            print ("You win")
        else:
            print ("You lost")

roll_dice(6)