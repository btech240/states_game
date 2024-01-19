import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# Load image into turtle
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
pen = turtle.Turtle()

states = pd.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        pen.hideturtle()
        pen.penup()
        state_data = states[states.state == answer_state]
        pen.goto(int(state_data.x), int(state_data.y))
        pen.write(answer_state)


screen.exitonclick()
