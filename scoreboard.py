from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier"
FONT_SIZE = 24
FONT_TYPE = 'normal'
FONT_COLOR = "white"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.pencolor(FONT_COLOR)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", font=(FONT, FONT_SIZE, FONT_TYPE), align=ALIGNMENT)

    def end_game(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=(FONT, FONT_SIZE, FONT_TYPE), align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.print_score()

