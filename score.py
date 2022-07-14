from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()

        self.present_score()

    def present_score(self):
        self.goto(-225, 265)
        self.write(f"LEVEL:{self.level}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.present_score()

    def game_over(self):
        self.clear()
        self.goto(0,  0)
        self.write(f"Game OVER \n    level: {self.level}", align=ALIGNMENT, font=FONT)

    def reset_level(self):
        self.clear()
        self.level = 1
        self.present_score()
