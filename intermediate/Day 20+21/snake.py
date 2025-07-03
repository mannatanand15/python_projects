from turtle import Turtle
SNAKE_POSITIONS=[(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP= 90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

#TODO 1:Create a snake body
#by using a tuple or by specifying different segments

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
        # segment1=Turtle(shape="square")
        # segment1.color("white")
        #
        # segment2=Turtle(shape="square")
        # segment2.color("white")
        # segment2.goto(x=-20,y=-0)
        #
        # segment3=Turtle(shape="square")
        # segment3.color("white")
        # segment3.goto(x=-40,y=0)0
    # TODO 6: EXTEND THE SNAKE EVERYTIME IT HITS THE FOOD

    # TODO 2: MOVE THE SNAKE

    def move(self):
    #for loop and range(start,stop,skip)
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

#TODO 3: CONTROL THE SNAKE
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)           #any change should be made in turtle at zero index
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
