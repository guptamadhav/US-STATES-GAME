import turtle
from turtle import Turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
correct_ans = []
while len(correct_ans) < 50:
    state = screen.textinput(title=f"{correct_ans}/50 Guess the state", prompt="What's the another state").title()
    add_state = data[data["state"] == state]
    state_list = data.state.to_list()
    if state == "Exit":
        missing_state = [state for state in state_list if state not in correct_ans]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if state in state_list:
        correct_ans.append(state)
        i = Turtle()
        i.color("black")
        i.pu()
        i.hideturtle()
        new_x = int(add_state.x)
        new_y = int(add_state.y)
        i.goto(new_x, new_y)
        i.write(f"{state}", align="center", font=("Aerial", 10, "normal"))

screen.exitonclick()
