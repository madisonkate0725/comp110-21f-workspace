"""An exercise in remainders and boolean logic."""

__author__ = "730331607"

integer: int = int(input("Enter an int: "))

if bool(integer % 2 == 0) and bool(integer % 7 == 0):
    print("TAR HEELS")
else:
    if (int((integer % 2))) == 0:
        print("TAR")
    else:
        if int((integer % 7) == 0):
            print("HEELS")
        else:
            print("CAROLINA")
