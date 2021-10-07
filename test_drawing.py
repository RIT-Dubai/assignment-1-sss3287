import turtle
import math
import drawing

"""This function tests the init function"""


def test_init():
    drawing.init()
    x=round(turtle.xcor(), 0)
    assert (x == -200)

    y=round(turtle.ycor(), 0)
    assert (y == 200)

    pos=turtle.isdown()
    assert (pos == True)

"""This function tests the rectangle_will_fit function"""


def test_rectangle_will_fit():
    r=drawing.rectangle_will_fit(-50, -50, 90, 70)
    x=round(turtle.xcor(), 0)
    assert (x == -50)

    y=round(turtle.ycor(), 0)
    assert (y == -50)

    pos=turtle.isdown()
    assert (pos == False)

    assert(r==False)

"""This function tests the circle_will_fit function"""


def test_circle_will_fit():
    c = drawing.circle_will_fit(100, 100, 50)
    x=round(turtle.xcor(), 0)
    assert (x==100)

    y=round(turtle.ycor(), 0)
    assert (y==100)

    pos=turtle.isdown()
    assert (pos==False)

    assert(c==True)

"""This function tests the triangle_will_fit function"""


def test_triangle_will_fit():
    t=drawing.triangle_will_fit(100, -100, 100)
    x=round(turtle.xcor(), 0)
    assert (x==100)

    y=round(turtle.ycor(), 0)
    assert (y==-100)

    pos=turtle.isdown()
    assert (pos==False)

    assert(t==True)


"""This function tests get_color function"""


def test_get_color():
    color = drawing.get_color("b")
    assert(color == "blue")

"""This function tests draw shape function for rectangle"""


def test_draw_shape_rectangle():
    r = drawing.draw_shape('r', 'blue', -100, -50, 90, 70)

    assert(r == 2*(90+70))

    x = round(turtle.xcor(), 0)
    assert(x == -100)

    y = round(turtle.ycor(), 0)
    assert(y == -50)

    heading = turtle.heading()
    assert(heading == 0)

    color = turtle.fillcolor()
    assert(color == "blue")

"""This function tests the draw shape function for circle"""


def test_draw_shape_circle():
    c = drawing.draw_shape('c', 'green', 100, 100, 50, 0)

    assert(c == 2*math.pi*50)

    x = round(turtle.xcor(), 0)
    assert(x == 100)

    y = round(turtle.ycor(), 0)
    assert(y == 100)

    heading =turtle.heading()
    assert(heading == 0)

    color = turtle.fillcolor()
    assert(color == "green")

"""This function tests the draw shape function for triangle"""


def test_draw_shape_triangle():
    t = drawing.draw_shape('t', 'blue', 100, -100, 100, 0)

    assert(t == 3*100)

    x = round(turtle.xcor(), 0)
    assert(x == 100)

    y = round(turtle.ycor(), 0)
    assert(y == -100)


