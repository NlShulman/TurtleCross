import random
import time
from turtle import Screen
from turtle_crossing.cars import Cars
from turtle_player import Player
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.colormode(255)

score = Score()
player = Player()
car = Cars()

screen.onkeypress(key="Up", fun=player.move)
# screen.onkey(key="Space", fun=restart_game)

speed = 0.1
game_on = True


while game_on:
    car.create_car()
    car.move()

    for block in car.all_cars:
        if block.distance(player) < 20:
            game_on = False
            score.game_over()

    if player.ycor() > 280:
        score.update_score()
        player.goto(0, player.y)
        speed -= 0.01
    screen.update()
    time.sleep(speed)


screen.exitonclick()