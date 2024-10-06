from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        # self.pensize(20)
        self.penup()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def increase(self):
        self.pendown()
        self.showturtle()
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move= False, align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(arg="game over", move=False, align=ALIGNMENT, font=FONT)