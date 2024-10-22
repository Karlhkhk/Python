#22.10.24 Karl
#Ülesanne 7 massiivid

#Aastaajad
kuud = [('jaanuar' ,5,-19,-16,-6,0,8,3,4,-17,3,-9,6,-13,-7,-15,-17,-13,-9,-20,-8,-10,-3,-13,-18,9,-10,-17,-16,-15,-12,4),
('veebruar' ,4,-12,-18,-14,-4,0,-17,-5,-16,-9,10,-9,-19,-3,5,10,2,-6,-3,2,-3,2,1,-12,-15,-12,-11,-18,),
('märts' ,-3,4,-11,-10,5,3,-16,3,4,3,-2,-16,-7,-18,-10,-7,2,-19,1,-7,-1,-18,-13,0,-8,0,-8,-8,-9,-13,0),
('aprill' ,-17,-11,3,6,5,-16,9,-16,3,-11,-19,9,5,-14,-16,3,-20,-20,-1,0,-16,-5,3,-7,-6,2,-5,-5,7,-10),
('mai' ,2,-15,-20,-19,-7,-5,-7,-19,1,-2,-2,-7,2,10,-20,-6,1,-10,7,-2,6,3,6,-13,-6,-19,-8,4,-9,0,5),
('juuni' ,-3,-20,-2,6,10,4,-7,4,6,-18,8,-5,10,2,-16,-17,-9,3,-17,-12,-18,9,-12,-16,3,-16,0,2,-5,4),
('juuli' ,-1,1,7,-16,-20,-3,1,-18,-9,-12,-8,-12,-7,8,-3,-17,-7,-7,-9,-1,6,-4,-13,-12,9,-6,-8,-10,-6,6,-14),
('august' ,-4,-19,9,-10,-13,4,-16,10,-16,1,-17,-8,-17,-12,8,-11,10,-12,-14,-18,5,-12,-18,1,-17,3,2,-7,-3,0,-10),
('september',8,4,-16,-18,-9,-2,-8,-7,-12,-9,9,-14,-4,-2,8,0,4,-16,8,-9,-13,-2,0,-6,-2,-16,-14,8,-20,1),
('oktoober',-5,-4,-7,-8,-3,-12,5,7,2,-13,3,-10,-3,-13,2,-5,-6,9,-17,-13,-20,-3,-20,-9,-11,-13,-7,-9,6,-9,-12),
('november',-7,-14,-6,-20,-15,-8,-11,-2,7,-4,5,-15,-18,-9,-7,2,4,-8,-5,-13,-2,-3,-18,7,-7,-15,2,-9,-9,-18),
('detsember',-14,0,-14,-17,7,5,3,4,-16,-18,-4,-5,2,-7,-7,4,2,7,-18,-18,4,9,-11,-3,5,-18,-16,6,-13,-1,4)]

print(f"Hetkekuu {kuud[9][0]}")
kuus_kokku = len(kuud[9])-1
print(f"Viimane mõõtmine: {kuud[9][len(kuud[9])-1]}")
print("Selle kuu temperatuurid")
ajutine = []
for i in range(kuus_kokku):
    ajutine.append(kuud [9][i+1])
    print(kuud [9][i+1], end=", ")

print (ajutine)
print(f"Max temp: {max(ajutine)}") 
print(f"Min temp: {min(ajutine)}") 
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")
print(f"-20 esineb {ajutine.count(-20)} korda") 
ajutine.pop(5-1)
ajutine.insert(5-1, 16)
ajutine.sort()
print(ajutine)




""""
      
#Muusikaplada

Laulud = ['ALIKA – "Bridges”','Anett x Fredi – "Read Between The Lines”','villemdrillem – "leekiv armastus”','licherik & Mäx – "PAKSUD”'
,'nublu – "ära ärata”','NOËP – "Move Your Feet”','Trad.Attack! – "Bring It On”'
,'Bedwetters – "It Is What It Is”','Reket – "Panama paberid”'
,'Grete Paia – "Võluväel”']




for i in range(10):
    print (str(i+1)+". "+Laulud[i])

try:
    valik = int(input("Vali lugu 1-10:", ))
    print(f"Mängin: {Laulud[valik-1]}")

except:
    print("Tegid vale otsuse")




"""