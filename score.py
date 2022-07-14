from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-220, 270)
        self.present_score()

    def present_score(self):
        self.write(f"LEVEL:{self.level}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.present_score()

    def game_over(self):
        self.clear()
        self.goto(0,  0)
        self.write(f"Game OVER \n    level: {self.level}", align=ALIGNMENT, font=FONT)