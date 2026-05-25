#Python program that makes art.

#Import functions and name them
import turtle as tle
import random as ran

#Make the background black and reshape the turtle
tle.bgcolor(0, 0, 0)
tle.shape('turtle')

#assign varibles and random rbg values
tick = 1
Rbg = ran.uniform(0.1, 1)
rBg = ran.uniform(0.1, 1)
rbG = ran.uniform(0.1, 1)
sides = ran.randint(3,6)

#loop
for count in range(0, 270):
    #set color to the random rbg values
    tle.color(Rbg, rBg, rbG)

    #Make the shapes
    tle.forward(count)
    tle.left(360 / sides)

    #Make sure that ever 5 times the loop is repeated it changes color
    tick = tick + 1
    if tick == 5:
        tick = 1
        Rbg = ran.uniform(0.1, 1)
        rBg = ran.uniform(0.1, 1)
        rbG = ran.uniform(0.1, 1)
        
    
    
