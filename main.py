import random
import time
from turtle import Screen
from turtle_crossing.cars import Cars
from turtle_player import Player
from score import Level


# screen.onkey(key="Space", fun=restart_game)

speed = 0.1
new_game = True

while new_game:
    game_on = True
    screen = Screen()
    screen.clearscreen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()
    screen.colormode(255)

    level = Level()
    car = Cars()
    player = Player()

    screen.onkeypress(key="Up", fun=player.move)

    while game_on:

        car.create_car()
        car.move()

        for block in car.all_cars:
            if block.distance(player) < 20:
                game_on = False
                level.game_over()
                user_choice = screen.textinput(title="PLAY AGAIN?", prompt=" Y\ N").lower()
                if user_choice == "n":
                    screen.bye()
                elif user_choice == "y":
                    player.reset_position()
                    level.reset_level()

        if player.ycor() > 280:
            level.update_score()
            player.goto(0, player.y)
            speed -= 0.01
        screen.update()
        time.sleep(speed)


screen.exitonclick()
