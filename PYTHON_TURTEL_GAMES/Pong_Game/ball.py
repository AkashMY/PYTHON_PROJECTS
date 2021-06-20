import random
from turtle import Turtle
# SCEEN_EDGE_RIGHT = 400
# SCEEN_EDGE_UP = 400
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        # self.shapesize(stretch_wi, stretch_len=0.5)
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_Y(self):
        self.y_move *= -1

    def bounce_ball_X(self):
        self.x_move *= -1

