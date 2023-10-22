from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.speed(0)
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(100, 260)
        self.clear()

    def level_up(self,point):
        self.level += point
        self.clear()
        self.write("Level: {}".format(self.level), align="Left", font=FONT)

    def lose(self):
        self.clear()
        self.write("GAME OVER", align="center", font=FONT)

    # def lose(self,level):
    #     self.clear()
    #     self.write("Level: {}".format(lelvel), align="center", font=FONT)
