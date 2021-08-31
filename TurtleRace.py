from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 500)
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_position = [-50, -25, 0, 25, 50, 75]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")
turtles = []


def winning_text():
    write_turtle = Screen()
    write_turtle.bgcolor("black")
    write_turtle.setup(500,500)
    write_turtle.title(f"You've won! The {winning_color} turtle is the winning turtle!")


def losing_text():
    write_turtle = Screen()
    write_turtle.bgcolor("black")
    write_turtle.setup(500,500)
    write_turtle.title(f"You've lost! The {winning_color} turtle is the winning turtle!")



for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_position[turtle_index])
    turtles.append(new_turtle)


if user_bet:
    race_is_on = True


while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                winning_text()
                # turtle.write(f"You've won! The {winning_color} turtle is the winning turtle!")
            else:
                losing_text()
                # turtle.write(f"You've lost! The {winning_color} turtle is the winning turtle!")

        turtle_distance = random.randint(5,20)
        turtle.forward(turtle_distance)



screen.exitonclick()
