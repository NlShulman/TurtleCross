from turtle import Turtle
import random

MOVE_DISTANCE = 10


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        if 1 == random.randint(0, 6):
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            random_y_pos = random.randint(-250, 250)
            new_car.goto(310, random_y_pos)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(MOVE_DISTANCE)
