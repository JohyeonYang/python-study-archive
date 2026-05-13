from turtle import Turtle, Screen
import movement
import random

is_race_on = False
screen = Screen() #create Screen Instance

screen.setup(width=500,height=400) #setting size
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win? Enter a color :")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles =[]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x =- 230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet : #once user inputs, race on
    is_race_on = True

while is_race_on:

    for turtle in all_turtles :
        
        if turtle.xcor() > 230 : #if x-coordinate of each turtle greater than 230
            is_race_on =False
            winning_color = turtle.pencolor()
            if user_bet == winning_color :
                print("You won!")
            else :
                print(f"{winning_color} won!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        
screen.exitonclick()
