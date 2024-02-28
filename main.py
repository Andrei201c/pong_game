from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from line import Line
from score import Score
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(900, 500)
screen.title("PONG GAME")
screen.tracer(0)

line = Line()

score_bot = Score((60, 180))
score_player = Score((-60, 180))


paddle_left = Paddle((-430, 0))
paddle_right = Paddle((420, 0))

ball = Ball()

screen.listen()
time.sleep(0.01)
screen.onkeypress(paddle_left.movement_paddle_up, 'w')
screen.onkeypress(paddle_left.movement_paddle_down, "s")
screen.onkeypress(paddle_right.movement_paddle_up, 'Up')
screen.onkeypress(paddle_right.movement_paddle_down, "Down")


keep = True
while keep:
    if score_bot.score_bot <= 5 or score_player.score_player <= 5:
        time.sleep(0.04)
    elif score_bot.score_bot <= 10 or score_player.score_player <= 10:
        time.sleep(0.01)
    elif score_bot.score_bot <= 15 or score_player.score_player <= 15:
        time.sleep(0.03)
    else:
        time.sleep(0.01)

    screen.update()
    ball.move()

    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()

    if ball.distance(paddle_right) < 40 and ball.xcor() > 400 or ball.distance(paddle_left) < 40 and ball.xcor() < -410:
        ball.bounce_x()

    if ball.xcor() > 450:
        ball.reset_position()
        score_player.player_score_increase()
    elif ball.xcor() < -450:
        ball.reset_position()
        score_bot.bot_score_increase()

    if score_bot.score_bot == 20:
        screen.clear()
        screen.bgcolor("Red")
        score_bot.bot_win()
        keep = False
    elif score_player.score_player == 20:
        screen.clear()
        screen.bgcolor("Green")
        score_player.player_win()
        keep = False

screen.exitonclick()
