from turtle import Turtle
ALIGN = "Center"
FONT = ('Verdana', 40, "bold")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score_bot = 0
        self.score_player = 0
        self.color('yellow')
        self.penup()
        self.goto(position)
        self.update_score_bot()
        self.update_score_player()
        self.hideturtle()

    def update_score_bot(self):
        self.write(f"{self.score_bot}", align=ALIGN, font=FONT)

    def update_score_player(self):
        self.write(f"{self.score_player}", align=ALIGN, font=FONT)

    def bot_win(self):
        self.goto(0, 0)
        self.clear()
        self.write("BOT WIN", align=ALIGN, font=FONT)

    def player_win(self):
        self.goto(0, 0)
        self.clear()
        self.write("PLAYER WIN", align=ALIGN, font=FONT)

    def player_score_increase(self):
        self.score_player += 1
        self.clear()
        self.update_score_player()

    def bot_score_increase(self):
        self.score_bot += 1
        self.clear()
        self.update_score_bot()