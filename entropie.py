import random
import math

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
L = []
N = 11454 #numarul de cuvinte din baza de date
LIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gri(lit):
    return 1 - P[lit]

def galben(lit):
    return P[lit] * (4 / 5)

def verde(lit):
    return P[lit] * (1 / 5)

def entropie(cuvant):
    ENTROPIE = 0
    #toate numerele de la 0 la 243 in baza 3
    cnt = 0
    while cnt < 243:
        #transformam numarul in baza 3
        i = cnt
        LIST50 = [0 for i in range(5)]
        nr = 1 #contorizam impartirile
        while i > 0:
            r = i % 3 # 0 - gri, 1 - galben, 2 - verde
            LIST50[5 - nr] = r
            i = i // 3
            nr += 1
        cnt += 1
        #calculam cata informatie ne ofera fiecare posibil feedback
        p = 1
        for i in range(5):
            if i == 0:
                p *= gri(cuvant[i])
            elif i == 1:
                p *= galben(cuvant[i])
            else: 
                p *= verde(cuvant[i])
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


#calculam probabilitatea de aparitie a fiecarei litere
P = {k:0 for k in LIT}
num = 5 * N #numarul total de litere din fisier
for i in range(len(L)):
    for litera in L[i]:
        P[litera] += 1

for i in LIT:
    P[i] = P[i] / num

emax = 0
cuvmax = ""
for i in L:
    e = entropie(i)
    if e > emax:
        emax = e
        cuvmax = i

print(cuvmax)
print(emax)