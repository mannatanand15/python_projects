# SNAKE GAME PROJECT 
from turtle import Screen
#to delay the program
import time
from food import Food
from snake import Snake
from scoreboard import Scorecard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)    #turn the program on/off  {0 for off}
snake=Snake()
food=Food()
scoreboard=Scorecard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
score=Scorecard()
game_on=True
while game_on:
    screen.update()      #to turn on the program and it starts running then
    time.sleep(0.1)
    snake.move()

#TODO 4: DETECT COLLISION WITH FOOD BY USING DISTANCE METHOD

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
#TODO 5:DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()

