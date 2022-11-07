import turtle
from math import pi
from time import sleep

object = turtle.Turtle()

def arc(t: object = None, r: int = None, angle: int = None):
    """
    A função executa o pacote turtle que desenha a forma de um arco.
    :param t: object
    :param r: int
    :return object 
    """

    arc_lentgh = (2 * pi * r * angle) / 360 
    n = int(arc_lentgh / 3) + 1
    step_lentgh = arc_lentgh / n
    step_angle = angle / n 
    for i in range(n):
        t.fd(step_lentgh)
        t.lt(step_angle)
    t.hideturtle()
    turtle.mainloop()

arc(t=object, r=20, angle=360)

