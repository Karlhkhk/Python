#18.10.2024 Karl
#Ülesanne 5
import random
import turtle

# 4. Mündiviskamise äraarvamine koos juhuslikkusega
mynt = random.randint(0,1)
arva = input("Vali kull või kiri:" )
if (mynt == 0 and arva == "Kiri") or (mynt == 1 and arva == "Kull"):

    vastus ="green"
else:
    vastus = "red"

print(mynt)
turtle.color (vastus)
turtle.circle(100)
turtle.done()



# 3. Vanuse piirang
vanus = int(input("Lisa vanus: "))

if vanus >= 18:
    print("Piisavalt vana")
else:
    print("Liiga noor!")





# 2. Matemaatika test
a = random.randint(1,10)
b = random.randint(1,10)
vastus = int(input(str(a)+"*"+str(b)+"="))
if a*b == vastus:
    print("Tubli!")
else:
    print("Vale")





#1. Ilmaennustuse rakendus
try:
    c = int(input("Lisa kraadid:"))

    if c < 0:
        print("Kanna talveriideid")
    elif c >= 0 and c<=15:
        print("Kanna kevad-sügis rõigaid")
    else:
        print("Kanna suveriideid")
except:
    print("Pane täisarv!")
