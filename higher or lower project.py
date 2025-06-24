#display art
import art            #(from art import logo)
# create dictionary and generate a random account from the list
from game_data import data
import random     #this is an imp step


def check_answer(user_guess,a_followers,b_followers):
    if a_followers>b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"

def format_account(account):
    name=account["name"]
    descr=account["description"]
    country=account["country"]
    return f" {name},a {descr},from {country}"
print(art.logo)
score=0
account_b= random.choice(data)

#format the account data into printable format
game_continue=True
while game_continue:
    account_a=account_b
    account_b=random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A:{format_account(account_a)}")
    print(art.vs)
    print(f"Compare B:{format_account(account_b)}")

    #check follower count of each

    #make user guess
    guess=input("guess who has more follower count? A or B ").lower()
    print("\n"*20)
    print(art.logo)
    a_count=account_a["follower_count"]
    b_count=account_b["follower_count"]
    is_correct=check_answer(guess,a_count,b_count)
    #print score and give feedback
    if is_correct:
        score+=1
        print(f"you are right.your score is {score}")
    else:
        print(f"incorrect guess. your final score is {score}")
        game_continue=False
#making the game repeatable





