from turtle import Screen
from paddle import Player
from ball import Ball
from scoreboard import ScoreBoard
from dashboard import DashBoard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)


dashboard = DashBoard()
scoreboard1 = ScoreBoard(1)
scoreboard2 = ScoreBoard(2)
player1 = Player(1)
player2 = Player(2)
ball = Ball()

screen.listen()
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")

game_is_on = True
player_2 = True


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    if player_2:
        screen.onkeypress(player2.up, "w")
        screen.onkeypress(player2.down, "s")
    else:
        player2.automatic_move()
    ball.move()

    #Detect collision with the wall and bounce
    if ball.ycor() > 286 or ball.ycor() < -286:
        ball.wall_bounce()

    #Detect collision with the paddles
    if ball.distance(player2) < 40 and ball.xcor() > 430:
        ball.paddle_bounce()
    elif ball.distance(player1) < 40 and ball.xcor() < -430:
        ball.paddle_bounce()

    # Detect collision with wall
    if ball.xcor() > 490:
        ball.refresh()
        scoreboard1.increase()
    elif ball.xcor() < -490:
        ball.refresh()
        scoreboard2.increase()


screen.exitonclick()