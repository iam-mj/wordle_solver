"""
        Pentru eficientizarea timpului de executie, am ales sa calculam o singura 
    data primul cuvant optim, urmand ca acesta sa fie furnizat direct ca prima 
    incercare in cadrul programului principal "guesser.py"

"""
import math

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
mat = open("matrice.txt", "r")
L = []
N = 11454 #numarul de cuvinte din baza de date
LIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def entropie(poz):
    ENTROPIE = 0
    patterns = [0] * 243
    for j in range(len(L)):
        patterns[M[poz][j]] += 1
    for i in range(243):
        p = patterns[i] / N
        if p > 0:
            ENTROPIE += p * (math.log2(1 / p))
    return ENTROPIE 

#adaugam cuvintele intr-o lista
for x in f:
    L.append(x.strip(" \n"))#eliminam ENTER-ul de la finalul sirurilor de caractere
f.close()

#citim matricea de pattern-uri
M = []
cnt = 0
for linie in mat:
    if cnt < 11454:
        M.append([int(x.strip("\n")) for x in linie.split()])
        M[cnt].pop(0) #scoatem cnt-ul de pe fiecare linie din fisier
    cnt += 1
            
#calculam cuvantul cu cea mai mare entropie
emax = 0
cuvmax = ""
pozmax = -1
for i in range(len(L)):
    e = entropie(i)
    if e > emax:
        emax = e
        cuvmax = L[i]
        pozmax = i

print(f"Primul cuvant optim este {cuvmax}, avand entropia {emax}")
