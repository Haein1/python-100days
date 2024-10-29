import pandas
import turtle

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


#get the x,y coordinates from turtle by clicking the mouse
# def get_x_y(x, y):
#     print(x, y)
# screen.onscreenclick(get_x_y)

#!TODO 1-convert png to gif, get x,y coordinates from tutle by clicking-DONE
#!TODO 2-make the pop window--DONE

FONT = ('Arial', 8, 'normal')

screen = turtle.Screen()
img = "try_fruit.gif"
screen.addshape(img)
turtle.shape(img)

score = 0
tim = turtle.Turtle()
tim.hideturtle()

fruit_data = pandas.read_csv("fruit_x_y.csv")
# print(fruit_data)
fruit_type_list = fruit_data.fruit.to_list()
# print(fruit_type_list)

is_game_on = True

while is_game_on:

    fruit_input = screen.textinput(title=f"{score}/4. Guess fruit", prompt="identify fruit?")
    #print(fruit_input)
    if fruit_input in fruit_type_list:
        score += 1
        specific_fruit_row = fruit_data[fruit_data.fruit == fruit_input]
        # print(specific_fruit_row)
        # print(type(specific_fruit_row))#<class 'pandas.core.frame.DataFrame'>

        specific_fruit_x = specific_fruit_row.x.to_list()[0]
        specific_fruit_y = specific_fruit_row.y.to_list()[0]
        # print(specific_fruit_x)
        # print(type(specific_fruit_x))
        # print(specific_fruit_x)
        # print(specific_fruit_y)

        tim.penup()
        tim.goto(specific_fruit_x,specific_fruit_y)
        tim.write(f"{fruit_input}", align="center", font=FONT)
    elif fruit_input == None:
        is_game_on = False
screen.mainloop()
# screen.exitonclick()
