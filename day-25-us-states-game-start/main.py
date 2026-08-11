import pandas

import turtle


#importing turtle

screen = turtle.Screen()
screen.setup(width=1500, height=900)
screen.title("Guess the district name of Nepal")
image = "nepal_map_blank.gif"
screen.bgpic(image)


data = pandas.read_csv("nepal_districts_turtle_xy.csv")
all_state = data.District.to_list()
guessed_district = []
#game engine

while len(guessed_district) < 77:
    answer_state = screen.textinput(title="Make a guess", prompt="Guess another").title()

    if answer_state in all_state:
        guessed_district.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district = data[data.District == answer_state]
        t.goto(district.X.item(), district.Y.item())
        t.write(answer_state)









turtle.done()
