import turtle
import random

# Initialize Turtle and screen
screen = turtle.Screen()
screen.bgcolor("black")
artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing speed

# Define colors and parameters
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
line_length = 100
angle = 10  # Rotation angle for each line

# Draw the starburst pattern
for i in range(36):  # Loop to draw 36 lines in a circular pattern
    artist.color(colors[i % len(colors)])  # Cycle through colors
    artist.forward(line_length)  # Draw the line
    artist.backward(line_length)  # Move back to the center
    artist.right(angle)  # Rotate for the next line

# Finish up
turtle.done()