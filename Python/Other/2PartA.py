#import the turtle

import turtle

#set up the background
turtle.Screen().setup(1093,440)
turtle.Screen().bgpic("graphPaper.gif")

#name the turtle
t = turtle.Pen()

#make the turtle a turtle
t.shape("turtle")

#position the turtle
t.penup()
t.backward(290)
t.left(90)

#Make the bar graph
t.pendown()

#Line 1
t.color("OrangeRed")
t.forward(64)
t.right(90)
t.forward(60)
t.right(90)
t.forward(64)

#Move Line
t.left(90)
t.forward(44)

#Line 2
t.color("Gold")
t.left(90)
t.forward(64)
t.right(90)
t.forward(60)
t.right(90)
t.forward(64)

#Move Line
t.left(90)
t.forward(44)

#Line 3
t.color("Fuchsia")
t.left(90)
t.forward(64)
t.right(90)
t.forward(60)
t.right(90)
t.forward(64)

#Move Line
t.left(90)
t.forward(44)

#Line 4
t.color("Indigo")
t.left(90)
t.forward(128)
t.right(90)
t.forward(60)
t.right(90)
t.forward(128)

#Move Line
t.left(90)
t.forward(44)

#Line 5
t.color("Red")
t.left(90)
t.forward(64)
t.right(90)
t.forward(60)
t.right(90)
t.forward(64)

#Move Line
t.left(90)
t.forward(44)

#Line 6
t.color("Green")
t.left(90)
t.forward(64)
t.right(90)
t.forward(60)
t.right(90)
t.forward(64)
