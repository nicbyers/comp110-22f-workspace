"""Utility Functions."""
__author__ = "730615558"

def only_evens(input: list[int]) -> list[int]:
    """Checking for even numbers in a list."""
    list_int: list[int] = []
    i: int = 0 
    while i < len(input):
        if input[i] % 2 == 0:
            list_int.append(input[i])
        i += 1

    return list_int


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    list_cc: list[int] = []
    i: int = 0
    while i < len(list_1):
        list_cc.append(list_1[i])
        i += 1
    
    i = 0

    while i < len(list_2):
        list_cc.append(list_2[i])
        i += 1

    return list_cc


def sub(a_list: list[int], int_1: int, int_2: int) -> list[int]:
    result: list[int] = []

    if int_1 < 0:
        int_1 = 0 
    
    if int_2 > len(a_list):
        int_2 = len(a_list)

    if len(a_list) == 0:
        return result 
    
    if int_1 > len(a_list):
        return result 
    
    if int_2 == 0:
        return result

    i: int = int_1

    while i < int_2: 
        result.append(a_list[i])
        i += 1
    return result
