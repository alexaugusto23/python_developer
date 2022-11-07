import turtle
from time import sleep

object = turtle.Turtle()

def square(t: object = None, length: int = None) -> object :  
    """
    A função executa o pacote turtle que desenha a forma de um quadrado.
    :param t: object
    :param length: int
    :return object 
    """
    for i in range(4):
        sleep(0.5)
        t.fd(length)
        t.lt(90)

square(t=object, length=100)
