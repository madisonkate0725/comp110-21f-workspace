"""Finding duplicate letters in a word."""

__author__ = "730331607"

word: str = str(input("Enter a word: "))

duplicate: bool = False

i: int = 0 
j: int = 0
while i < len(word):
    while j < len(word):
        if word[j] == word[i] and i != j:
            duplicate = True
        j = j + 1
    j = 0
    i = i + 1

print("Found duplicate: " + str(duplicate))
