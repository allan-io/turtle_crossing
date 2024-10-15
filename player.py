from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.y = -280
        self.goto(0, self.y)
        self.setheading(90)

    def move(self):
        self.y += 20
        self.goto(0, self.y)

    def level_up(self):
        self.y = -280
        self.goto(0, self.y)
