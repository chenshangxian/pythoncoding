import turtle


myTurtle = turtle.Turtle()
myTurtle.speed(0)  
myTurtle.setheading(90)
def my_square(size):
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.right(270)

size = 10


for _ in range(100):
    my_square(size)
    size += 10  
    myTurtle.penup()  
    myTurtle.goto(0, 0) 
    myTurtle.pendown()  

turtle.done()