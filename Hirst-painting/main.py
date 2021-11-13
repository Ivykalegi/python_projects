import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract('image.jpg', 30)

# rgb_colors = []

# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

# print(rgb_colors)


turtle = Turtle()
turtle.hideturtle()
turtle.penup()
screen = Screen()
screen.colormode(255)


color_list = [(229, 225, 221), (218, 229, 220), (233, 220, 226), (218, 223, 230), (230, 207, 91), (225, 149, 91),
              (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145)
              (233, 81, 49), (202, 67, 27),
              (192, 186, 23), (174, 18, 13), (33, 129, 49), (7, 99, 37), (13, 64, 39), (12, 41, 76), (242, 203, 4),
              (139, 79, 92), (88, 13, 20), (53, 166, 76), (51, 23, 19), (180, 134, 146), (6, 64, 137), (213, 68, 75),
              (230, 170, 161), (49, 151, 191), (77, 133, 186), (175, 204, 176)]

turtle.speed("fastest")
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if dot_count %10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen.exitonclick()
