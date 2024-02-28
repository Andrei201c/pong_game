from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=0.5, stretch_wid=5)
        self.penup()
        self.color('lightgray')
        self.speed('fastest')
        self.goto(position)

    def movement_paddle_up(self):
        y_pos = self.ycor() + 10
        self.goto(self.xcor(), y_pos)

    def movement_paddle_down(self):
        y_pos = self.ycor() - 10
        self.goto(self.xcor(), y_pos)
