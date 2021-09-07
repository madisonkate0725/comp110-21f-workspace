"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730331607"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

cookie_number: int = randint(1, 10)

if cookie_number == 1:
    print("Soon you will come into a large fortune!")
else: 
    if cookie_number == 2:
        print("You will find free food this week!")
    else:
        if cookie_number == 3:
            print("Soon you will hear great news you have been waiting on!")
        else:
            if cookie_number == 4:
                print("If you finally do your laundry this week, you will feel productive!")
            else:
                if cookie_number == 5:
                    print("You will do well on all your assignments this week!")
                else: 
                    if cookie_number == 6:
                        print("A new opportunity will present itself soon!")
                    else:
                        if cookie_number == 7:
                            print("This week you will start to practice more selfcare!")
                        else: 
                            if cookie_number == 8:
                                print("You will discover a new hobby!")
                            else: 
                                if cookie_number == 9:
                                    print("You will finish that thing you have been working on forever!")
                                else:
                                    if cookie_number == 10:
                                        print("You will discover a new hobby this week!")

print("Now, go spread positive vibes!")