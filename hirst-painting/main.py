import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

tim.setheading(225)
tim.penup()
tim.forward(250)
tim.penup()
tim.setheading(0)

tim.hideturtle()
for j in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
# from turtle import Turtle, Screen
# import random
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#
#     color_tuple = (red, green, blue)
#     rgb_colors.append(color_tuple)
#
#     #rgb_colors.append(color.rgb)
# print(rgb_colors)

# extracted colors from color_list

# first_color = colors[0]
# rgb = first_color.rgb

#print(rgb)

# tim = Turtle()
# tim.shape("circle")
# turtle.colormode(255)
# # tim.home()
# TURTLE_SIZE = 20
#
# screen = Screen()
#
# tim = Turtle(shape="circle", visible=False)
# tim.penup()
# tim.goto(TURTLE_SIZE/2 - screen.window_width()/3, screen.window_height()/2 - TURTLE_SIZE)
# tim.pendown()
# tim.showturtle()
#
# # screen.mainloop()
# for j in range(10):
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
#     rand_color = random.choice(color_list)
#     tim.color(rand_color, rand_color)
#     tim.begin_fill()
#     tim.circle(10)
#     tim.end_fill()
# tim.penup()
# tim.forward(50)
# tim.pendown()
# # for i in range(10):
# #     for j in range(10):
# #         tim.penup()
# #         tim.forward(50)
# #         tim.pendown()
# #         rand_color = random.choice(color_list)
# #         tim.color(rand_color, rand_color)
# #         tim.begin_fill()
# #         tim.circle(10)
# #         tim.end_fill()
# #         # tim.forward(20)
# #
# #     tim.right(90)
# #
# #     tim.forward(50)
#
# # screen = Screen()
# screen.exitonclick()