from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.color("green")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_player_up(self):
        self.goto(0, self.ycor()+MOVE_DISTANCE)

    def move_player_down(self):
        self.goto(0, self.ycor()-MOVE_DISTANCE)

    def return_player(self):
        self.goto(STARTING_POSITION)

