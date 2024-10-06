# import turtle
#
# # Create turtle object
# t = turtle.Turtle()
#
# # Disable updates and speed up drawing
# turtle.tracer(0, 0)
#
# # Draw a large number of circles
# for i in range(100):
#     t.circle(50)
#     t.left(10)
#
# # Update the screen at the end of drawing
# turtle.update()
#
# # Keeps the window open
# turtle.done()

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water")
    def swim(self):
        print("moving in water")

nemo = Fish()
# nemo.swim()
nemo.breathe()