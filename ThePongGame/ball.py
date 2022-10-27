from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.75)
        self.color("white")
        self.x_move = 15
        self.y_move = 15
        self.random_start()
        self.move_speed = 0.12

    def random_start(self):
        start = [-1, 1]
        self.y_move *= random.choice(start)
        self.x_move *= random.choice(start)

    def move(self):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.14
        self.random_start()
