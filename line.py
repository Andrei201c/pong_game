from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -250)
        self.pendown()
        self.pensize(7)
        self.pencolor('white')
        self.color('white')
        self.left(90)
        self.forward(550)
