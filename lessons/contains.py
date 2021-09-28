""""Example of writing a function to process a lists."""

def main() -> None:
    """Entrypoint of program."""
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kevin", names))
#Define a function
def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in the haystack, False otherwise"""
    #Name 'contains'
    #Two paramenters (needle(str), haystack(List))
    #Return true if needle is found in the haystack
        # Move through each item in list until needle is found
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1
    return False
        # As soon as a needle is found return true
        #If all items have been checked return false
if __name__ == "__main__":
    main()