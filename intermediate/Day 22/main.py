import turtle as t
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen=Screen()
score=Score()
screen.bgcolor("black")
#TODO 1:CREATE A SCREEN
screen.setup(width=800,height=600)
screen.title("Pingpong Game")
screen.tracer(0)  #used to turn off animation
#TODO 2:CREATE AND MOVE THE PADDLE
paddle=Turtle()
ball=Ball()
ball.speed("fastest")
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on=True

while game_on:
    time.sleep(ball.move_speed)
    paddle.move()
    ball.move()
    screen.update()
    ball.move()
     # TODO 4:DETECT COLLISION WITH WALL AND BOUNCE
    if ball.ycor()<-280 or ball.ycor()>280:
        ball.bounce_y()

#TODO 5:Detect collision with paddle
    #the ball will collide and bounce in x direction
    if ball.distance(r_paddle)<50 and ball.xcor()>340:
        ball.bounce_x()
    if ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_x()
#TODO 6: DETECT WHEN THE PADDLE MISSES
    #when right paddle misses
    if ball.distance(r_paddle)>50 and ball.xcor()>370:
        ball.reset()
        score.l_update()
    if ball.distance(l_paddle)>50 and ball.xcor()<-370:
        ball.reset()
        score.r_update()

screen.exitonclick()
