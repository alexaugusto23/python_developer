import turtle
from time import sleep

object = turtle.Turtle()

def square(t: object =None) -> object :  
    """
    A função executa o pacote turtle que desenha a forma de um quadrado.
    :param t: object
    :return object 
    """
    for i in range(4):
        sleep(0.5)
        t.fd(100)
        t.lt(90)

square(object)
