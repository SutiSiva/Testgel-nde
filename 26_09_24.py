#Turtle Übungen

'''import turtle
john = turtle.Turtle()

john.width(5)
john.penup()
john.back(140)
john.pendown()

for color in ["red", "blue", "green"]:
  john.color(color)
  john.forward(10)
  john.penup()
  john.forward(10)
  john.pendown()
turtle.done()'''

'''import turtle
john = turtle.Turtle()

john.width(5)
john.penup()
john.back(140)
john.pendown()

for color in ["red", "orange", "yellow", "green", "blue", "purple", "black"]:
    john.color(color)
    john.right(120)
    john.forward(100)
    john.right(120)
    john.forward(100)
    john.right(120)
    john.forward(100)
    if color == "black":
        john.penup()
    else:
        john.penup()
        john.right(50)
        john.forward(100)
        john.pendown()


turtle.done()'''

'''import turtle
john = turtle.Turtle()

john.width(5)
john.penup()
john.back(140)
john.pendown()
for count in range(6):
    for color in ["red", "orange", "yellow", "green", "blue", "purple"]:
        john.color(color)
        john.right(120)
        john.forward(100)
        john.right(120)
        john.forward(100)
        john.right(120)
        john.forward(100)
        if color == "purple":
            john.penup()
        else:
            john.penup()
            john.right(60)
            john.forward(100)
            john.pendown()
    john.penup()
    john.right(120)
    john.forward(100)
    john.left(60)
    john.forward(100)
    john.pendown()
    john.left(60)



turtle.done()'''

'''import turtle
john = turtle.Turtle()
john.color("black")
john.width(3)
for repeat in range(4):
    length = (repeat+1)*10
    for quadrat in range(4):
        john.forward(length)
        john.right(90)
    john.penup()
    john.backward(5)
    john.left(90)
    john.forward(5)
    john.right(90)
    john.pendown()

turtle.done()'''

import turtle
john = turtle.Turtle()
john.color("black")
john.width(3)
for repeat in range(4):
    length = (repeat+1)*10
    for pentagon in range(5):
        john.forward(length)
        john.right(72)
    john.penup()
    john.backward(5)
    john.left(90)
    john.forward(7.5)
    john.right(90)
    john.pendown()

turtle.done()