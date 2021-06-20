from turtle import Screen
import time
from snake import Snake
from food import Food
from playsound import playsound
from score_bord import ScoreBoard

# setting Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake_Game")
screen.tracer(0)

# creating_snakes
snake = Snake()

# Control snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initializing Food
food = Food()

# Initializing Score Display
score_board = ScoreBoard()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        playsound("beep.wav")
        score_board.increase_score()
        snake.extend()

    # Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score_board.update_high_score()
        game_is_on = False
        score_board.Game_over()

    # Detect collision with
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score_board.Game_over()


screen.exitonclick()
