import turtle
import math
X_MAX = 200
X_MIN = -200
Y_MAX = 200
Y_MIN = -200

def init():
    turtle.penup()
    turtle.tracer(0)
    turtle.goto(X_MIN, Y_MAX)
    turtle.pendown()
    for i in range(4):
        turtle.forward(400)
        turtle.right(90)

def rectangle_will_fit(x, y, length, height):
    turtle.tracer(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    if x+length > X_MAX or x < X_MIN:
        return False

    if y+height > Y_MAX or y < Y_MIN:
        return False

    return True


def circle_will_fit(x, y, length):
    turtle.penup()
    turtle.tracer(0)
    turtle.goto(x, y)
    turtle.setheading(0)
    i = 0
    if x+length > X_MAX or x-length < X_MIN:
        return False

    if y+length > Y_MAX or y-length < Y_MIN:
        return False

    return True


def triangle_will_fit(x, y, length):
    turtle.penup()
    turtle.tracer(0)
    turtle.goto(x, y)
    turtle.setheading(0)
    if x<X_MIN or x+length>X_MAX:
        return False

    if y < Y_MIN or y+(length*math.sqrt(3)/2) > Y_MAX:
        return False

    return True

def draw_shape(shape, color_code, x, y, length, height):
    turtle.tracer(1)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color_code)
    if shape == 'r' and rectangle_will_fit(x, y, length, height):
        turtle.begin_fill()
        turtle.fillcolor(color_code)
        for i in range(2):
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill()
        input()

    elif shape == 'c' and circle_will_fit(x, y, length):
        turtle.tracer(1)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(color_code)
        turtle.circle(length)
        turtle.end_fill()

    elif shape == 't' and triangle_will_fit(x, y, length):
        turtle.tracer(1)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(color_code)
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
        turtle.end_fill()

    else:
        return 0


def main():
    init()
    draw_shape('t', 'blue', 100, -100, 100, 0)
    draw_shape('c', 'green', 100, 100, 50, 0)
    draw_shape('r', 'red', -100, -50, 60, 50)

main()
