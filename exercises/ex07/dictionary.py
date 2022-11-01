"""A dictionary."""
__author__ = "730615558"

my_dict: dict[str, str] 


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Inverts dictionary keys and values."""
    new_dict: dict[str, str] = {}

    for key in my_dict: 
        if my_dict[key] in new_dict:
            raise KeyError("KeyError")
        new_dict[my_dict[key]] = key 
    
    return new_dict


def favorite_color(color: dict[str, str]) -> str:
    """Returns highest instance of favorite color."""
    new_dict: dict[str, int] = {}
    for key in color:
        if color[key] in new_dict: 
            new_dict[color[key]] += 1
        else:
            new_dict[color[key]] = 1
    current_max: int = 0
    color_max: str = "" 
    for key in new_dict: 
        if current_max < new_dict[key]:
            current_max = new_dict[key]
            color_max = key

    return color_max


def count(list_num: list[str]) -> dict[str, int]:
    """Counts the number of times that a value appears in an input list."""
    new_dict: dict[str, int] = {}

    for i in range(0, len(list_num)):
        if list_num[i] in new_dict:
            new_dict[list_num[i]] += 1
        else: 
            new_dict[list_num[i]] = 1 

    return new_dict 
