from math import *
#Karl Kold
#Harjutus 02
#30.09.24

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

