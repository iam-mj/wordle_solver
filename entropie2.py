import random
import math
from feedback import feed

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
mat = open("matrice2.txt", "r")
g = open("solutii.txt", "x")
L = []
N = 11454 #numarul de cuvinte din baza de date
LIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def entropie(poz, ok, Dict, valL):
    ENTROPIE = 0
    patterns = [0] * 243
    for j in range(len(L)):
        if ok != 1:
            if j in Dict.keys(): #comentezi asta daca faci pentru TAREI
                patterns[M[poz][j]] += 1
        else:
            patterns[M[poz][j]] += 1
    for i in range(243):
        p = patterns[i] / len(valL)
        if p > 0:
            ENTROPIE += p * (math.log2(1 / p))
    return ENTROPIE   

#adaugam cuvintele intr-o lista
for x in f:
    L.append(x.strip(" \n"))#eliminam ENTER-ul de la finalul sirurilor de caractere
f.close()

#citim matricea
M = []
cnt = 0
for linie in mat:
    if cnt < 11454:
        M.append([int(x.strip("\n")) for x in linie.split()])
        M[cnt].pop(0) #scoatem cnt-ul de pe fiecare linie din fisier
    cnt += 1

def rezolv_wordle(cuv):

    incercari = 0
    SOLUTIE = cuv + " "

    D = {k:cuv.count(k) for k in cuv}

    ok = 1
    ok2 = 1
    valL = L
    Dict = {}

    while len(valL) > 1:

        if ok != 1:
            #calculam cuvantul cu cea mai mare entropie
            emax = 0
            cuvmax = ""
            pozmax = -1
            for i in range(len(L)):
                if L[i] in valL:
                    e = entropie(i, ok, Dict, valL)
                    if e > emax:
                        emax = e
                        cuvmax = L[i]
                        pozmax = i

        #primul cuvant stim deja ca este TAREI asa ca il alegem direct pentru a castiga timp
        else:
            cuvmax = "TAREI"
            for i in range(len(L)):
                if L[i] == "TAREI":
                    pozmax = i
            emax = entropie(pozmax, ok, Dict, valL)
            ok = 0
        
        #trimitem cuvantul cu entropia cea mai mare la wordle
        SOLUTIE += cuvmax + " "
        incercari += 1
        
        #cerem feedback de la wordle
        fd = feed(cuvmax, cuv, L, D)

        if fd != "22222": #reactualizam lista doar in cazul in care nu am gasit inca cuvantul
            #transformam feedback-ul intr-un int
            nr = 0
            for i in range(4, -1, -1):
                nr += (3 ** (4 - i)) * (ord(fd[i]) - ord('0'))

            Dict_aux = {}
            #actualizam lista de cuvinte valide
            valL = []
            for i in range(len(M[pozmax])):
                if ok2 != 1:
                    if i in Dict.keys() and M[pozmax][i] == nr:
                        valL.append(L[i])
                        Dict_aux[i] = 1
                else:
                    if M[pozmax][i] == nr:
                        valL.append(L[i])
                        Dict_aux[i] = 1
            ok2 = 0
            Dict = Dict_aux.copy()

        else:
            SOLUTIE += "\n"
            break

    else:
        SOLUTIE += valL[0] + "\n"
        incercari += 1

    g.write(SOLUTIE)
    return incercari

MEDIE = 0
for i in range(N):
    MEDIE += rezolv_wordle(L[i])
    print(i)

print(MEDIE / N)
g.close()