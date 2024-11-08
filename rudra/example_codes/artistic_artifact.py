import turtle

# Initialize Turtle
screen = turtle.Screen()
screen.bgcolor("white")
artist = turtle.Turtle()
artist.speed(10)

# Define colors and variables
colors = ["red", "blue", "green", "purple", "orange"]
angle = 36  # Angle to rotate after each circle
radius = 50

# Draw spiral flower
for i in range(36):  # Loop to draw 36 circles in a pattern
    artist.color(colors[i % len(colors)])  # Cycle through colors
    artist.circle(radius)  # Draw a circle
    artist.right(angle)  # Rotate turtle
    radius += 2  # Increase the radius gradually

turtle.done()
