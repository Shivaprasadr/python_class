import turtle

# Set up the screen with larger dimensions
screen = turtle.Screen()
screen.setup(width=800, height=800)  # Increase the screen size
screen.title("Enlarged Turtle Graphics")

# Set up the turtle
t = turtle.Turtle()
t.speed(2)  # Optional: Set a slower speed to observe the drawing
t.penup()
t.goto(-150, -150)  # Move starting position to the left side
t.pendown()

# Draw the first shape (circle-like rounded edges)
t.pencolor("black")
t.pensize(5)  # Increase pen size for thicker lines
t.begin_fill()
for _ in range(4):
    t.right(90)
    t.circle(150, 180)  # Increase the arc length
    t.fillcolor("blue")
t.end_fill()  # End the filling of the first shape

# Draw a larger square
t.penup()
t.goto(-150, -150)  # Adjust position for centering the square
t.pendown()
t.begin_fill()
t.pencolor("black")
t.pensize(5)
for _ in range(4):
    t.forward(300)  # Increase the square size
    t.left(90)
    t.fillcolor("white")
t.end_fill()

# Draw the smaller inner circle pattern
t.penup()
t.goto(0, 0)  # Center position for circles
t.pendown()

t.begin_fill()
radius = 70  # Increase radius of the inner circles
angle = 45
t.fillcolor("red")
for _ in range(8):
    t.circle(radius)
    t.left(angle)
t.end_fill()

t.begin_fill()
radius = 55  # Increase radius of the second inner circle layer
t.fillcolor("blue")
for _ in range(8):
    t.circle(radius)
    t.left(angle)
t.end_fill()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
