""""An example of a while loop statement."""

counter: int = 0
maximum: int = int(input("Count up to, but not including what?"))
while counter < maximum:
    print(counter)
    counter = counter + 1

print("Done!")