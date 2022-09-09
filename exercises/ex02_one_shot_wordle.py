"""EX02 - One Shot Wordle!"""
__author__ = "730615558"

length_counter: int = 0 
SECRET: str = "python"

word: str = input("What is your 6 letter guess? ")

while len(word) != len(SECRET): 
    word = input("That was not 6 letters! Try again:  ")


constant: int = 0


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

box_variable: str = ""


while constant < 6:
    if word[constant] == SECRET[constant]: 
        box_variable = box_variable + GREEN_BOX
    else:

        chr_pos: bool = False
        guess_constant: int = 0
    
        while not chr_pos and guess_constant < len(SECRET):
            if SECRET[guess_constant] == word[constant]: 
                chr_pos = True
            else: 
                guess_constant = guess_constant + 1
        if chr_pos:
            box_variable = box_variable + YELLOW_BOX
           

        else: 
            box_variable = box_variable + WHITE_BOX
    constant = constant + 1


print(box_variable)

   
if word == SECRET: 
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")