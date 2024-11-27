import turtle

def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Enlarged Turtle Graphics")
    return screen

def draw_rounded_square(t):
    t.speed(2)
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    t.pencolor("black")
    t.pensize(5)
    t.fillcolor("blue")
    t.begin_fill()
    for _ in range(4):
        t.right(90)
        t.circle(150, 180)
    t.end_fill()

def draw_inner_square(t):
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    for _ in range(4):
        t.forward(300)
        t.left(90)
    t.end_fill()

def draw_inner_circle_pattern(t):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    radius = 70
    t.circle(radius)
    t.end_fill()

def main():
    screen = setup_screen()
    t = turtle.Turtle()
    draw_rounded_square(t)
    draw_inner_square(t)
    draw_inner_circle_pattern(t)
    screen.mainloop()

if __name__ == "__main__":
    main()