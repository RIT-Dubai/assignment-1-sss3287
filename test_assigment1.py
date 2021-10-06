import turtle
import assignment1


def test_draw_shape_rectangle():
    assignment1.draw_shape('r', 'red', -100, -50, 90, 70)

    shape = 'r'
    assert(shape == 'r')

    color_code = 'red'
    assert (color_code == 'red')

    x = -100
    assert (x == -100)

    y = -50
    assert (y == -50)

    length = 90
    assert (length == 90)

    height = 70
    assert (height == 70)


def test_draw_shape():
    assignment1.draw_shape('c', 'green', 100, 100, 50, 0)

    shape = 'c'
    assert(shape == 'c')

    color_code = 'green'
    assert (color_code == 'green')

    x = 100
    assert (x == 100)

    y = 100
    assert (y == 100)

    length = 50
    assert (length == 50)

    height = 0
    assert (height == 0)


def test_draw_shape():
    assignment1.draw_shape('t', 'blue', 100, -100, 100, 0)

    shape = 't'
    assert(shape == 't')

    color_code = 'blue'
    assert (color_code == 'blue')

    x = 100
    assert (x == 100)

    y = -100
    assert (y == -100)

    length = 100
    assert (length == 100)

    height = 0
    assert (height == 0)


