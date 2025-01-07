To enable the turtle to reach the cursor's position in the best possible way, we can use the **Pythagorean theorem** and **basic trigonometry**. The turtle module provides methods like `setheading()` and `forward()` that can be used to orient and move the turtle in the shortest path.

Here's how you can achieve this:

### **Logic**:
1. **Determine the direction**: Calculate the angle between the turtle's current position and the target cursor position.
2. **Orient the turtle**: Use `setheading()` to make the turtle face the target.
3. **Move towards the target**: Calculate the distance to the target using the Pythagorean theorem and move the turtle forward.

### **Python Code**:
```python
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
```

### **Explanation**:
1. **Random Target Generation**:
   - `random.randint(-300, 300)` generates a random position within the turtle screen bounds.

2. **Angle Calculation**:
   - `math.atan2()` calculates the angle between the current and target positions in radians.
   - `math.degrees()` converts this angle to degrees for use with `setheading()`.

3. **Distance Calculation**:
   - The distance is computed using the formula:
     \[
     \text{distance} = \sqrt{(\text{target}_x - \text{current}_x)^2 + (\text{target}_y - \text{current}_y)^2}
     \]

4. **Turtle Movement**:
   - `setheading(angle)` makes the turtle face the target.
   - `forward(distance)` moves the turtle to the target.

### **Result**:
- A red circle marks the target position.
- The turtle moves directly and efficiently to the target using the shortest path.

This approach ensures the turtle reaches the cursor's position in the optimal way.