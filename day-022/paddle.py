from turtle import Turtle

class Paddle (Turtle): # inherited from Turtle class
    def __init__(self, position) : #when we create the object
        super().__init__() # inherited

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) #relative size 1=20pix
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20 # from the current Ycoordinate +20
        self.goto(self.xcor(), new_y) # to new position


    def go_down(self):
        new_y = self.ycor() - 20 # from the current Ycoordinate +20
        self.goto(self.xcor(), new_y) # to new position