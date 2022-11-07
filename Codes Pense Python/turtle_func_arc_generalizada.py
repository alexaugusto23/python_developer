import turtle
from math import pi
from time import sleep

object = turtle.Turtle()

def polyline(t: object = None, n: int = None, lentgh: int = None, angle: int = None) -> object:
    """
    Desenha n segmentos de reta com o comprimento dado e 
    ângulo (em graus) entre eles. t é um turtle.
    :param t: object
    :param n: int
    :param lentgh: int
    :param angle: int
    :return object 
    """
    for i in range(n):
        t.fd(lentgh)
        t.lt(angle)


def polygon(t: object = None, n: int = None, lentgh: int = None) -> object:
    """
    A função executa o pacote turtle que desenha a forma de um polígono.
    :param t: object
    :param n: int
    :param lentgh: int
    :return object 
    """

    angle = 360.0 / n
    polyline(t=t, n=n , lentgh=lentgh, angle=angle)
    sleep(1)
    object.clear()


def arc(t: object = None, r: int = None, angle: int = None) -> object:
    """
    A função executa o pacote turtle que desenha a forma de um arco.
    :param t: object
    :param r: int
    :param angle: int
    :return object 
    """

    arc_lentgh = (2 * pi * r * angle) / 360 
    n = int(arc_lentgh / 3) + 1
    step_lentgh = arc_lentgh / n
    step_angle = float(angle) / n 
    polyline(t=t, n=n, lentgh=step_lentgh, angle=step_angle)

def circle(t: object = None, r: int = None) -> object:
    """
    A função executa o pacote turtle que desenha a forma de um círculo.
    :param t: object
    :param r: int
    :return object 
    """
    arc(t=t, r=r, angle=360)
    sleep(1)
    object.clear()

circle(t=object, r=20)
polygon(t=object, n=5, lentgh=30)