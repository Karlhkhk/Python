#Iseseisevtöö 1
#Karl Kold 05.12.24


#Ülesanne 1.1
# print("Tere, maailm!")

#Ülesanne 1.2

# aasta = 2020
# liblikas = "teelehe-mosaiikliblikas"
# lause_keskosa = ". aasta liblikas on"
# lause = str(aasta) + liblikas + lause_keskosa
# print(lause)

#Ülesanne 1.3 Pilved
# küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
# väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
# väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
# Kasutaja peab saama sisestada pilvede kõrgust nii täisarvuna kui ka ujukomaarvuna, nt 7.5.

# pilvedekorgus = int(input("Pilvede aluse kõrgus: "))
# if pilvedekorgus > 6.0: 
#     print ("Need on ülemised pilved")
# else:
#     pilvedekorgus < 6.0
#     print("Need on alumised pilved")

#Ülesanne 1.4. Bussid
Inimestearv = int(input("Midu inimest on vaja transpordida: "))
Kohtadearv = 40
bussid = Inimestearv//Kohtadearv
viimasesbussis = Inimestearv%Kohtadearv
if viimasesbussis>0:
    print (f"Inimeste arv on {Inimestearv} ja teil on vaja {bussid} bussi, viimases bussis on {viimasesbussis}")
    print(Kohtadearv)
    print(bussid)
    print(viimasesbussis)


