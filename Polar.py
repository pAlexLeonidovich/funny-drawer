import turtle
import math

def mainline(subj):
    subj.color('red')
    subj.width(3)
    for i in range(4):
        subj.forward(300)
        subj.backward(300)
        subj.left(90)

def drawdot(subj,angle,radius):
    subj.color("green")
    subj.up()
    subj.setheading(angle)
    subj.forward(radius)
    subj.dot(5)
    subj.backward(radius)
    subj.down()


def drawfunc(subj, function):
    if '=' not in function:
        print("it is not func")
        return

    left_side, right_side = function.split('=')


    for a in range(0, 360):

        if 'x' in left_side:
            x = eval(right_side, {"__builtins__": None}, {**vars(math), "a": a, "abs": abs})
        else:
            x = eval(left_side, {"__builtins__": None}, {**vars(math), "a": a, "abs": abs})

        if 0 <= x <= 300:
            drawdot(subj, a, x)

drawer = turtle.Turtle()

drawer.hideturtle()
turtle.tracer(0,0)
turtle.Screen().bgcolor("black")

mainline(drawer)
drawfunc(drawer, 'x = 180 + 40 * tan(radians(a * 6))')

turtle.done()