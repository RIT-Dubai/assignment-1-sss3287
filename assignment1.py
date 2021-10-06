import turtle
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
        input()

    elif shape == 'c':
        turtle.tracer(1)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(color_code)
        turtle.circle(length)
        turtle.end_fill()

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

    else:
        return 0


def main():
    init()
    draw_shape('t', 'blue', 100, -100, 100, 0)
    draw_shape('c', 'green', 100, 100, 50, 0)
    draw_shape('r', 'red', -100, -50, 90, 70)

main()
