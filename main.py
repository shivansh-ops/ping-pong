from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
l_paddle = Paddle(position=(-350, 0))
r_paddle = Paddle(position=(350, 0))
ball = Ball()
score = Score()
screen.listen()

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 340:
        ball.reset_ball()
        score.l_point()

    if ball.xcor() < -340:
        ball.reset_ball()
        score.r_point()
screen.exitonclick()
