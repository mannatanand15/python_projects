from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#TODO 2: CREATE AND MOVE THE CARS
class CarManager:
    def __init__(self):
        self.all_cars = []   #empty list
        self.car_speed=STARTING_MOVE_DISTANCE
       # self.all_cars.speed = STARTING_MOVE_DISTANCE  (this is incorrect becoz speed attribute can't be assigned to a list)
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=2,stretch_len=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            new_car.penup()
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

