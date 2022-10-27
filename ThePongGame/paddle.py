from turtle import Turtle

MOVE_DISTANCE = 14


class Player(Turtle):
    def __init__(self, player_number):
        super().__init__()
        self.player = player_number
        self.create_paddle()
        self.setheading(90)

    def create_paddle(self):
        """create a new paddle"""
        self.shapesize(0.7, 3)
        self.penup()
        self.color("white")
        self.shape("square")
        if self.player == 1:
            self.goto(-450, 0)
        elif self.player == 2:
            self.goto(450, 0)

    def up(self):
        new_y = self.ycor() + 14
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 14
        self.goto(self.xcor(), new_y)

    def automatic_move(self):
        if self.ycor() > 270:
            self.setheading(270)
            self.forward(MOVE_DISTANCE)
        elif self.ycor() < -270:
            self.setheading(90)
            self.forward(MOVE_DISTANCE)
        else:
            self.forward(MOVE_DISTANCE)