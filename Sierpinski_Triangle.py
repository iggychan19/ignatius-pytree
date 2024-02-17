'''Ignatius Chan, 230653K, AA2303'''

import turtle

def drawTriangle(points, color, myTurtle):
    # Set the color for the triangle
    myTurtle.fillcolor(color)

    # Start drawing the triangle
    myTurtle.up()  # Lift the pen to move without drawing
    myTurtle.goto(points[0][0], points[0][1])  # Move to the first point
    myTurtle.down()  # Put the pen down to start drawing

    # Draw the triangle and fill it with color
    myTurtle.begin_fill()  # Start filling the triangle with color
    myTurtle.goto(points[1][0], points[1][1])  # Draw line to the second point
    myTurtle.goto(points[2][0], points[2][1])  # Draw line to the third point
    myTurtle.goto(points[0][0], points[0][1])  # Draw line back to the first point
    myTurtle.end_fill()  # Finish filling the triangle with color

def getMid(p1, p2):
    # Calculate the midpoint between two points
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, myTurtle):
    # List of colors to use for different levels of the triangle
    colors = ['blue', 'red', 'green', 'cyan', 'yellow', 'pink']

    # Draw the main triangle
    drawTriangle(points, colors[degree], myTurtle)

    # Recursive calls for the smaller triangles if degree is greater than 0
    if degree > 0:
        # Draw the top left triangle
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)
        
        # Draw the top right triangle
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree - 1, myTurtle)
        
        # Draw the bottom triangle
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)

def main():
    # Create turtle and screen objects
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()

    # Disable animation for faster drawing
    myWin.tracer(0)

    # Define the three points of the largest triangle
    myPoints = [[-200, -50], [0, 200], [200, -50]]
    degree = 5  # Set the depth of recursion

    # Start drawing the Sierpinski triangle
    sierpinski(myPoints, degree, myTurtle)

    # Hide the turtle after drawing is complete
    myTurtle.hideturtle()

    # Wait for a mouse click to exit the program
    myWin.exitonclick()

# Run the program
main()
