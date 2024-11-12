import turtle

# Set up the screen dimensions and title
screen = turtle.Screen()
screen.setup(width=800, height=800)  # Set the screen size
screen.title("Enlarged Turtle Graphics")

# Set up the turtle
t = turtle.Turtle()
t.speed(2)  # Set drawing speed to observe the process
t.penup()
t.goto(-150, -150)  # Move turtle to starting position on the left side
t.pendown()

# Draw the first shape with rounded corners
t.pencolor("black")
t.pensize(5)  # Set pen thickness for bold lines
t.fillcolor("blue")  # Set fill color to blue
t.begin_fill()
for _ in range(4):
    t.right(90)  # Rotate 90 degrees to draw each side of the rounded square
    t.circle(150, 180)  # Draw a 180-degree arc with a radius of 150 units
t.end_fill()  # Complete and fill the shape

# Draw a larger square inside the rounded shape
t.penup()
t.goto(-150, -150)  # Move turtle to bottom-left corner of the square
t.pendown()
t.begin_fill()
t.fillcolor("white")  # Set fill color to white
for _ in range(4):
    t.forward(300)  # Draw each side of the square, 300 units long
    t.left(90)  # Turn 90 degrees left to draw the next side
t.end_fill()

# Draw an inner circle pattern centered at (0, 0)
t.penup()
t.goto(0, 0)  # Move turtle to the center of the screen
t.pendown()

# Draw the first layer of circles
t.fillcolor("red")  # Set fill color for the first circle layer
t.begin_fill()
radius = 70  # Set radius for the first inner circle layer
angle = 45  # Set the angle of rotation between each circle
for _ in range(8):
    t.circle(radius)  # Draw a circle with the specified radius
    t.left(angle)  # Rotate left by 45 degrees to draw the next circle
t.end_fill()

# Draw the second layer of circles
t.fillcolor("blue")  # Set fill color for the second circle layer
t.begin_fill()
radius = 55  # Set radius for the second inner circle layer
for _ in range(8):
    t.circle(radius)  # Draw a circle with the specified radius
    t.left(angle)  # Rotate left by 45 degrees to draw the next circle
t.end_fill()

# Hide the turtle to finish the drawing
t.hideturtle()
turtle.done()
