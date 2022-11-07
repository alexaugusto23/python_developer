import turtle
from time import sleep

bob = turtle.Turtle()

for i in range(4):
    sleep(0.5)
    bob.fd(100)
    bob.lt(90)