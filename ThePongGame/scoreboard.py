from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", "70", "normal")
SCOREBOARD_ONE = (-75, 200)
SCOREBOARD_TWO = (75, 200)


class ScoreBoard(Turtle):
    def __init__(self, player_number):
        super().__init__()
        self.player = player_number
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.position()
        self.scoreboard()

    def position(self):
        if self.player == 1:
            self.goto(SCOREBOARD_ONE)
        elif self.player == 2:
            self.goto(SCOREBOARD_TWO)

    def scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.scoreboard()