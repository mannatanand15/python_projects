from random import randint
easy_turns=10     #global variables
hard_turns=5
turns=0
def check(user_guess,answer,turns):
    """checks answers against guess and tell the remaining guesses"""
    if user_guess>answer:
        print ("too high")
        return turns-1
    elif user_guess<answer:
        print("too low")
        return turns-1           #to end loop
    else:
        print("you win")
def set_level():
    level=input("Choose a difficulty.Type 'easy' or 'hard':")
    if level=='easy':
        return easy_turns
    else:
        return hard_turns
def game():
    print("Welcome to number guessing game!\n I am thinking of a number between 1 to 100.")
    answer=randint(1,100)
    turns=set_level()
    guess=0
    while guess!=answer:      #to continue the running of loop
        print(f"you have {turns} remaining turns ")
        guess=int(input("make a guess:"))
        turns= check(guess,answer,turns)
        if turns==0:
            print("you run out of guesses.you lose")
            return
        elif guess!=answer:
            print("guess again")
game()
#track the number of terms and reduce them by 1

