
import turtle as t
import numpy as np
import random as r
import math as m
import os as os
class Turtle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.t = t.Turtle()
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.color(color)
    def forward(self, distance):
        self.t.forward(distance)
    def backward(self, distance):
        self.t.backward(distance)
    def left(self, angle):
        self.t.left(angle)
    def right(self, angle):
        self.t.right(angle)
    def penup(self):
        self.t.penup()
    def pendown(self):
        self.t.pendown()
    def color(self, color):
        self.t.color(color)


    def ReadPosition(turtle,name):
        """Read the position of the turtle"""
        # get the position of the turtle and name of each turtle
        position = turtle.t.pos()
        name = turtle.t
        # print the position of the turtle
        print("Position of {}: {}".format(name, position))
        return 1

# create a drawing of rhombicosidodecahedron
    def rhombicosidodecahedron():
        t1 = Turtle(0, 0, "red")
        t2 = Turtle(0, 0, "green")
        t3 = Turtle(0, 0, "blue")
        
        # set the color of the background
        t.bgcolor("black")
        t.tracer(100, 0)
        turtles = np.array([t1, t2, t3])
        turtlesLocation = np.array([t1.t.xcor(), t1.t.ycor(), t2.t.xcor(), t2.t.ycor(), t3.t.xcor(), t3.t.ycor()])

        # create a loop that will draw the rhombicosidodecahedron
        for Item in turtles:
            Turtle.ReadPosition(Item, Item.t)
            if (Item == t1):
                t1.left(90)
                t1.forward(60)
                t1.right(90)
                t1.forward(60)
            if (Item == t2):
                t2.left(-90)
                t2.forward(60)
                t2.right(-90)
                t2.forward(60)
            if (Item == t3):
                t3.forward(60)
                t3.forward(60)
                t3.left(90)
                t3.forward(60)
                t3.right(90)
                t3.forward(60)

        for RNG in turtlesLocation:
            const = [RNG+(3.14/3.14 * r.random()), RNG+(3.14/3.14 * r.random()), RNG+(3.14/3.14 * r.random()),
                     RNG+(3.14/3.14 * r.random()), RNG+(3.14/3.14 * r.random()), RNG+(3.14/3.14 * r.random()),
                     RNG+(3.14/3.14 * r.random()), RNG+(3.14/3.14 * r.random()), RNG+(3.14/3.14 * r.random())]
            print(const)
            # get the average of the random numbers
            average = sum(const) / len(const)
            standardDeviation = r.random() * m.sqrt(sum((x - average) ** 2 for x in const) / len(const))
            for i in range(0, 20000004, 1):
                for i in const:
                    
                    turtles[0].t.rt(average * 3.14)
                    turtles[0].t.fd(average * 2 * standardDeviation + i)
                    turtles[0].t.lt(average * 2 * standardDeviation * 3.14)
                    turtles[0].t.fd(average * 2 * standardDeviation + 3.14)
                    
                    turtles[2].t.rt(average * 2 * 3.14)
                    turtles[2].t.fd(average * 2 * standardDeviation + i)
                    turtles[2].t.lt(average * 2 * standardDeviation * 3.14)
                    turtles[2].t.fd(average * 2 * standardDeviation + 3.14)

                    turtles[1].t.rt(average * 2 * 3.14)
                    turtles[1].t.fd(average * 2 * standardDeviation + i)
                    turtles[1].t.lt(average * 2 * standardDeviation * 3.14)
                    turtles[1].t.fd(average * 2 * standardDeviation + 3.14)
        t.done()
        return 1
# run the turtle
