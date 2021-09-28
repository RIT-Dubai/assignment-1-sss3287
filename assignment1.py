import turtle
X_MAX = 400
X_MIN = -X_MAX
Y_MAX = 400
Y_MIN = -Y_MAX

#Below checks if rectangle will fit in python window


def rectangle_will_fit(x, y, length1, height1):
    if X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX and X_MIN <= x + length1 <= X_MAX and Y_MIN <= y - height1:
        print ('True')
    else:
        print('False')

#Below draws a rectangle of the specified shape,color,x,y,length and height.


def draw_shape(shape, color_code, x, y, length, height):

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
        turtle.begin_fill()
        turtle.fillcolor(color_code)
        turtle.circle(length)
        turtle.end_fill()

    elif shape == 't':
        turtle.begin_fill()
        turtle.fillcolor(color_code)
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
        turtle.end_fill()

    else:
        return



def main():
    draw_shape('c', 'pink', 0, 0, 250, 0)


main()
