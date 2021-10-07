import turtle
import math
X_MAX = 400
X_MIN = -400
Y_MAX = 400
Y_MIN = -400

"""This function draws the window"""


def init():
    turtle.penup()
    turtle.tracer(0)
    turtle.goto(X_MIN//2, Y_MAX//2)
    turtle.pendown()
    for i in range(4):
        turtle.forward(400)
        turtle.right(90)
"""This function checks if the rectangle_will_fit """


def rectangle_will_fit(x, y, length, height):
    XT = x-X_MAX//2
    YT = -y+Y_MAX//2
    turtle.tracer(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    if XT+length>X_MAX//2 or XT<X_MIN//2:
        return False

    if YT+height>Y_MAX//2 or YT<Y_MIN//2:
        return False

    else:
          return True

"""This function checks if the circle_will_fit"""


def circle_will_fit(x, y, length):
    XT = x-X_MAX//2
    YT = -y+Y_MAX//2
    turtle.penup()
    turtle.tracer(0)
    turtle.goto(x, y)
    turtle.setheading(0)
    i = 0
    if XT+length>X_MAX or XT-length<X_MIN:
        return False

    if YT+length>Y_MAX or YT-length<X_MIN:
        return False


    else:
        return True

"""This function checks if the triangle_will_fit"""


def triangle_will_fit(x, y, length):
    XT = x-X_MAX//2
    YT = -y+Y_MAX//2
    turtle.penup()
    turtle.tracer(0)
    turtle.goto(x, y)
    turtle.setheading(0)
    i = 0
    if x<X_MIN or x+length>X_MAX:
        return False

    if y<Y_MIN or y+(length*math.sqrt(3)/2)>Y_MAX:
        return False

    else:
        return True

"""This function limits the colour"""


def get_color(color_code):
    color = ""
    if color_code == "blue":
        color = "blue"
    elif color_code == "green":
        color = "green"
    elif color_code == "red":
        color = "red"

    return color
"""This function draws a rectangle,circle and triangle"""


def draw_shape(shape, color_code, x, y, length, height):
    turtle.tracer(1)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color_code)
    if shape == 'r':
        turtle.begin_fill()
        turtle.fillcolor(color_code)
        for i in range(2):
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill()
        perimeter = 0
        if rectangle_will_fit(-100, -50, 90, 70) == True:
            perimeter = 2*(length + height)
            print("The Perimeter of rectangle is", perimeter)

        else:
            perimeter = 2*(length + height)
            print("The Perimeter of rectangle is", perimeter)

        return perimeter

    elif shape == 'c':
        turtle.tracer(1)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(color_code)
        turtle.circle(length)
        turtle.end_fill()
        perimeter=0
        if circle_will_fit(100, 100, 50)==True:
            perimeter = math.pi*length*2
            print("The Perimeter of circle is", perimeter)
        else:
            print("The Perimeter of circle is", perimeter)

        return perimeter

    elif shape == 't':
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
        perimeter=0
        if triangle_will_fit(100, -100, 100)==True:
            perimeter = length*3
            print("The Perimeter of triangle is", perimeter)
        else:
            print("The Perimeter of triangle is", perimeter)

        return perimeter


    else:
        return 0



def main():
    init()
    draw_shape('t', 'blue', 100, -100, 100, 0)
    draw_shape('c', 'green', 100, 100, 50, 0)
    draw_shape('r', 'red', -50, -50, 90, 70)



main()
