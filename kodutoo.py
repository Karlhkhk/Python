#Karl Kold IT-24
#18.12.24
#Ülesanne 10, 11, 12 13, 15, 



#Ül 10
	# kasutaja sisestab 3 kaugushĆ¼ppe tulemust - 1p
	# sinu programm leiab ning vĆ¤ljastab parima ja keskmise tulemuse - 2p
	# programmi dialoog kasutajaga on arusaadav ja Ć¼heselt mĆµistetav - 1p
	# kood kommenteeritud - 1p
	
for i in range (3):
    print(input("Sisesta kolm kaugushüppe tulemust: "))
tulemused = [i]
tulemused = print (i)

#Ül 11
# sinu programm kĆ¼sib kasutajalt, kas ta soovib salakeelt luua vĆµi tĆµlkida - 1p
# 	kasutaja sisestab tavalise sĆµna, mis muudetakse salakeeleks - 1p
# 	kasutaja sisestab salakeeles sĆµna, mis teisendatakse jĆ¤lle normaalseks - 1p
# 	kood kommenteeritud - 1p


#Ül 12

# Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
# Oluline on kasutada kahte funktsiooni!!


# # Euro eeki
# summa = float(input("Sisesta eurodes summa: ")) #Kasutaja sisestab Eurodes summa
# print(f"{summa} EUR = {summa * 15.6466:.2f} EEK") #Printib välja EEKis

# # EEK euri
#summa = float(input("Sisesta EEK summa : ")) #Kasutaja sisestab EEkis summa
#print(f"{summa} EEK = {summa / 15.6466:.2f} EUR") #Printib välja euros



# #Ül 13
#kuvatakse korrektne arusaadav kĆ¼simus ja  vastus - 1p
#eelnev kontroll, kas kasutaja ei lisanud arvu vĆµi pani nulli - 2p
#kood mis teavitab paaris vĆµi paaritust arvust - 2p
#kuvatakse programmi pealkiri - 1p



# arv = int(input("Sisesta arv: ")) #Küsib kasutajalt arvu

# if (arv % 2) == 0:#Kontrollib kas arv on paariline või paaritu
#    print("{0} on paariline".format(arv)) #Printib vastuse et on paaritu
# else: #Või siis
#    print("{0} on paaritu".format(arv)) #Paaritu


#Ül 14
#Palkade vĆµrdlus - Loo palk.txt fail tĆ¶Ć¶tajate nime, soo ja palganumbriga (10 tĆ¶Ć¶tajat).
#Koosta programm, mis analĆ¼Ć¼sib kas firmas toimub diskrimineerimist soo jĆ¤rgi. Selleks vĆµrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kĆµige kĆµrgemat palka. Programm peab tegema otsuse.

	


#Ül 15
#Temperatuurid - Programm peab tĆ¶Ć¶tlema Ć¼he aasta kĆµigi pĆ¤evade temperatuure. Kirjutada programm, mis leiab kuude kaupa, mitmendal kuupĆ¤eval oli kĆµige soojem. VĆ¤ljasta kuupĆ¤ev ja vastav temperatuur. (Kui sama temperatuuriga oli mitu pĆ¤eva, vĆ¤ljasta vĆ¤hemalt Ć¼ks)
