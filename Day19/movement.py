
def move_forwards(t):  # 't'is parameter of Turtle
    t.forward(10)

def move_backwards(t):
    t.backward(10)

def move_turn_left(t):
    t.left(10)

def move_turn_right(t):
    t.right(10)

def clear_screen(t):  
    t.clear()
    t.penup()
    t.home()
    t.pendown()

def listen_active(s):
    s.listen() # method to listen to the event

def screen_onkey(s):
    s.onkey(move_forwards, "w") #binding to w 
    s.onkey(move_backwards, "s") #binding to s 
    s.onkey(move_turn_left, "a") #binding to a 
    s.onkey(move_turn_right, "d") #binding to d 




