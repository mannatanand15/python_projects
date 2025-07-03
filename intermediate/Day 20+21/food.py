# IN THIS PROGRAM WE ARE USING CONCEPT OF INHERITANCE

from turtle import Turtle
import random

#we wish the food class to inherit turtle class
#food(subclass) & turtle(superclass)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        #generally the size of any turtle object is 20*20
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x=random.randint(-180,180)
        random_y=random.randint(-180,180)
        self.goto(random_x,random_y)

