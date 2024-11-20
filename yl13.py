#Karl Kold 19.11.24
#ÜL13







import turtle

screen = turtle.Screen()
t = turtle.Turtle()
turtle.speed(0)
# Küsi kasutajalt numbrilist sisendit
pikkus = screen.numinput("Pikusse sisestamine", "Joonlaua Pikkus?", default=20, minval=0, maxval=100)
cm =10
mm = 3



for i in range(int(pikkus)):
    for j in range(10):
        turtle.forward(mm)
        turtle.left(90)
        turtle.forward(mm)
        turtle.left(180)
        turtle.forward(mm)
        turtle.left(90)
    turtle.left(90)
    turtle.forward(cm)
    turtle.write(i+1, font=("Arial", 8, "normal"))
    turtle.left(180)
    turtle.forward(cm)
    turtle.left(90)
    

turtle.done()

