#Karl Kold 19.11.24
#ÜL14


import turtle
ekraan = turtle.Screen()
turtle.speed(90)



def turtle_peale_klikkimine(x, y):
    print(x,y)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)

def varv_red():
    turtle.color("red")
def varv_green():  
    turtle.color("green")
def varv_blue():
    turtle.color("blue")
def puhsta_ekraan(x,y):
    turtle.clear()
 
ekraan.onclick(turtle_peale_klikkimine, 1)
ekraan.onclick(puhsta_ekraan, 3)
ekraan.onkey(varv_red, "r")
ekraan.onkey(varv_green, "g")
ekraan.onkey(varv_blue, "b")
ekraan.listen()
turtle.mainloop()