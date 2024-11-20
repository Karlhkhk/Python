#Karl Kold 20.11.24
#Ülesanne 16

import os
import datetime


# operatsioonisüsteemi nimi
print(os.getlogin())


#Aktiivne kataloog
print(os.getcwd())

#Skript küsib kasutajalt, mitu kataloogi ta soovib luua
# Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)
try:
    mitu = 3
    x = datetime.datetime.now()
    for i in range(mitu):
        y = x.strftime("%d%m%Y")
        os.mkdir(y+"_"+str(i+1))


#     Kataloogi kustutamine:
# Pärast kataloogide loomist küsib skript kasutajalt, millist äsja loodud või olemasolevat kataloogi soovitakse kustutada, esitades kataloogi nime 1, 2 jne
# Kui sisestatud kataloogi nimi eksisteerib, kustutatakse see
except:
   print("Kataloogid juba olemas lollakas!")

valik = input("Lisa Kataloogi nimi kustutamiseks:")
try:
    os.rmdir(valik)
except:
    print("Sellist kataloogi ei saa kustutada lollakas!")
items = os.listdir('.')
for item in items:
    if os.path.isdir(item):
        print(item)


  
