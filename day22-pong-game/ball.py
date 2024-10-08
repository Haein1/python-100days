from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.x_pos = 0
        # self.y_pos = 0
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 # the logic of ball bouncing
    # def move_down(self):
    #     self.goto(self.xcor()+10, self.ycor()+10)
        # self.x_pos = 380
        # self.y_pos = 280
        # self.penup()
        # self.goto(self.x_pos, self.y_pos)
        # self.pendown()

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase_speed(self):
        self.speed += 1
        self.speed(self.speed)