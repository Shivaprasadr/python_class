from rudra_graphics import setup_screen, draw_rounded_square, draw_inner_square, draw_inner_circle_pattern
import turtle

def main():
    screen = setup_screen()
    t = turtle.Turtle()
    draw_rounded_square(t)
    draw_inner_square(t)
    draw_inner_circle_pattern(t)
    screen.mainloop()

if __name__ == "__main__":
    main()