import turtle
#tervist
#tsauki
print("hello world")

#16.10.24 Kold
#Ülesanne 4

#Ringi pindala ja Turtle
try:
    r = int(input("Sisesta raadiuse suurus:"))
    s = 3.14 * r **2
    p = 2 * 3.14 * r
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt {p:.2f}  ")
    turtle.circle(r*2, 360)
    turtle.done()

except:
    print("Sisestus vale lollakas")
#Kingituste pakkimine
try:
    kast = 5
    kingitusteArv = int(input("Mittu kingi sul on:"))
    komplektid = kingitusteArv//kast #täisarvu saamine
    yle = kingitusteArv%kast #jäägi saamine
    print (f" Saad teha {komplektid} täis kinkekasti. Üle jääb {yle} kingitust.")
except:
    print("Lisasid koguse valesti")

#Faili allalaadimine
try: 

    Failisuurus = int(input("Sisesta faili suurus:"))
    alla_kiirus = int(input("Sisesta allalaadimise kiiruss:"))
    aeg = Failisuurus/alla_kiirus
    print(f"Alla laadimiseks kulub: {aeg} sekundit")
except:
    print("Sa ei sisestanud täisarvu")

#Raamatute allahindlus
ale = 0.3
hind = 12.50
kogus = int(input("Lisa kogus:"))
summa = (hind - (hind * ale)) * kogus
print(f"{kogus} raamatu hind soodustusega on {summa:.2f}€.")

#Aia pikkus
a = int(input("Lisa 1 külg: "))
b = int(input("Lisa 2 külg: "))
p = 2 * (a + b)
print(f"Aia kogupikkus on: {p} meetrit")