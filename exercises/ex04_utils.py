"""Listing Utility Functions."""
__author__ = "730615558"


def all(haystack: list[int], needle: int,) -> bool:
    """Checking a list of integers to see if input matches the entire list."""
    i: int = 0 

    if len(haystack) == 0: 
        return False
        
    while i < len(haystack):
        if haystack[i] == needle:
         i += 1 
        else: 
            return False

    return True


def max(input: list[int]) -> int:
    """Checking for the maximum output in a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    current_max: int = input[0]
    i: int = 0 

    while i < len(input):
        if input[i] > current_max:
            current_max = input[i]
        i += 1 

    return current_max


def is_equal(list_1: list[int], list_2: list[int]) -> int: 
    """Checking to see if lists of integers match."""
    if list_1 == list_2:
        return True
    else: 
        return False 
