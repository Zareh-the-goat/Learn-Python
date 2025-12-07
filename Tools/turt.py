import turtle
import time

window = turtle.Screen()
my_turtle = turtle.Turtle()

my_turtle.speed(0)

for _ in range(4):

    for _ in range(4):
        my_turtle.forward(30)
        time.sleep(0)
        my_turtle.right(90)

    my_turtle.forward(30)

window.exitonclick()
