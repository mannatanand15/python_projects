from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=1
        self.goto(-220,250)
        self.write("Level-",font=FONT)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level-{self.level}",align="center",font=FONT)
#turtle only accepts american english so the align would be "center" not "centre"

    def increase_score(self):
        self.update()
        self.level += 1
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",font=FONT)
