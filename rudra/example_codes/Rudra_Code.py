import turtle

# Set up the screen
screen = turtle.Screen()

# Set up the turtle
t = turtle.Turtle()
xcor = 100
if xcor == 100:
    t.pencolor("black")
    t.pensize(3)
    # Draw the first shape (circle) with fill color
    t.begin_fill()
    for circle in range(4):
        t.right(90)
        t.circle(xcor, 190)
        t.fillcolor("blue")
    t.end_fill()  # End the filling of the circle
    
    # Draw the square
    t.begin_fill()
    t.pencolor("black")
    t.pensize(3)
    for square in range(4):
        t.forward(180)
        t.left(90)
        t.fillcolor("white")
    t.end_fill()
    t.penup()
    t.goto(90,90)
    t.pendown()
    
    t.begin_fill()
    radius = 45
    angle = 45
    for circle in range (8):
        t.circle(radius)
        t.left(angle)
        t.fillcolor("red")
    t.end_fill()

    t.begin_fill()
    radius = 36
    angle = 45
    for circle in range (8):
        t.circle(radius)
        t.left(angle)
        t.fillcolor("blue")
    t.end_fill()

     

   




# Hide the turtle and display the window

turtle.done()