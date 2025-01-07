import turtle as trtl
import random as rand

# ----- Game Configuration -----
font_setup = ("Arial", 20, "normal")
timer = 25
counter_interval = 1000  # 1 second
timer_up = False
score_yellow = 0  # Initialize yellow ball score
score_blue = 0  # Initialize blue dot score
steps = 0  # Initialize the step counter
grid_size = 10  # Number of cells on the grid (10x10 grid)
cell_size = 50  # Size of each grid cell (in pixels)

# ----- Initialize Screen and Turtles -----
wn = trtl.Screen()
counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(300, 300)

# Main turtle (player)
t = trtl.Turtle()
t.shape("turtle")
t.speed("fastest")
t.penup()
t.shapesize(2, 2)

# Yellow circle (target)
yellow_circle = trtl.Turtle()
yellow_circle.shape("circle")
yellow_circle.color("Gold")
yellow_circle.penup()
yellow_circle.shapesize(2.5, 2.5)

# Score display turtle
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-300, 300)
score_writer.hideturtle()

# List of dots
dots = []

# ----- Helper Functions -----
def create_dots():
    """Places blue dots evenly on the grid."""
    for i in range(-grid_size // 2, grid_size // 2 + 1):
        for j in range(-grid_size // 2, grid_size // 2 + 1):
            dot = trtl.Turtle()
            dot.shape("circle")
            dot.color("blue")
            dot.speed(0)
            dot.penup()
            dot.shapesize(0.8, 0.8)
            dot.goto(i * cell_size, j * cell_size)
            dots.append(dot)
    countdown()

def respawn_dot(dot):
    """Respawns a dot after 5 seconds."""
    wn.ontimer(lambda: dot.showturtle(), 5000)

def check_dot_collision():
    """Checks if the turtle collects a dot."""
    global score_blue
    for dot in dots:
        if dot.isvisible() and t.distance(dot) < 20:
            dot.hideturtle()
            score_blue += 1
            update_score()
            respawn_dot(dot)
            break

def move_yellow_circle():
    """Moves the yellow circle randomly on the grid."""
    if not timer_up:
        x = rand.randint(-grid_size // 2, grid_size // 2) * cell_size
        y = rand.randint(-grid_size // 2, grid_size // 2) * cell_size
        yellow_circle.goto(x, y)
        wn.ontimer(move_yellow_circle, 2000)

def update_score():
    """Updates the score display."""
    score_writer.clear()
    score_writer.write(f"Yellow: {score_yellow}  Blue: {score_blue}", font=font_setup)

def update_steps():
    """Increments the step counter."""
    global steps
    steps += 1

def countdown():
    """Handles the countdown timer."""
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup, align="center")
        timer_up = True
        end_game()
    else:
        counter.write(f"Timer: {timer}", font=font_setup, align="center")
        timer -= 1
        wn.ontimer(countdown, counter_interval)

def move_up():
    if not timer_up:
        new_y = t.ycor() + cell_size
        if new_y <= (grid_size // 2) * cell_size:
            t.setheading(90)
            t.sety(new_y)
            check_collision()
            check_dot_collision()
            update_steps()

def move_down():
    if not timer_up:
        new_y = t.ycor() - cell_size
        if new_y >= (-grid_size // 2) * cell_size:
            t.setheading(270)
            t.sety(new_y)
            check_collision()
            check_dot_collision()
            update_steps()

def move_left():
    if not timer_up:
        new_x = t.xcor() - cell_size
        if new_x >= (-grid_size // 2) * cell_size:
            t.setheading(180)
            t.setx(new_x)
            check_collision()
            check_dot_collision()
            update_steps()

def move_right():
    if not timer_up:
        new_x = t.xcor() + cell_size
        if new_x <= (grid_size // 2) * cell_size:
            t.setheading(0)
            t.setx(new_x)
            check_collision()
            check_dot_collision()
            update_steps()

def check_collision():
    """Checks if the turtle touches the yellow circle."""
    global score_yellow
    if t.distance(yellow_circle) < 30:
        score_yellow += 1
        update_score()

def end_game():
    """Displays the final score and a message."""
    t.hideturtle()
    yellow_circle.hideturtle()
    for dot in dots:
        dot.hideturtle()
    message = trtl.Turtle()
    message.hideturtle()
    message.penup()
    message.goto(0, 100)
    message.write(f"Yellow: {score_yellow}  Blue: {score_blue}", font=("Arial", 30, "normal"), align="center")

# ----- Events and Screen Setup -----
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Initialize game elements
create_dots()
move_yellow_circle()

wn.mainloop()
