import random
import math

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
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


def entropie(poz):
    ENTROPIE = 0
    for pattern in range(243):
        p = 0
        for j in len(L):
            if M[poz][j] == pattern: 
                p += 1
        p = p / len(L)        
        ENTROPIE += p * (math.log2(1 / p))
    return ENTROPIE   

#adaugam cuvintele intr-o lista
for x in f:
    L.append(x.strip(" \n"))#eliminam ENTER-ul de la finalul sirurilor de caractere
f.close()

#alegem un cuvant random
n = random.randint(0, N - 1)
cuv = L[n]
print(cuv)

DICT = {}
for cuv in L:
    DICT[cuv] = {k:cuv.count(k) for k in cuv}

print(fdbk("TAREI", "TAIAI"))

cnt = 0
#formam matricea de patterns
"""
for cuv in L:
    M.append([fdbk(cuv, cuv2) for cuv2 in L])
    if cnt == 0:
        print(M[cnt])
    cnt += 1

#calculam cuvantul cu cea mai mare entropie
emax = 0
cuvmax = ""
for i in len(L):
    e = entropie(i)
    print(L[i], i, sep = " ")
    if e > emax:
        emax = e
        cuvmax = L[i]
  
#trimitem cuvantul cu entropia cea mai mare la wordle
print(cuvmax) 
print(emax)
 """