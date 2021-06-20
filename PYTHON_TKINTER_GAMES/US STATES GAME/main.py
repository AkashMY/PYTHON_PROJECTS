import pandas
from turtle import Turtle , Screen

screen = Screen()
screen.title("U.S. STATES GAME")
img = "blank_states_img.gif"
screen.addshape(img)

guessed_states = []
states_to_learn = []

tom = Turtle()
tom.shape(img)

while len(guessed_states) < 50:

    state = screen.textinput(title=f"{len(guessed_states)}/50 are correct", prompt="Enter the State name").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()

    if state == "Exit":
        break

    if state in all_states:
        guessed_states.append(state)
        tim = Turtle()
        tim.pu()
        tim.hideturtle()
        state_data = data[data.state == state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(f"{state}", False, "center", ("Arial", 5, "bold"))

    for states in all_states:
        if states not in guessed_states:
            states_to_learn.append(states)

    missing = pandas.DataFrame(states_to_learn)
    missing.to_csv("missing_states.csv")












# def to_get_XY(x,y):
#     print(x,y)
#
# screen.onscreenclick(to_get_XY)
# turtle.mainloop()





screen.exitonclick()
