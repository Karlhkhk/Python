def mahlapakkide_arv (ountekogus):
    mahlapakkidearv = int(round (ountekogus * 0.4/3))
    return mahlapakkidearv
kg = int(input("Õunte kogus: "))
print(mahlapakkide_arv(kg))