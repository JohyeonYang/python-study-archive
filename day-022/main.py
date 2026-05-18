from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up,"Up") # Callback Function go_up
screen.onkey(right_paddle.go_down,"Down")

screen.onkey(left_paddle.go_up,"w") 
screen.onkey(left_paddle.go_down,"s")

game_is_on = True
while game_is_on :
    time.sleep(0.1) # slower 
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340 :
        ball.bounce_x() 

screen.exitonclick()