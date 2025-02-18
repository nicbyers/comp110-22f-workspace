"""Buckle up buttercup, it's princess time!"""
__author__ = "730615558"

from random import randint

player: str = ""
points: int = 0 
GRINNING_FACE_COWBOY: str = "\U0001F920"


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    greet()
    x: bool = True 
    while x: 
        result = input("start_1, start_ 2, stop: ")
        if result == "start_1":
            player_points(points)
            question_a()
            player_points(points)
            question_b()
            player_points(points)
            question_c()
            player_points(points)
            question_d()
            player_points(points)
            question_e()
            finale()

        elif result == "start_2":
            player_points(points)
            question_b()
            player_points(points)
            question_c()
            player_points(points)
            question_d()
            player_points(points)
            question_e()
            finale()

        elif result == "stop":
            x = False
            random: int = randint(0, 100)
            print(f"See ya next time, {player}! Here's a random number just for fun: {random} {GRINNING_FACE_COWBOY}")
            exit()
        

def greet() -> None:
    """Greets the player."""
    global player
    print("Hello, welcome to 'Which Disney Princess Are You?' quiz. Your job is to answer a few questions, and by the end of this quiz you will see which disney princess you are! Before we start...")
    player = input("What is your name? ")


def player_points(player_points: int) -> int:
    """Returns points accrued at the end of the game."""
    points = player_points
    print(f"This is currently your point count: {points}")
    return points


def question_a() -> None:
    """First question of quiz.""" 
    global points
    print("How do you see yourself?")
    input_ques_a = input("kind, courageous, bold: ")
    if input_ques_a == "kind": 
        points += 1
    elif input_ques_a == "courageous":
        points += 4
    elif input_ques_a == "bold":
        points += 5


def question_b() -> None: 
    """Second question of quiz."""
    global points 
    print("How do others see you?")
    input_ques_b = input("playful, shy, naive: ")
    if input_ques_b == "playful": 
        points += 10
    elif input_ques_b == "shy": 
        points += 5 
    elif input_ques_b == "naive":
        points += 10 


def question_c() -> None:
    """Third question of quiz.""" 
    global points 
    print("How would you describe yourself when it comes to getting what you want?")
    input_ques_c = input("ambitious, outspoken, strong-willed: ")
    if input_ques_c == "ambitious":
        points += 15 
    elif input_ques_c == "outspoken":
        points += 20
    elif input_ques_c == "strong-willed":
        points += 15


def question_d() -> None:
    """Fourth question of quiz.""" 
    global points
    print("What do you value? ")
    input_ques_d = input("spirituality, independence, rebellion: ")
    if input_ques_d == "spirituality":
        points += 25 
    elif input_ques_d == "independence":
        points += 20
    elif input_ques_d == "rebellion":
        points += 20
    

def question_e() -> None:
    """Fifth question of quiz.""" 
    global points
    print("What trait could you not live without? ")
    input_ques_e = input("intelligence, curiousity, outspokenness: ")
    if input_ques_e == "intelligence":
        points += 15 
    elif input_ques_e == "curiosity":
        points += 15 
    elif input_ques_e == "outspokenness":
        points = 20 


def finale() -> None:
    """Check point value against princess range."""
    global points
    if points < 21:
        if points <= 5:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Snow White!")

        if points > 5 and points < 11:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Cinderella!")
        
        if points > 10 and points < 16:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Aurora!")
        
        if points > 15 and points < 21:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Ariel!")
        
    if points > 20:

        if points > 20 and points < 26: 
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Belle")

        if points > 25 and points < 31:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Tiana")

        if points > 30 and points < 36:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Jasmine!")
        
        if points > 35 and points < 41:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Mulan")

        if points > 40 and points < 46:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Rapunzel!")
        
        if points > 45 and points < 51:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Merida!")
        
        if points > 50 and points < 56:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Moana!")
        
        if points > 55 and points < 61:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Raya!")
        
        if points > 60:
            print(f"You have {points} points! Congrats {player}, your Disney Princess is Pocahontas!")

        if points > 80:
            print("You're out of range, please restart the quiz!")
        exit()


if __name__ == "__main__":
    main()