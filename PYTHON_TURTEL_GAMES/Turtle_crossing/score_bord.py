from  turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.level = 1
        self.color("white")
        self.goto(-250, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}", move=False, align="center", font=("Arial", 15, "bold"))

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER!", move=False, align="center", font=("Arial", 15, "bold"))