from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.goto(100, 250)
        self.r_score_board()
        self.l_score_board()

    def r_score_board(self):
        self.goto(100, 250)
        self.write(f"{self.r_score}", move=False, align="center", font=("Arial", 35, "bold"))

    def l_score_board(self):
        self.goto(-100, 250)
        self.write(f"{self.l_score}", move=False, align="center", font=("Arial", 35, "bold"))
