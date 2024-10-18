#18.10.2024 Karl
#Ülesanne 6

# Redel
#Mata
import turtle
import math
korgus = 4.4
nurk = 53
kaugus = abs(korgus/math.tan(nurk))
c = math.sqrt(korgus**2 + kaugus**2)
print(kaugus, c)
#Turtle joonis
kordaja = 10
turtle.forward(kaugus*kordaja)
turtle.left(90)
turtle.forward(korgus*kordaja)
turtle.left(180-67)
turtle.forward(c*kordaja)













turtle.done()