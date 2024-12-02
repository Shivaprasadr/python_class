import turtle
import random
import math

# Setup turtle screen
screen = turtle.Screen()
screen.title("Turtle Shortest Path")
screen.setup(width=600, height=600)

# Create the turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(1)

# Generate a random cursor position
target_x = random.randint(-300, 300)
target_y = random.randint(-300, 300)

# Draw the target position
target_marker = turtle.Turtle()
target_marker.penup()
target_marker.goto(target_x, target_y)
target_marker.shape("circle")
target_marker.color("red")
target_marker.write(f"({target_x}, {target_y})", align="left", font=("Arial", 12, "normal"))
target_marker.hideturtle()

# Function to move turtle to the target
def move_turtle_to_target(turtle, target_x, target_y):
    # Get current position of the turtle
    current_x, current_y = turtle.pos()

    # Calculate the angle to the target
    angle = math.degrees(math.atan2(target_y - current_y, target_x - current_x))

    # Set the turtle's heading towards the target
    turtle.setheading(angle)

    # Calculate the distance to the target
    distance = math.sqrt((target_x - current_x)**2 + (target_y - current_y)**2)

    # Move the turtle forward by the calculated distance
    turtle.forward(distance)

# Move the turtle to the target
move_turtle_to_target(my_turtle, target_x, target_y)

# Finish
turtle.done()
