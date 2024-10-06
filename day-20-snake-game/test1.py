import turtle

# Create turtle object
t = turtle.Turtle()

# Update the screen every 10th action
turtle.tracer(10, 100)

# Draw a star
for i in range(50):
    t.forward(200)
    t.right(144)

# Keeps the window open
turtle.done()
