from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('img/leonardo.gif')
        self.goto(STARTING_POSITION)

    def walk(self):
        # if self.ycor() < FINISH_LINE_Y:
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)

    def set_center(self):
        self.goto(STARTING_POSITION)