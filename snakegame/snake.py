from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.game = []
        self.create_snake()

    def create_snake(self):
        """create the starting snake"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """add a new segment to the snake"""
        new_part = Turtle()
        new_part.penup()
        new_part.color("silver")
        new_part.shape("square")
        new_part.goto(position)
        self.game.append(new_part)

    def grow_snake(self):
        self.add_segment(self.game[-1].position())

    def move(self):
        # for i in range(start=2 , stop= 0, step=-1)
        for n in range(len(self.game) - 1, 0, -1):
            new_x = self.game[n - 1].xcor()
            new_y = self.game[n - 1].ycor()
            self.game[n].goto(new_x, new_y)
        self.game[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.game[0].heading() != DOWN:
            self.game[0].setheading(UP)

    def down(self):
        if self.game[0].heading() != UP:
            self.game[0].setheading(DOWN)

    def left(self):
        if self.game[0].heading() != RIGHT:
            self.game[0].setheading(LEFT)

    def right(self):
        if self.game[0].heading() != LEFT:
            self.game[0].setheading(RIGHT)

    def game_over(self):
        for part in self.game:
            part.goto(-700, -700)
        self.game.clear()
        self.create_snake()