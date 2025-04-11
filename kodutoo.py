# 10 kaugushüpe
def kaugushuppe():
    tulemused = []
    
    for i in range(3):
        try:
            tulemus = float(input(f"sisesta kaugushüpe #{i+1} (meeter): "))  # küsime kasutajalt kaugushüppe tulemuse
            tulemused.append(tulemus)  # salvestame tulemuse
        except ValueError:
            print("palun sisesta kehtiv arv.")  # kui sisestatakse vale väärtus, siis anname veateate
            return

    parim_tulemus = max(tulemused)  # leiame parima tulemuse
    keskmine_tulemus = sum(tulemused) / len(tulemused)  # arvutame keskmise tulemuse
    print(f"parim kaugushüpe: {parim_tulemus} m")  # kuvame parima tulemuse
    print(f"keskmine kaugushüpe: {keskmine_tulemus:.2f} m")  # kuvame keskmise tulemuse

kaugushuppe()  # käivitame kaugushüppe programmi


# 11 salakeel
def salakeel():
    valik = input("kas soovid salakeelt luua (1) või tõlkida (2)? ")  # küsime, kas tahame salakeelt luua või tõlkida

    if valik == "1":  # kui valitakse salakeele loomine
        tavaline_sona = input("sisesta tavaline sõna: ")  # palume sisestada tavaline sõna
        salakeel = ''.join(['x' for _ in tavaline_sona])  # muudame sõna tähed x-ideks
        print(f"salakeeles: {salakeel}")  # kuvame salakeeles sõna
    
    elif valik == "2":  # kui valitakse salakeele tõlkimine
        salakeel_sona = input("sisesta salakeeles sõna: ")  # palume sisestada salakeeles sõna
        normaalne_sona = ''.join(['*' for _ in salakeel_sona])  # muudame kõik tähed *-deks
        print(f"normaalses keeles: {normaalne_sona}")  # kuvame normaalses keeles sõna

salakeel()  # käivitame salakeele programmi


# 12 eurokalkulaator
def eurokalkulaator():
    def eur_eeek(eur):  # funktsioon eurode teisendamiseks kroonideks
        return eur * 15.6466

    def eek_eur(eek):  # funktsioon kroonide teisendamiseks eurodeks
        return eek / 15.6466

    valik = input("kas soovid teisendada eur -> eek (1) või eek -> eur (2)? ")  # küsime, kas tahame teha teisendust eurodest kroonideks või vastupidi

    if valik == "1":  # kui valitakse eur -> eek
        eur = float(input("sisesta eurode kogus: "))  # palume sisestada eurode kogus
        print(f"{eur} eur on {eur_eeek(eur)} eek")  # kuvame teisendatud summa
    
    elif valik == "2":  # kui valitakse eek -> eur
        eek = float(input("sisesta eek summa: "))  # palume sisestada kroonide summa
        print(f"{eek} eek on {EEK_eur(eek)} eur")  # kuvame teisendatud summa

eurokalkulaator()  # käivitame eurokalkulaatori programmi


# 13 paaris või paaritu
def paaris_või_paaritu():
    try:
        arv = int(input("sisesta arv et kontrollida kas see on paaris või paaritu: "))  # küsime, kas arv on paaris või paaritu
    except ValueError:
        print("palun sisesta kehtiv arv.")  # kui sisestatakse vale väärtus, siis anname veateate
        return

    if arv == 0:  # kui arv on null
        print("arv ei saa olla null.")  # anname teada, et null ei ole lubatud
    elif arv % 2 == 0:  # kui arv on paaris
        print(f"{arv} on paaris.")  # kuvame, et arv on paaris
    else:  # kui arv on paaritu
        print(f"{arv} on paaritu.")  # kuvame, et arv on paaritu

paaris_või_paaritu()  # käivitame paaris või paaritu programmi


# 15 temperatuurid
def temperatuurid():
    jaanuar = [-16, -12, -15, -20, 0, -1, -20, -2, -20, -14, -18, -8, 2, -1, -14, -7, -15, -17, -6, -17, -17, -7, 0, 3, -20, -17, -15, -8, -12, 3]
    veebruar = [-9, -2, -7, 1, -16, -19, -19, -11, -16, -15, -9, -2, -16, -4, -20, -5, -6, -17, -5, 0, -16, 2, 0, -20, -16, -2, -18]
    marts = [2, -9, -1, -3, -6, -2, 1, -2, -3, -9, -1, -4, 0, -6, -7, 1, 0, 2, -5, -10, 2, -7, -3, 2, -10, 2, -9, -8, -5, -2]
    april = [-5, 0, 10, -9, 0, -9, -8, 6, -5, 3, -1, 4, 9, -1, 2, 0, 10, 0, 5, 0, -10, 0, 6, 3, -6, -2, -10, -8, -2]
    mai = [12, 5, 8, -1, -2, 4, 10, -1, 7, 15, 7, 3, 6, 4, 10, 9, 13, 6, 14, 10, 14, 2, 6, 12, 15, 2, 14, 11, 9, 1]
    juuni = [12, 5, 17, 6, 10, 14, 9, 7, 15, 23, 29, 11, 16, 18, 9, 25, 14, 8, 16, 22, 19, 22, 23, 18, 16, 16, 26, 24, 22]
    juuli = [15, 8, 21, 28, 18, 13, 9, 9, 8, 6, 8, 12, 12, 29, 28, 20, 6, 9, 12, 8, 14, 18, 14, 13, 23, 6, 24, 24, 17, 20]
    august = [7, 6, 5, 19, 18, 18, 17, 20, 15, 11, 7, 10, 13, 12, 20, 11, 10, 14, 18, 14, 24, 6, 17, 16, 6, 17, 5, 13, 11]
    september = [21, 19, 21, 9, 13, 18, 6, 6, 20, 7, 25, 13, 8, 9, 14, 16, 19, 10, 7, 25, 7, 17, 16, 15, 17, 18, 15, 9, 19]
    oktoober = [2, 2, 1, 5, -2, 5, 5, 2, 2, 2, 1, -2, 1, -2, 0, -2, 5, 4, 0, 1, -1, 2, 0, 2, 2, 2, -1, 1, 4, -1]
    november = [-6, -7, -2, -7, -2, -4, 0, -7, -8, -6, 0, -9, -2, -3, -2, 0, -8, -2, -5, -2, -5, -8, -10, 0, -2, -9, -9, -7, -1]
    detsember = [-15, 2, -11, -14, -15, -5, -5, -18, -18, -19, 0, 0, 2, -7, -16, -7, -4, -1, -1, -16, -18, -10, -3, -19, -6, -16, -16, -8, -2, -18]

    kuud = [jaanuar, veebruar, marts, april, mai, juuni, juuli, august, september, oktoober, november, detsember]
    kuud_nimed = ["Jaanuar", "Veebruar", "Märts", "Aprill", "Mai", "Juuni", "Juuli", "August", "September", "Oktoober", "November", "Detsember"]
    
    for i, kuu in enumerate(kuud):  # läbime kõik kuud
        max_temp = max(kuu)  # leiame kuus kõrgeima temperatuuri
        max_temp_paeva_indeks = kuu.index(max_temp)  # leiame päeva, millel oli kõige soojem
        print(f"{kuud_nimed[i]}: kõige soojem päev oli {max_temp_paeva_indeks + 1}. päeval, temperatuur oli {max_temp}°C")  # kuvame tulemuse

temperatuurid()  #
