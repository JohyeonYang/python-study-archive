from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0) #hiding the process

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() #screen reacting by input

screen.onkey(snake.up, "e") 
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on =True

while game_is_on :
    screen.update() #refreshing the screen
    time.sleep(0.7) #0.1sec delay
    snake.move()

    #Detect collision with food
    if snake.head.distance(food)<15 :
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()