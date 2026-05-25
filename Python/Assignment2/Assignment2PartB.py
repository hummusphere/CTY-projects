#Import and name turtle
import turtle
t = turtle.Pen()

#make turtle into a turtle
t.shape("turtle")

#make the turtle may favorite color
t.color("lime")

#position turtle
t.penup()
t.left(90)
t.forward(150)
t.right(90)
t.backward(150)

#Draw glasses

# Left side
t.pendown()
t.pensize(2)
t.left(140)
t.forward(20)
t.left(120)
t.forward(70)

#make left circle
t.circle(30)

#middle 
t.left(100)
t.penup()
t.forward(60)
t.pendown()
t.forward(25)

#make right circle
t.left(255)
t.circle(30)

# Right side
t.right(260)
t.penup()
t.forward(60)
t.pendown()
t.left(90)
t.forward(70)
t.right(120)
t.forward(20)
