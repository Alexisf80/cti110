#Alexis Furmage
#10-29-24
#P4LAB1b
#Write a turtle program that draws my initials "A" and "F".

import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)
t.color("blue")

def draw_A():
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.setheading(75)
    t.forward(100)
    t.right(150)
    t.forward(100
    t.backward(50)
    t.right(105)
    t.forward(30)
    t.penup()

def draw_F():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    t.setheading(90)
    t.forward(100)

    t.right(90) 
    t.forward(50)

    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.setheading(0)
    t.forward(30)

    t.penup()
draw_A()
draw_F()

t.hideturtle()
screen.mainloop()
