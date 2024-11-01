#Alexis Furmage
#10-29-24
#P4LAB1a
# Write a turtle graphics programs that draws a triangle and a square using loops.


import turtle

# Set up the turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

# Draw a square
t.penup()
t.goto(-50, 0)  # Move to a starting position for the square
t.pendown()
draw_square(100)

# Draw a triangle
t.penup()
t.goto(0, 0)  # Move to a starting position for the triangle
t.pendown()
draw_triangle(100)

# Finish up
t.hideturtle()
screen.mainloop()
