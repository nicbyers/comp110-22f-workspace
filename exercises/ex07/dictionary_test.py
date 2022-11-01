"""Testing function instances."""

from dictionary import invert
from dictionary import favorite_color
from dictionary import count 


def test_dictionary_invert_1() -> None:
    """Checks for empty list."""
    dict_1: dict[str, str] = {}
    assert invert(dict_1) == {}


def test_dictionary_invert_2() -> None: 
    """Inverts keys and values within a dictionary."""
    dict_1: dict[str, str] = {'toxic': 'water', 'missing': 'bricks', 'north': 'south'}
    assert invert(dict_1) == {'water': 'toxic', 'bricks': 'missing', 'south': 'north'}


def test_dictionary_invert_3() -> None: 
    """What happens when values are the same and are inverted to matching keys."""
    dict_1: dict[str, str] = {'kris': 'jordan'}
    assert invert(dict_1) == {'jordan': 'kris'}


def test_dictionary_favorite_color_4() -> None:
    """What happens when there is an empty list."""
    dict_1: dict[str, str] = {}
    assert favorite_color(dict_1) == ""


def test_dictionary_favorite_color_5() -> None: 
    """Returns the most common color."""
    dict_1: dict[str, str] = {"Frannie": "yellow", "Nick": "blue", "Jacob": "blue"}
    assert favorite_color(dict_1) == "blue"


def test_dictionary_favorite_color_6() -> None: 
    """What is returned when most common color is tied."""
    dict_1: dict[str, str] = {"Marah": "yellow", "Urvi": "blue", "AAron": "red"}
    assert favorite_color(dict_1) == "yellow"


def test_dictionary_count_7() -> None: 
    """What happens when there is an empty string."""
    list_1: list[str] = []
    assert count(list_1) == {} 


def test_dictionary_count_8() -> None: 
    """Counting the number of times the same key appears."""
    dict_1: list[str] = ['UNC', 'Duke', 'NCSU']
    assert count(dict_1) == {'UNC': 1, 'Duke': 1, 'NCSU': 1}


def test_condition_count_9() -> None:
    """When there is two values in a string."""
    dict_1: list[str] = ["unc", "duke"]
    assert count(dict_1) == {"unc": 1, "duke": 1}
