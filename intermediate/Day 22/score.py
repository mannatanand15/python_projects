from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.scoreboard()


    def scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score,align="left",font=("courier",50,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="right",font=("courier",50,"normal"))

    def l_update(self):
        self.l_score+=1
    def r_update(self):
        self.r_score+=1
