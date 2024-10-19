from turtle import Turtle
import random

CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
DISTANCE = 10


class Car_manager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create_car()
        self.car_speed = DISTANCE


    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(CAR_COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            y_random = random.randint(-280, 280)
            new_car.penup()
            new_car.goto(280, y_random)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += DISTANCE