import random
import math

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
g = open("matrice.txt", "x")
L = []
N = 11454 #numarul de cuvinte din baza de date
LIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

M = []

def fdbk(cuv, cuv2):
    #cuv2 e cuvantul cautat
    user_sol = "00000"

    D1 = DICT[cuv2].copy()
    D2 = DICT[cuv].copy()

    for i in range(5):
        if cuv[i] == cuv2[i]:
            user_sol = user_sol[:i] + "2" + user_sol[i + 1:]
            D1[cuv[i]] -= 1
            D2[cuv[i]] -= 1
        elif cuv[i] not in cuv2:
            user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
        else:
            user_sol = user_sol[:i] + "-" + user_sol[i + 1:]
        
        for i in range(5):
            if user_sol[i] == "-" and D1[cuv[i]] != 0:
                user_sol = user_sol[:i] + "1" + user_sol[i + 1:]
                D1[cuv[i]] -= 1
            elif user_sol[i] == "-":
                user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
    nr = 0
    for i in range(4, -1, -1):
        nr += (3 ** (4 - i)) * (ord(user_sol[i]) - ord('0'))
    return nr 

#adaugam cuvintele intr-o lista
for x in f:
    L.append(x.strip(" \n"))#eliminam ENTER-ul de la finalul sirurilor de caractere
f.close()

#pastram pt fiecare cuvant de cate ori apare fiecare litera
DICT = {}
for cuv in L:
    DICT[cuv] = {k:cuv.count(k) for k in cuv}

#formam matricea de patterns
cnt = 0
for cuv in L:
    linie = ""
    M.append([fdbk(cuv, cuv2) for cuv2 in L])
    for element in M[cnt]:
        linie += " " + str(element)
    g.write(str(cnt))
    g.write(linie)
    g.write('\n')
    cnt += 1

g.close()