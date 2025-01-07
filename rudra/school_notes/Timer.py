import turtle as trtl
import random as rand




#-----game configuration-----
font_setup = ("Arial", 20, "normal")
timer = 25 
counter_interval = 1000  # 1 second
timer_up = False
score = 0  # Initialize the score
steps = 0  # Initialize the step counter
optimal_score = 75  # Optimal score to display a special message




# Grid configuration
grid_size = 10  # Number of cells on the grid (10x10 grid)
cell_size = 50  # The size of each grid cell (in pixels)




#-----initialize screen and turtles-----
wn = trtl.Screen()
counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(300, 300)




# Create the main turtle (player turtle)
t = trtl.Turtle()
t.shape("turtle")
t.speed("fastest")  # Increase movement speed
t.penup()  # Ensure the pen is up to avoid drawing a line
t.shapesize(2, 2)  # Adjust the size of the turtle




# Create the yellow circle (target turtle) with a black border
yellow_circle = trtl.Turtle()
yellow_circle.shape("circle")
yellow_circle.color("Gold")
yellow_circle.penup()
yellow_circle.shapesize(2.5, 2.5)  # Adjusted size of the yellow circle




yellow_circle_start_position = (0, 0)




# Create score display turtle
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-300, 300)  # Position the score display
score_writer.hideturtle()
score_writer.color("black")




# Dots configuration
dots = []
num_dots = grid_size * grid_size  # Total number of dots for a full grid




def create_dots():
    if timer >= 0:
     """Places dots evenly on the grid."""
     for i in range(-grid_size // 2, grid_size // 2 + 1):
            for j in range(-grid_size // 2, grid_size // 2 + 1):
                dot = trtl.Turtle()
                dot.shape("circle")
                dot.color("blue")
                dot.speed(0)
                dot.penup()
                dot.shapesize(0.8, 0.8)  # Smaller dots
                dot.goto(i * cell_size, j * cell_size)
                dots.append(dot)
    else:
        dot.clear()
    # Start the timer only after all dots are created
    countdown()




def respawn_dot(dot):
    """Respawns a dot immediately after 5 seconds."""
    wn.ontimer(lambda: dot.showturtle(), 5000)




def check_dot_collision():
    """Checks if the turtle touches any dots."""
    global score
    for dot in dots:
        if dot.isvisible() and t.distance(dot) < 20:  # Collision threshold
            dot.hideturtle()
            score += 1
            update_score()
            respawn_dot(dot)
            break




def move_yellow_circle_step():
    """Moves the yellow circle along the grid one cell at a time."""
    if not timer_up:
        current_x, current_y = yellow_circle.xcor(), yellow_circle.ycor()
        direction = rand.choice(["up", "down", "left", "right"])




        if direction == "up" and current_y + cell_size <= (grid_size // 2) * cell_size:
            yellow_circle.sety(current_y + cell_size)
        elif direction == "down" and current_y - cell_size >= (-grid_size // 2) * cell_size:
            yellow_circle.sety(current_y - cell_size)
        elif direction == "left" and current_x - cell_size >= (-grid_size // 2) * cell_size:
            yellow_circle.setx(current_x - cell_size)
        elif direction == "right" and current_x + cell_size <= (grid_size // 2) * cell_size:
            yellow_circle.setx(current_x + cell_size)




        wn.ontimer(move_yellow_circle_step, 300)  # Recursively call movement function




def update_score():
    """Updates the score on the screen."""
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=font_setup)




def update_steps():
    """Updates the step counter."""
    global steps
    steps += 1




#-----game functions-----
def countdown():
    """Handles the countdown timer."""
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup, align="center")
        timer_up = True
        clear_screen_after_timer()
        display_score_message()
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
    global score
    if t.distance(yellow_circle) < 30:  # Adjusted collision threshold
        score += 5  # Bonus points
        update_score()




        # Change the turtle color randomly each time it touches the yellow circle
        colors = ["silver","blue","brown","purple","green"]
        t.color(rand.choice(colors))




        yellow_circle.goto(rand.randint(-grid_size // 2, grid_size // 2) * cell_size,
                           rand.randint(-grid_size // 2, grid_size // 2) * cell_size)
        move_yellow_circle_step()  # Restart yellow circle movement




#-----clear the screen after timer ends-----
def clear_screen_after_timer():
    """Clears all turtles and elements after the timer ends."""
    t.hideturtle()
    yellow_circle.hideturtle()
    counter.clear()
    score_writer.clear()




#-----display score message-----
def display_score_message():
    """Displays the final score and message based on score."""
    final_message = trtl.Turtle()
    final_message.hideturtle()
    final_message.penup()
    final_message.goto(0, 100)




    # Display score
    final_message.write(f"Your Score: {score} ({steps} steps)", font=("Arial", 30, "normal"), align="center")




    # Display message based on score
   
    if score >= 100:
        final_message.goto(0, 50)
        final_message.write("Perfect!", font=("Arial", 30, "normal"), align="center")
    elif 80 <= score < 100:
        final_message.goto(0, 50)
        final_message.write("Awesome!", font=("Arial", 30, "normal"), align="center")
    elif 50 <= score < 80:
        final_message.goto(0, 50)
        final_message.write("Try Again!", font=("Arial", 30, "normal"), align="center")
    else:
        final_message.goto(0, 50)
        final_message.write("Better luck next time!", font=("Arial", 30, "normal"), align="center")




#-----events and screen setup-----
wn.listen()  # Enable keyboard listening




# Bind keys for movement
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")




# Create dots
create_dots()




# Move the yellow circle initially and start its movement








# Keep the screen open
wn.mainloop()















