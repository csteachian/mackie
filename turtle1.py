import turtle
import random

wn = turtle.Screen()
w = wn.window_width()
h = wn.window_height()

t1 = turtle.Turtle()

t1.pendown()
t1.color(255/255,0/255,255/255)
t1.goto(0,0)

def randpos():
    xpos = random.randint(-100,100)
    ypos = random.randint(-200,200)
    t1.goto(xpos,ypos)

def randcol():       
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    t1.color(red/255,green/255,blue/255)

def square():   
    for counter in range(0,4):
        t1.forward(100)
        t1.right(90)

def square():
    xpos = random.randint(-100,100)
    ypos = random.randint(-200,200)
    t1.goto(xpos,ypos)
    
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    t1.color(red/255,green/255,blue/255)
    
    for counter in range(0,4):
        t1.forward(100)
        t1.right(90)

def octagon():
    xpos = random.randint(-100,100)
    ypos = random.randint(-200,200)
    t1.goto(xpos,ypos)
    
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    t1.color(red/255,green/255,blue/255)
    
    for counter in range(0,8):
        t1.forward(50)
        t1.right(45)

def triangle():
    xpos = random.randint(-100,100)
    ypos = random.randint(-200,200)
    t1.goto(xpos,ypos)
    
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    t1.color(red/255,green/255,blue/255)
    
    for counter in range(0,3):
        t1.forward(100)
        t1.right(120)

def star():
    xpos = random.randint(-100,100)
    ypos = random.randint(-200,200)
    t1.goto(xpos,ypos)
    
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    t1.color(red/255,green/255,blue/255)
    
    for counter in range(0,5):
        t1.forward(100)
        t1.right(144)

t1.speed(0)
for loop in range(0,10):
    randpos()
    randcol()
    square()
    randpos()
    randcol()
    triangle()
    randpos()
    randcol()
    star()
    randpos()
    randcol()
    octagon()
wn.exitonclick()
















    
