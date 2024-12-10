valik = input("Sisesta faili nimi:")
fail = open(valik)
read = fail.readlines()
mitmes = 1
for i in read:
    print(mitmes, i, end='') 
    mitmes +=1


lugu = int(input("Sisesta loonumber: "))
fail = open(valik)
read = fail.readlines()
for i in read:
    print ( i, end='' )