import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_bord import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle_Crossing")
screen.tracer(0)

# Initializing player
player = Player()

# Initializing car
cars = CarManager()

# Initializing Score
score = ScoreBoard()

screen.listen()
screen.onkey(player.move_player_up, "Up")
screen.onkey(player.move_player_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Randomly creates cars
    cars.create_cars()
    cars.move_cars()

    # Returns the turtle to home position when player reaches top
    if player.ycor() > 280:
        player.return_player()
        cars.increase_speed()
        score.level_up()

    # Detect collision with car:
    for car in cars.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()
