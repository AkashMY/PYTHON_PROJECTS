import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEEDS = [10, 15, 20, 25, 30]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager :
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_cars(self):
        random_number = random.randint(1,6)
        if random_number == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=0.8, stretch_len=2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            y = random.randint(-280,280)
            new_car.goto(350, y)
            new_car.setheading(180)
            self.all_cars.append(new_car)
            
    def move_cars(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT