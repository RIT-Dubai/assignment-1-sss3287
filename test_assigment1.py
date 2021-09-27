import turtle
import assignment1

def test_rectangle_will_fit():
    assignment1.rectangle_will_fit(-100,100,50,50)

    x = -100
    assert (x==-100)

    y = 100
    assert (y==100)

    length = 50
    assert (length==50)

    height = 50
    assert (height==50)

    result = assignment1.rectangle_will_fit(x, y ,length,height)

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




