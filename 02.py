from math import *
#Karl Kold
#Harjutus 02
#30.09.24


#Loo kolm täisarvulist muutjat a, b, c
#Loo valem, mis arvutab kolmnurga ümbermõõdu
a=2
b=2
c=2
P= a+b+c
print("Kolmnurga ümbermõõt on:", P, "cm")

#Toote hind
#Toote hind 36,75
#Soodushind hetkel 40%
#Soovin kolme toote summat

hind = 36.75
soodushind = 0.40
kokku = hind * soodushind * 3
print("Kolm summat kokku:", kokku, "Euri")
 
#Pitsa
# kokku: 14,19
# 4,54
Kogu = 14.19
Inimesed = 3

Kokku = Kogu / Inimesed

print("Kokku läheb:", Kokku, "euri")


# Rulluisutajad
kiirus = 29.9
aeg = 24/60
dist = kiirus * aeg

print("Rulluisutaja jõuab:", dist,"km kaugusele")


#Kolmnurga Hüpotenuus

a = 16
b = 9
c = sqrt(a**2+b**2)
print("Hüpotenuus on:",c)


#Ajateisendus
#// - et arvutada täisarvu
#% - et saada minuteid
aeg = int(input("Lisa aeg minutides: "))
h = aeg//60
m = aeg%60
print(h, ":",m)

#Arvusüsteemid
#0 - 9 #kümmnendarvusüsteem
#0 - F #Kuueteistkümnendsüsteem
#0 - 1 #kahendsüsteem

arv = int(input("Lisa arv: "))
kahend = bin(arv)
kuus = hex(arv)
print ("Sinu teisendused on: ",kahend,"ja",kuus)

#Kütusekulu arvutamine

l = int (input("Lisa tangitud liitrid:"))
km = int (input("Lisa läbitud kilomeetrid:"))
kytusekulu = l/(km/100)
print("Sinu kütusekulu on:", kytusekulu)

