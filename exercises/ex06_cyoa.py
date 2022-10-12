"""Buckle up buttercup, it's princess time!"""
__author__ = "730615558"

player: str = ""
points: int = 0 
play_pts: int = 0

def main() -> None: 
    greet()
    x: bool = True 
    while x: 
        result = input("start_1, start_ 2, stop: ")
        if result == "start_1":
            question_a()
            question_b()
            question_c()
            question_d()
            question_e()
            finale()
        elif result == "start_2":
            question_b()
            question_c()
            question_d()
            question_e()
            finale()
        elif result == "stop":
            x = False
            print("See ya next time!")
            exit()


def greet() -> None:
    global player
    print("Hello, welcome to 'Which Disney Princess Are You?' quiz. Your job is to answer a few questions, and by the end of this quiz you will see which disney princess you are! Before we start...")
    player = input("What is your name? ")


def player_points(play_pts: int) -> int: 
    


def question_a() -> None: 
    global points
    print("How do you see yourself?: ")
    input_ques_a = input("kind, courageous, bold: ")
    if input_ques_a == "kind": 
        points += 1
    elif input_ques_a == "courageous":
        points += 4
    elif input_ques_a == "bold":
        points += 5


def question_b() -> None: 
    global points 
    print("How do others see you?: ")
    input_ques_b = input("playful, shy, naive: ")
    if input_ques_b  == "playful": 
        points += 10
    elif input_ques_b == "shy": 
        points += 5 
    elif input_ques_b == "naive":
        points += 10 


def question_c() -> None: 
    global points 
    print("How would you describe yourself when it comes to getting what you want?: ")
    input_ques_c = input("ambitious, outspoken, strong-willed: ")
    if input_ques_c == "ambitious":
        points += 15 
    elif input_ques_c == "outspoken":
        points += 20
    elif input_ques_c == "strong-willed":
        points += 15


def question_d() -> None: 
    global points
    print("What do you value?: ")
    input_ques_d = input("spirituality, independence, rebellion")
    if input_ques_d == "spirituality":
        points += 25 
    elif input_ques_d == "independence":
        points += 20
    elif input_ques_d == "rebellion":
        points += 20
    

def question_e() -> None: 
    global points
    print("What trait could you not live without?: ")
    input_ques_e = input("intelligence, curiousity, outspokenness")
    if input_ques_e == "intelligence":
        points += 15 
    elif input_ques_e == "curiosity":
        points += 15 
    elif input_ques_e == "outspokenness":
        points = 20 

def finale() -> str:
    global points
    if points < 21:
        if points <= 5:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Snow White!")

        if points > 5 and points < 11:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Cinderella!")
        
        if points > 10 and points < 16:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Aurora!")
        
        if points > 15 and points < 21:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Ariel!")
        
    if points > 20:

        if points > 20 and points < 26: 
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Belle")

        if points > 25 and points < 31:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Tiana")

        if points > 30 and points < 36:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Jasmine!")
        
        if points > 35 and points < 41:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Mulan")

        if points > 40 and points < 46:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Rapunzel!")
        
        if points > 45 and points < 51:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Merida!")
        
        if points > 50 and points < 56:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Moana!")
        
        if points > 55 and points < 61:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Raya!")
        
        if points > 60 and points < 66:
            print(f"You have {points} points! Congrats" + player + ", your Disney Princess is Pocahontas!")


if __name__ == "__main__":
    main()