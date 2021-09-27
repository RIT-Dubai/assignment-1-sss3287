import turtle
X_MAX = 400
X_MIN = -X_MAX
Y_MAX = 400
Y_MIN = -Y_MAX

#Below checks if rectangle will fit in python window
def rectangle_will_fit(x, y, length, height):
    if X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX and X_MIN <= x + length <= X_MAX and Y_MIN <= y - height:
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
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    input()

def main():
    draw_shape('r', 'red', 50, 50, 300, 150)

main()
