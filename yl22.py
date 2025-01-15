from datetime import datetime, timedelta
import dateparser


# kp = datetime(2008, 6, 14)
# now = datetime.now()
# print(now)
# print(now.strftime("%d.%m %Y %H:%M:%S"))

# # Arvuta nende kahe kuupäeva vahe
# vahe = now - kp

# print("Kuupäevade vahe päevades:", vahe.days)
# print("Kuupäevade vahe aastades:", int(vahe.days/365))

# #Jubelaasta
# if int (vahe.days/365)%5==0:
#     print("Juubel")
# else:
#     print("Ei ole juubel")





#22.2

import csv

now = datetime.now()
faili_nimi = 'rentals.csv'
kokku = 0
kliendid = []
vanus = []
vanused = []
mvordsed = 0
rendiajad = []
# Faili avamine ja lugemine
with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    rentals = csv.reader(fail)
    pais = next(rentals)

    for rent in rentals:
        kokku+=1
        #Vanused
        kp = rent[8].split("/")
        synna = datetime(int(kp[2]),int(kp[0]),int(kp[1]), )
        vanus = int((now - synna).days/365)
        vanused.append(int(vanus))
        #Unikaalsed ID
        if rent[7] not in kliendid:
            kliendid.append(rent[7])
        #Risti kontorid
        if rent[2]!=rent[3]:
            mvordsed+=1
        #Keskmine rentimise aeg
        ajavahe = datetime.strptime(rent[1], "%d/%m/%Y")-datetime.strptime(rent[0],"%d/%m/%Y")
        rendiajad.append(ajavahe.days)


print(f"Rentimisi kokku: {kokku-1}")
print(f"Kliente kokku: {len(kliendid)}")
print(f"Keskmine vanus: {sum(vanused)/len(vanused):0.1f}")
print(f"Risti kontorite rentimise osakaal {mvordsed/kokku*100:0.2f}%")
print(f"Risti kontorite rentimise osakaal {sum(rendiajad)/len(rendiajad):0.1f}%")
