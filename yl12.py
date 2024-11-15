


konto = 10

def konto_haldur(algne_saldo, toiming, summa):
    global konto
    if toiming == "deposiit":
        v = summa + algne_saldo
        konto = v
    else:
        v = summa  - algne_saldo
        konto = v
    return v
    




print(konto_haldur(20, "deposiit", konto))
print(konto_haldur(10, "deposiit", konto))
print(konto_haldur(100, "deposiit", konto))
print(konto_haldur(100, "deposiit", konto))





# kytus = lambda kytusekulu, kaugus: (kytusekulu / 100) + kaugus
# print(kytus(5, 150))






# def temp(t, yhik):
#     """
#     Teisendada temperatuuri Celsiusest Fahrenheitiks ja vastupidi
 
#     Parameetrid:
#     t (int): Temperatuur.
#     yhik (string): "C" või "F".
 
#     Tagastab: 
#     int: Tagastab Temperatuuri
 
#     Näide:
#     >>> temp(2, "c")
#    32
#     Näide:
#     >>> temp(2, "f")
#    -32
#     """

#     if yhik=="c":
#         v = t * 5/9+32
#     else:
#         v = (t - 32)* 5/9

#     return round(v,2)



# print(temp.__doc__)
# print(temp(0,"f"))