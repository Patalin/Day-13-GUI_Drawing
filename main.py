# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# tim.shape("turtle")
# tim.color("red")
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# colours = ["Green", "Red", "black", "yellow", "violet", "DeepSkyBlue", "wheat", "IndianRed", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# directions = [0, 90, 180, 270]
# for _ in range(200):
#     tim.speed(100)
#     tim.pensize(10)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())

for _ in range(72):
    tim.color(random_color())
    tim.speed(11)
    tim.circle(100, 360, 36)
    tim.left(5)
    # tim.tilt(30)

screen = Screen()
screen.exitonclick()
