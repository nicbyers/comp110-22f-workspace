"""Listing Utility Functions"""
__author__ = "730615558"

def all(haystack: list[int], needle: int,) -> bool:
    i: int = 0 
    while i < len(haystack):
        if haystack[i] == needle:
            return True 
        i += 1 
    return False

def max(input: list[int]) -> int:
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
    if list_1 == list_2:
        return True
    else: 
        return False 
