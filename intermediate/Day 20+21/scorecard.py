#TODO 5:CREATE A SCOREBOARD   (we will do that using a turtle only using write function)
from turtle import Turtle

class Scorecard (Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.score +=1
        self.update_score()
