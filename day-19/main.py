from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a colour:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

# print(user_bet)

x_pos = -230
y_pos = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x_pos, y_pos)
    y_pos += 40

    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()


# def move_forwards():
#     tim.forward(20)
#
# def move_backwards():
#     tim.setheading(180)
#     tim.forward(20)
#
# def counter_clockwise():
#     tim.left(10)
#
# def clockwise():
#     tim.right(10)
#
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
#
# screen.onkey(key = "w", fun = move_forwards)
# screen.onkey(key = 's', fun = move_backwards)
# screen.onkey(key = 'a', fun = counter_clockwise)
# screen.onkey(key = 'd', fun = clockwise)
# screen.onkey(key = 'c', fun = clear_drawing)