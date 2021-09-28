import turtle
import assignment1

def test_rectangle_will_fit():
    assignment1.rectangle_will_fit(-100, 100, 50, 50)

    x = -100
    assert (x == -100)

    y = 100
    assert (y == 100)

    length1 = 50
    assert (length1 == 50)

    height1 = 50
    assert (height1 == 50)


def test_draw_shape():
    assignment1.draw_shape('r', 'red', 50, 50, 300, 150)

    shape = 'r'
    assert(shape=='r')

    color_code = 'red'
    assert (color_code=='red')

    x = 50
    assert (x==50)

    y = 50
    assert (y==50)

    length = 300
    assert (length==300)

    height = 150
    assert (height==150)


def test_draw_shape():
    assignment1.draw_shape('c', 'pink', 0, 0, 150, 0)

    shape = 'c'
    assert(shape=='c')

    color_code = 'pink'
    assert (color_code=='pink')

    x = 0
    assert (x==0)

    y = 0
    assert (y==0)

    length = 150
    assert (length==150)

    height = 0
    assert (height==0)


def test_draw_shape():
    assignment1.draw_shape('t', 'blue', 50, 50, 200, 0)

    shape = 't'
    assert(shape=='t')

    color_code = 'blue'
    assert (color_code=='blue')

    x = 50
    assert (x==50)

    y = 50
    assert (y==50)

    length = 200
    assert (length==200)

    height = 0
    assert (height==0)


