#Ülesanne 3
#Karl Kold 05.12.24


#3.1

# fail = open ("rebased.txt", encoding="UTF-8")

# vastuvõetud = []

# for rida in fail:
#     vastuvõetud.append(int(rida))
# print(vastuvõetud)
# fail.close()

# a = int(input("Palun sisestage, millise aasta andmeid vajate? "))

# print(vastuvõetud[int(a[3])-1])

#3.2


fail = open("konto.txt", encoding="UTF-8")

for rida in fail:
    if float(rida) > 0:
        print (rida, end="")