import turtle
import random
wn = turtle.Screen()
w = wn.window_width()
h = wn.window_height()

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()

turtles = [t1, t2, t3, t4, t5, t6]

def square(item, size):
    for x in range(4):
        item.forward(size)
        item.right(90)
        item.forward(size)
        item.left(random.randrange(-180, 180))

wn.tracer(False)
for iteration in range(3):
    for item in turtles:
        item.penup()
        item.goto(random.randrange(-w,w),random.randrange(-h,h))
        item.color(random.randrange(0,255)/255.,random.randrange(0,255)/255.,random.randrange(0,255)/255.)
        item.pendown()
wn.tracer(False)
for move in range(2500):
    for item in turtles:
        item.speed(0)
        square(item,random.randrange(5,25))
wn.tracer(False)

wn.exitonclick()
