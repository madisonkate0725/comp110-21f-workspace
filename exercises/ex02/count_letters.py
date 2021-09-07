"""Counting letters in a string."""

__author__ = "730331607"


# Begin your solution here...

letter: str = str(input("What letter do you want to seach for?: "))

word: str = str(input("Enter a word: "))

occurance_of_letters: int = 0

position_on_string = int = 0 

while position_on_string < len(word):
    if word[position_on_string] == letter:
        occurance_of_letters = occurance_of_letters + 1
    position_on_string = position_on_string + 1

total_number_of_letters: str = str(occurance_of_letters)

print("Count: " + total_number_of_letters)