from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

speed = 0.06
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_of_wall()

    for segment in right_paddle.paddle:
        if segment.distance(ball) < 25 and ball.xcor() <= 345:
            ball.bounce_of_paddle()
            speed *= 0.9

    for segment in left_paddle.paddle:
        if segment.distance(ball) < 25 and ball.xcor() >= -345:
            ball.bounce_of_paddle()
            speed *= 0.9

    if ball.xcor() > 400:
        ball.reset()
        scoreboard.left_score_value += 1
        scoreboard.refresh_score(scoreboard.left_score_text, scoreboard.left_score_value)
        speed = 0.06

    if ball.xcor() < -400:
        ball.reset()
        scoreboard.right_score_value += 1
        scoreboard.refresh_score(scoreboard.right_score_text, scoreboard.right_score_value)
        speed = 0.06


screen.exitonclick()
