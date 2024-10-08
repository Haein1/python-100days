from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
# from scoreboard import Scoreboard
from scoreboard import Scoreboard
import time


R_PADDLE_POSITION = (350, 0)
L_PADDLE_POSITION = (-350, 0)

#create the screen
screen = Screen()
screen.bgcolor("black")
#screen.screensize(canvwidth=800, canvheight=600)
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


#make a paddle in the background
#create the paddle
r_paddle = Paddle(R_PADDLE_POSITION)
l_paddle = Paddle(L_PADDLE_POSITION)
#create the ball and make it move
ball = Ball()
scoreboard = Scoreboard()

# paddle = Turtle()
# #paddle.hideturtle()
# paddle.shape("square")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.color("white")
# paddle.penup()
# paddle.goto(350, 0)
# #paddle.showturtle()
#
# #move the paddle
# def go_up():
#     new_y = paddle.ycor()+20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor()-20
#     paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")


#my code
# paddle_position = [(350, 0), (350, 20), (350, 40), (350, -20), (350, -40)]
# paddle_segments = []
#
# for position in paddle_position:
#     segment = Turtle()
#     segment.shape("square")
#     segment.color("white")
#     segment.penup()
#     segment.goto(position[0], position[1])
#     paddle_segments.append(segment)





is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()  # show everything that happened in the background so far
    ball.move()
    # break
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #detect when r_paddle misses the ball
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    #detect when l_paddle misses the ball
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()