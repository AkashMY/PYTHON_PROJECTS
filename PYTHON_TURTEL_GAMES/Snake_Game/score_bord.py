from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Blue")
        self.pu()
        with open("data.txt") as data:
            high_score = data.read()
            self.high_score = int(high_score)
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def Game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nYour Score is: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_high_score(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as data:
                data.write(f"{self.score}")
