"""List utility functions."""

__author__ = "730331607"


# TODO: Implement your functions here.

def all(the_list: list[int], the_int: int) -> bool:
    """Determines whether or not all the integers are the same as a chosen integer."""
    i: int = 0
    if len(the_list) == 0:
        return False
    while i < len(the_list):
        item: int = the_list[i]
        if item != the_int:
            return False
        i += 1
    return True


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determining whether every index is equal between two lists."""
    i: int = 0
    if len(list_1) == 0 and len(list_2) == 0:
        return True
    if len(list_1) == 0:
        return False
    if len(list_2) == 0:
        return False
    if len(list_2) != len(list_1):
        return False
    if len(list_1) <= len(list_2):
        while i < len(list_1):
            item_: int = list_2[i]
            if item_ != list_1[i]:
                return False
            i += 1
        return True
    else:
        while i < len(list_1):
            item_: int = list_1[i]
            if item_ != list_2[i]:
                return False
            i += 1
        return True


def max(a_list_of_int: list[int]) -> int:
    """A function to find the max integer of a list."""
    if len(a_list_of_int) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    j: int = 1
    maxval: int = a_list_of_int[i]
    while i < len(a_list_of_int):
        while j < len(a_list_of_int):
            if a_list_of_int[j] <= a_list_of_int[i] and i != j and maxval < a_list_of_int[i]:
                maxval: int = a_list_of_int[i]
            j += 1
        j = 0
        i += 1
    return maxval
        

print(max([3, 5, 3, 4, 1]))


# def max(a_list_of_int: list[int]) -> int:
#     """A function to find the max integer of a list."""
#     if len(a_list_of_int) == 0:
#         raise ValueError("max() arg is an empty List")
#     i: int = 0
#     j: int = 1
#     maxval: int = a_list_of_int[i]
#     while i < len(a_list_of_int):
#         while j < len(a_list_of_int):
#             if a_list_of_int[j] < a_list_of_int[i] and i != j:
#                 maxval: int = a_list_of_int[i]
#             j += 1
#         j = 0
#         i += 1
#     return maxval