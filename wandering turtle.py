from turtle import  *
from random import randint
speed(0)
shape ('turtle')
def wander():
    while True:
        forward(6)
        if xcor() >= 50 or xcor() <= -100 or ycor() <= -100 or ycor() >= 50:
            left(randint(90,92))

wander()
