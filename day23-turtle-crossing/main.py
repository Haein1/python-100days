from turtle import Turtle, Screen
import time
from player import Player
from car_manager import Car_manager
from scoreboard import Scoreboard

'''
To do structure:
1: move the turtle with keypress  -DONE
2: create and move the cars  --DONE
3: Detect collision with car --DONE
4: Detect when turtle reaches the other side--DONE
5: Create a scoreboard --DONE
'''

#TODO 1: move the turtle with keypress  -DONE
#TODO 2: create and move the cars  --DONE



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = Car_manager()
#TODO 5: Create a scoreboard --DONE
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # TODO 3: Detect collision with car --DONE
    for car in car_manager.cars:
        if player.distance(car) < 20:
            player.game_over()
            is_game_on = False

    # TODO 4: Detect when turtle reaches the other side--DONE
    if player.ycor() > 280:
        player.update_pos()
        scoreboard.update_level()
        car_manager.level_up()



screen.exitonclick()