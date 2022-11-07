import turtle
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

polygon(t=object, n=7, length = 70) 
