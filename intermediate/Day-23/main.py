import time
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager=CarManager()
screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Turtle Cross")

#TODO 1:MOVE THE TURTle WITH THE KEYPRESS
screen.listen()       #to pass the onkey function
screen.onkey(player.go_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #TODO 3 :DETECT COLLISION WITH THE CAR
    for car in car_manager.all_cars:
        if car.distance(player)<20:      #to check the distance between car and the player
            game_is_on = False
            scoreboard.game_over()
    #TODO 4:DETECT THAT THE TURTLE HAS COMPLETED THE RACE
        if player.game_finish:
            player.back_to_start()
            car_manager.level_up()
            scoreboard.increase_score()


screen.exitonclick()
