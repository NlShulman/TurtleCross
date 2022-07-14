from turtle import Turtle

MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.setheading(90)
        self.y = -280
        self.reset_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(0, self.y)
