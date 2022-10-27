from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.game[0].distance(food) < 15:
        food.refresh()
        snake.grow_snake()
        score.increase()

    #Detect collision with wall
    if snake.game[0].xcor() > 295 or snake.game[0].xcor() < -295 or snake.game[0].ycor() > 295 or snake.game[0].ycor() < -295:
        again = screen.textinput("Game Over", prompt="Game over\nDo you want to play again? 'Yes' or 'No': ")
        if again == "Yes":
            score.game_over()
            snake.game_over()
            food.refresh()
        else:
            game_is_on = False

    #Detect collision with tail
    for segment in snake.game[1:]:
        if snake.game[0].distance(segment) < 10:
            again = screen.textinput("Game Over", prompt="Game over\nDo you want to play again? 'Yes' or 'No': ")
            if again == "Yes":
                score.game_over()
                snake.game_over()
                food.refresh()
            else:
                game_is_on = False

screen.exitonclick()