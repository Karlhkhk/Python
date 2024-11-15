import turtle


d = 50
turtle.speed(0)

for i in range(4):
    turtle.left(90)
    for i in range(4):
        turtle.forward(d)
        turtle.left(90)
        turtle.forward(d)
        turtle.right(90)
        turtle.forward(d)
        turtle.left(90)


        