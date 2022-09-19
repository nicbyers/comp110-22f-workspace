"""Wordle, but for real this time!"""
__author__ = "730615558"

contains_chr: str = ""

def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes" 
    turn_counter: int = 0
    won: bool = False
    while turn_counter < 6 and not won: 
        print(f"===Turn {turn_counter + 1}/6===")
        guess: str = input_guess(len(SECRET))
        print(emojified(guess, SECRET)) 
        if guess == SECRET:
            won = True 
            print(f"You won in {turn_counter + 1}/6 turns!")

        else: 
            turn_counter = turn_counter + 1 
    if won == False:
        print("X/6 - Sorry, try again tomorrow!") 
        

def contains_char(word: str, singular_chr: str) -> bool: 
    """Checking to see whether character is found in word"""
    assert len(singular_chr) == 1 

    index: int = 0


    while index < len(word):
        if word[index] == singular_chr: 
            return True
        index += 1
    
    return False


def input_guess(expected_length: int) -> str:
    input_guess: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(input_guess) != expected_length: 
        input_guess = input("That was not " +  str(expected_length) + " letters! Try again:  ")
    return input_guess


def emojified(guess: str, SECRET: str) -> str:
    """Visual of whether character is found in word"""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    box_variable: str = ""

    word: str = ("What is your 5 character guess? ")

    index: int = 0

    assert len(guess) == len(SECRET)

    while index < len(SECRET):
        if guess[index] == SECRET[index]: 
            box_variable = box_variable + GREEN_BOX
        else: 
            if contains_char(SECRET, guess[index]):
                box_variable = box_variable + YELLOW_BOX
            
            else: 
                box_variable = box_variable + WHITE_BOX
        index = index + 1

    return box_variable

if __name__ == "__main__":
    main()