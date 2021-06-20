import time
from turtle import Screen
from ball import Ball
from slider import Slider
from score import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONGO")
screen.tracer(0)


# Initializing Sliders
r_slider = Slider((350, 0))
l_slider = Slider((-350, 0))

# Control the slider
screen.listen()
screen.onkey(r_slider.up, "Up")
screen.onkey(r_slider.down, "Down")
screen.onkey(l_slider.up, "w")
screen.onkey(l_slider.down, "s")

# Initializing ball
ball = Ball()

# Initializing score Board
score_board = ScoreBoard()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_Y()

    if ball.xcor() > 320 and ball.distance(r_slider) < 50 or ball.xcor() < -320 and ball.distance(l_slider) < 50:
        ball.bounce_ball_X()

    if ball.xcor() > 360:
        score_board.l_score += 1
        score_board.clear()
        score_board.l_score_board()
        score_board.r_score_board()
        ball.goto(0, 0)
        ball.bounce_ball_X()

    if ball.xcor() < -360:
        score_board.r_score += 1
        score_board.clear()
        score_board.r_score_board()
        score_board.l_score_board()
        ball.goto(0, 0)
        ball.bounce_ball_X()
    ball.move()

screen.exitonclick()
