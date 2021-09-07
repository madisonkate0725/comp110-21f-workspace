"""Repeating a beat in a loop."""

__author__ = "730331607"


# Begin your solution here...

word_repeated: str = str(input("What beat do you want to repeat? "))
number_of_times_repeated: int = int(input("How many times do you want to repeat it? "))
counter: int = 0

while counter < number_of_times_repeated:
    print(word_repeated)
    counter = counter + 1
    if counter <= 0:
        print("No beat...")
