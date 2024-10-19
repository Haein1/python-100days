from turtle import Turtle

LEVEL = 1
FONTS = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.game_level = LEVEL
        self.write(f"Level: {self.game_level}", align="center", font=FONTS)

    def update_level(self):
        self.game_level += 1
        self.clear()
        self.write(f"Level: {self.game_level}", align="center", font=FONTS)

