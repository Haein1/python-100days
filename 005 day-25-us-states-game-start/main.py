import turtle
import pandas

FONT = ('Arial', 8, 'normal')

score = 0
screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)
tim = turtle.Turtle()
tim.hideturtle()

# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
# print(answer_state)


# data['x'] = data['x'].astype(int)
# data['y'] = data['y'].astype(int)

data = pandas.read_csv("50_states.csv")

is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{score}/50  Guess the State", prompt="What's another state's name?")
    # print(answer_state)
    if answer_state in data.state.to_list():
        score += 1
        #print("yes")
        answer_state_row = data[data.state == answer_state]
        #print(type(data.state == answer_state))
        # print(answer_state_row)
        # print(answer_state_row.x)
        # print(type(answer_state_row.x))
        # print(answer_state_row.x.to_list()[0])
        answer_state_x = answer_state_row.x.to_list()[0]
        answer_state_y = answer_state_row.y.to_list()[0]
        # answer_state_x = answer_state_row.x[1]
        # answer_state_y = answer_state_row.y[1]
        # print(answer_state_row.x)
        # print(answer_state_x)
        # print(type(answer_state_x))
        # print(answer_state_y)
        # print(type(answer_state_y))
        tim.penup()
        tim.goto(answer_state_x, answer_state_y)
        tim.write(answer_state, align="center", font=FONT)
    elif answer_state == None:
        is_game_on = False
        # print("no")
        # answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
        # print(answer_state)
#print(data)



# search key words on Google "get x y coordinates on click python turtle"

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop() # let the window exist even though we click on the window for coordinates


screen.exitonclick()