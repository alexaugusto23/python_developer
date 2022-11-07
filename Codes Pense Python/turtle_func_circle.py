import turtle
from math import pi
from time import sleep

object = turtle.Turtle()

def polygon(t: object = None, n: int = None ,  length: int = None) -> object :  
    """
    A função executa o pacote turtle que desenha a forma de um polígono de n tamanhos.
    :param t: object
    :param n: int
    :param length: int
    :return object 
    """

    angle  = 360 / n

    for i in range(n):
        sleep(0.5)
        t.fd(length)
        t.lt(angle)
        

def circle(t: object = None, r: int = None) -> object :  
    """
    A função executa o pacote turtle que desenha a forma de um circulo.
    :param t: object
    :param r: int
    :return object 
    """

    circuferencia = 2 * pi * r
    n = int(circuferencia / 3) + 1
    length = circuferencia / n 
    polygon(t=t, n=n, length = length) 

circle(t=object ,r=10)
