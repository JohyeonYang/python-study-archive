from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer() #hiding the process

snake = Snake()

screen.listen() #screen reacting by input
screen.onkey(snake.up, "Up") #screen.onkey(binded method,"Keyname")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

game_is_on =True
while game_is_on :
    screen.update() #show the result
    time.sleep(0.1) #0.1sec delay
    snake.move()


screen.exitonclick()