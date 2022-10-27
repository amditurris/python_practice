from turtle import Turtle
ALIGNMENT= "center"
FONT= ("Courier", "14","normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        #high_score track
        with open("score_file.txt") as file:
            self.high_score = int(file.read())
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Score: {self.score}. High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.scoreboard()

    def game_over(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_file.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write(f"Score: {self.score}. High score: {self.high_score}", align=ALIGNMENT, font=FONT)
