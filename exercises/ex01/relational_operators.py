"""Practicing with inputs and numerical expressions"""

__author__ = "730331607"

first_number: int = int(input("Left-Hand side: "))
second_number: int = int(input("Right-Hand side: "))

answer_1: bool = bool(first_number < second_number)

print(str(first_number) + " < " + str(second_number) + " is " + str(answer_1))

answer_2: bool = bool(first_number >= second_number)

print(str(first_number) + " >= " + str(second_number) + " is " + str(answer_2))

answer_3: bool = bool(first_number == second_number)

print(str(first_number) + " == " + str(second_number) + " is " + str(answer_3))

answer_4: bool = bool(first_number != second_number)

print(str(first_number) + " != " + str(second_number) + " is " + str(answer_4))