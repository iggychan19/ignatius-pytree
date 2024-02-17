'''Ignatius Chan, 230653K, AA2303'''

import turtle
import math
import time
import random

# Global variables
a = 45  # Initial angle for Pythagoras tree branches

# Function to draw a filled square of a given size and color
def draw_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# Function to draw a Pythagoras tree recursively
def draw_pythagoras_tree(t, size, level, depth, color_index):
    global a
    if level == 0:
        return

    # Define colors for different levels
    if level in [8, 9, 10]:
        color = '#532915'
    elif level in [0, 3, 5]:
        colors = ['red', 'yellow', 'blue', 'yellow']
        color = colors[color_index % len(colors)]
    else:
        color = 'green'

    left_size = size * math.sin(math.radians(90 - a))
    right_size = size * math.sin(math.radians(a))

    # Draw square
    t.begin_fill()
    draw_square(t, size, color)
    t.end_fill()

    # Left branch
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(180 - a)
    t.forward(left_size)
    t.left(90)
    draw_pythagoras_tree(t, left_size, level - 1, depth, color_index + 1)

    # Right branch
    t.right(180)
    t.forward(right_size)
    t.left(90)
    draw_pythagoras_tree(t, right_size, level - 1, depth, color_index + 1)

    # Return to original position
    t.left(90 - a)
    t.back(size)

# Function to increase angle
def increase_angle():
    global a
    a += 5

# Function to decrease angle
def decrease_angle():
    global a
    a -= 5

# Function to draw a snowflake
def draw_snowflake(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    for i in range(8):  # Draw 8 branches of the snowflake
        branch_length = size
        for _ in range(3):
            t.forward(branch_length)
            t.backward(branch_length)
            t.right(45)
        t.left(90)

# Main function
def main():
    global t, size

    # Create a Turtle graphics screen
    screen = turtle.Screen()
    screen.title("Selective Color Changing Pythagoras Tree with Snowflakes")
    screen.bgcolor("brown")
    screen.colormode(1)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(0)

    # Bind arrow keys
    screen.onkey(increase_angle, "Right")
    screen.onkey(decrease_angle, "Left")
    screen.listen()

    size = 100
    depth = 10

    t.up()
    t.goto(50, -250)
    t.down()
    t.left(90)

    # Drawing the "MERRY XMAS!!!" text
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.up()
    text_turtle.color("white")
    text_turtle.goto(0, 200)
    text_turtle.write("MERRY XMAS!!! (click on your left/right arrow keys)", align="center", font=("Arial", 24, "bold"))

    # Turtle for snowflakes
    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.hideturtle()
    snowflake_turtle.speed(0)

    while True:
        for color_index in range(3):
            t.clear()
            draw_pythagoras_tree(t, size, depth, depth, color_index)
            screen.update()
            time.sleep(0.5)

            # Draw snowflakes
            for _ in range(5):  # Number of snowflakes per cycle
                x = random.randint(-screen.window_width()//2, screen.window_width()//2)
                y = random.randint(-screen.window_height()//2, screen.window_height()//2)
                snowflake_size = random.randint(5, 15)
                draw_snowflake(snowflake_turtle, x, y, snowflake_size)

if __name__ == "__main__":
    main()
