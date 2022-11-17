"""Pong"""
from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong') 
# screen.tracer(0)

right_paddle = Turtle()
# right_paddle.shape('square')
# right_paddle.color('white')
r_pad = right_paddle
r_pad.shape('square')
r_pad.color('white')
r_pad.shapesize(stretch_wid=5, stretch_len=1, outline=1 )
r_pad.penup()
r_pad.goto(350, 0)















screen.exitonclick()
