import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.addshape('img/leonardo.gif')
screen.addshape('img/suv.gif')

player1 = Player()
car = CarManager()
screen.onkeypress(fun=player1.walk, key="Up")
score = Scoreboard()

game_is_on = True
score.level_up(1)
while game_is_on:

    car.move()
    if car.coliision(player1.pos()):
        score.lose()
        game_is_on = False

    if player1.ycor() > 280:
        player1.set_center()
        score.level_up(1)
    time.sleep(0.1)
    screen.update()

screen.exitonclick()