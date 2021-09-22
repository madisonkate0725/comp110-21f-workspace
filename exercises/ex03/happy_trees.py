"""Drawing forests in a loop."""

__author__ = "730331607"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
counter: int = 0

depth: int = int(input("Depth: "))
if depth > 0:
    product: str = TREE
    while counter < depth:
        counter = counter + 1
        product = TREE * counter
        print(product)
  