from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.count = 0
        newcar = Turtle()
        newcar.pu()
        newcar.shape('img/suv.gif')
        y = random.randint(-230, 230)
        newcar.goto(-250,y)
        self.cars.append(newcar)

    def move(self):
        self.count += 1
        if self.count == 6:
            self.create_car()
            self.count = 0
        for i in range(0, len(self.cars)):
            self.cars[i].forward(STARTING_MOVE_DISTANCE)

    def create_car(self):
        newcar = Turtle()
        newcar.pu()
        newcar.shape('img/suv.gif')
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        newcar.goto(x, y)
        self.cars.append(newcar)

    def coliision(self,player_position):
        for i in range(0, len(self.cars)):
            if self.cars[i].distance(player_position) < 15:
                return True
