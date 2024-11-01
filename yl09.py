#Ülesanne 09
#01.11.2024
#Karl Kold
import random

#06
nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
unikaalsed_nimed = []
for i in nimed:
    if i not in unikaalsed_nimed:
            unikaalsed_nimed.append(i)


for i in unikaalsed_nimed:
    print(i)
        
        
#07

ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
hinded = []
for i in ryhma_hinded:
    hinded.append(float(i.split(" ")[1]))



print(f"Parim tulemus {max(hinded)}")
print(f"Halvim tulemus {min(hinded)}")
print(f"Keskmine tulemus {sum(hinded)/len(hinded)}")


#08

for i in range(11):
     print(f"{i} x {i} = {i*i}")

#08

tehed = ['+','-','*','/']
punktid = 0
for _ in range(11):
    i = random.randint(1, 10)
    j = random.randint(1, 10)
    tehe = random.choice(tehed)
    if tehe=="+":
        print(f"{i}  {tehe} {j} = ")
        vastus = int(input("Vastus: "))
        if vastus == i+j:
            print("Õige")
            punktid+=1
        else:
            print("Vale")

    elif tehe=="-":
        print(f"{i}  {tehe} {j} = {i-j}")
    elif tehe =="*":
        print(f"{i}  {tehe} {j} = {i*j}")
    else:
        print(f"{i} {tehe} {j} = {round(i/j,2)}")

    


"""
tehted = ['+','-','*','/']
for _ in range(11):
    i = random.randint(1,100)
    j = random.randint(1,100)
    tehe = random.choice(tehted)

    if tehe=="+":
        print(f"{i} {tehe} {j} = {i+j}")
    elif tehe=="-":
        print(f"{i} {tehe} {j} = {i-j}")
    elif tehe=="*":
        print(f"{i} {tehe} {j} = {i*j}")
    else:
        print(f"{i} {tehe} {j} = {round(i/j,2)}")
"""