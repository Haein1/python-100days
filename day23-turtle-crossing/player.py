from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
GAME_OVER_FONTS = ('Arial', 20, 'normal')


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game over", align="center", font=GAME_OVER_FONTS)

    def update_pos(self):
        self.penup()
        self.goto(STARTING_POSITION)