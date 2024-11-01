#Ülesanne 09
#01.11.2024
#Karl Kold
import random
import turtle
"""""
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
        if vastus == i-j:
            print("Õige")
            punktid+=1
        else:
            print("Vale")
    elif tehe =="*":
        print(f"{i}  {tehe} {j} = {i*j}")
        if vastus == i*j:
            print("Õige")
            punktid+=1
        else:
            print("Vale")
    else:
        print(f"{i} {tehe} {j} = ")
        vastus = float(input("Vastus: "))
        if vastus == [round{i/j,2}]:
            print("Õige")
            punktid+=1
        else:
            print("Vale")

#11
"""

for i in range(1,6):
    print("*"*i,end = " ")
    print()
for i in range(1,6):
    print("*"*(6-i),end = " ")
    print()

for i in range(1,6):
    print(" "*(6-i)+"*"*i,end = " ")
    print()

        
#12
even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]

sum_even = 0
for i in even_nums:
    if i%2 == 0:
        sum_even=0
    else:
        break

    print("Tsükkel jõudis lõppu", sum_even)

#13
1
2
3
4
5
6
7
8
9
10
11
12
13
14
ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

keskmine_odo=0
keskmine_hind=0
for i in ev_data:
    for j in i:
        print(j, end=" ")
        print(f"{j:>30}", end =" ")
    print()
    

