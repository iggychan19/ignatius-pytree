'''Ignatius Chan, 230653K, AA2303'''

import turtle

def drawSquare(myTurtle, top_left, size, color):
    # Function to draw a square
    myTurtle.fillcolor(color)  # Set the fill color for the square
    myTurtle.up()  # Lift the pen up to move without drawing
    myTurtle.goto(top_left[0], top_left[1])  # Move to the top-left corner
    myTurtle.down()  # Put the pen down to start drawing
    myTurtle.setheading(0)  # Set the direction of the turtle to east

    # Drawing the square
    myTurtle.begin_fill()  # Begin the fill process for the square
    for _ in range(4):  # Repeat 4 times as a square has 4 sides
        myTurtle.forward(size)  # Move forward by 'size' units
        myTurtle.right(90)  # Turn right by 90 degrees
    myTurtle.end_fill()  # End the filling process

def sierpinskiCarpet(myTurtle, top_left, size, degree, colors):
    # Recursive function to draw the Sierpinski Carpet
    color = colors[degree % len(colors)]  # Choose color based on the recursion level
    drawSquare(myTurtle, top_left, size, color)  # Draw the main square

    # Recursion for creating smaller squares
    if degree > 0:
        new_size = size / 3  # Calculate the size of the smaller squares

        # Loop through the 3x3 grid to draw smaller squares
        for i in range(3):
            for j in range(3):
                # Skip the center square of the grid
                if not (i == 1 and j == 1):
                    # Calculate the top-left point of the new smaller square
                    new_top_left = (top_left[0] + i * new_size, top_left[1] - j * new_size)
                    # Recursive call to draw smaller square
                    sierpinskiCarpet(myTurtle, new_top_left, new_size, degree - 1, colors)

def main():
    # Set up the turtle and the window
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.tracer(0)  # Disable animation for faster drawing

    # Initial parameters for the Sierpinski Carpet
    size = 300  # Size of the initial square
    top_left = (-150, 150)  # Coordinates of the top-left corner of the initial square
    degree = 3  # The depth of recursion
    colors = ['blue', 'red', 'green', 'cyan', 'yellow']  # List of colors for different recursion levels

    # Start drawing the Sierpinski Carpet
    sierpinskiCarpet(myTurtle, top_left, size, degree, colors)

    # Clean up
    myTurtle.hideturtle()  # Hide the turtle cursor
    myWin.exitonclick()  # Close the window when clicked

if __name__ == "__main__":
    main()

