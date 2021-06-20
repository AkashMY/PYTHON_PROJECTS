from turtle import Turtle
SCREEN_EDGE_DOWN = -240
SCREEN_EDGE_UP = 250


class Slider(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_slider()

    def create_slider(self):
        self.shape("square")
        self.pu()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(self.position)

    def up(self):
        if self.ycor() > SCREEN_EDGE_UP:
            pass
        elif self.ycor() < SCREEN_EDGE_UP:
            new_y = self.ycor() + 20
            self.sety(new_y)

    def down(self):
        if self.ycor() < SCREEN_EDGE_DOWN:
            pass
        elif self.ycor() > SCREEN_EDGE_DOWN:
            new_y = self.ycor() - 20
            self.sety(new_y)


