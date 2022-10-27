from turtle import Turtle

MOVE_DISTANCE = 14


class DashBoard:
    def __init__(self):
        self.middle = Turtle()
        self.middle.hideturtle()
        self.middle.color("white")
        self.middle.penup()
        self.middle.goto(0, -315)
        self.middle.left(90)
        for i in range(18):
            self.middle.pendown()
            self.middle.pensize(5)
            self.middle.forward(20)
            self.middle.penup()
            self.middle.forward(15)



