"""EX01 - A cute step toward Wordle."""
__author__ = "730615558"


length_counter: int = 0

word: str = input("Enter a 5-character word ")

if len(word) != 5:
    print("Error: Word is not 5 characters, try again!")
    exit()

character: str = input("Enter a single character ")

if len(character) != 1:
    print("Error: Character is not one character, try again!")

instance_counter: int = 0

print("Searching for " + character + " in " + word )

if character == word[0]: 
    print(character + " found at index 0")
    instance_counter = 1 + instance_counter

if character == word[1]: 
    print(character + " found at index 1")
    instance_counter = 1 + instance_counter
  

if character == word[2]:
    print(character + " found at index 2")
    instance_counter = 1 + instance_counter

if character == word[3]:
    print(character + " found at index 3")
    instance_counter = 1 + instance_counter

if character == word[4]:
    print(character + " found at index 4")
    instance_counter = 1 + instance_counter

if instance_counter == 0: 
    print(" No instances of " + character + " found in " + word)
else: 
    print(str(instance_counter) + " instance of " + character + " found in " + word)










    

