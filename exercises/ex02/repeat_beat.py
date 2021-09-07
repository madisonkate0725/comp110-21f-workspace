"""Repeating a beat in a loop."""

__author__ = "730331607"


# Begin your solution here...

word_repeated: str = str(input("What beat do you want to repeat? "))
number_of_times_repeated: int = int(input("How many times do you want to repeat it? "))
counter: int = 0
if number_of_times_repeated <= 0:
    print("No beat...")
    
else:
    product: str = word_repeated
    while counter < number_of_times_repeated - 1:
        product = word_repeated + " " + product
        counter = counter + 1
    print(product)


