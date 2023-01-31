import random
import turtle

import colorgram
from turtle import Turtle, Screen

# my_colors = colorgram.extract('image.jpg', 30)
# my_colors_rgb =[]
# for item in my_colors:
#     color_tuple = item.rgb
#     r = color_tuple.r
#     g = color_tuple.g
#     b = color_tuple.b
#     my_colors_rgb.append((r, g, b))
#
# print(my_colors_rgb)
# The colors are extracted from the image.jpg and saved in the list below. There is no need to repeat the lines above.
turtle.colormode(255)

color_list = [(207, 160, 82), (54, 88, 130),
              (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104),
              (169, 160, 39),
              (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180),
              (59, 39, 31),
              (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121),
              (219, 175, 187), (169, 206, 172), (219, 182, 169)]

muf = Turtle()
screen = Screen()
my_screen = screen.screensize()
muf.up()
muf.speed("fastest")

# Adjusting the first location of drawer so that our painting fits in the screen.
muf.setheading(225)
muf.forward(300)
muf.setheading(0)

dot_size = 20
dot_interval = 50

for i in range(10):
    starting_pos = muf.pos()
    for _ in range(10):
        muf.dot(dot_size, random.choice(color_list))
        muf.forward(dot_interval)
    muf.setposition(starting_pos[0],starting_pos[1] + 50)

screen.exitonclick()