import random
import math

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
L = []
N = 11454 #numarul de cuvinte din baza de date
LIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gri(lit):
    s = 0
    for i in range(5):
        s += N - P[lit][i]
    return s / (5 * N)

def galben(lit, poz):
    s = 0
    for i in range(5):
        if i != poz:
            s += P[lit][i]
    return s / (5 * N)

def galben2(lit, poz1, poz2):
    s = 0
    for i in range(5):
        if i != poz1 and i != poz2:
            s += P[lit][i]
    return s / (5 * N)

def verde(lit, poz):
    return P[lit][poz] / N

def entropie(cuvant):

    Dict = {k:[] for k in cuvant}
    for i in range(len(cuvant)):
        Dict[cuvant[i]].append(i)
    ENTROPIE = 0

    #toate numerele de la 0 la 243 in baza 3
    cnt = 0
    while cnt < 243:

        #transformam numarul in baza 3
        i = cnt
        LIST = [0 for i in range(5)]
        nr = 1 #contorizam impartirile
        while i > 0:
            r = i % 3 # 0 - gri, 1 - galben, 2 - verde
            LIST[5 - nr] = r
            i = i // 3
            nr += 1
        cnt += 1

        #calculam cata informatie ne ofera fiecare posibil feedback
        p = 1
        for i in range(len(LIST)):

            #cazurile pentru 2 litere identice
            if len(Dict[cuvant[i]]) == 2:

                ind = i 
                for j in Dict[cuvant[i]]: 
                    ind = ind ^ j #cealalta pozitie pe care se mai gaseste litera in cuvant

                if LIST[i] == 0 and LIST[ind] == 0 and i < ind:
                    p *= gri(cuvant[i])
                elif ((LIST[i] == 0 and LIST[ind] == 1) or (LIST[i] == 1 and LIST[ind] == 0)) and i < ind:
                    p *= galben2(cuvant[i], i, ind)
                elif LIST[i] == 2 and LIST[ind] == 0:
                    p *= verde(cuvant[i], i)
                elif LIST[i] == 1 and LIST[ind] == 1:
                    p *= galben2(cuvant[i], i, ind)
                elif LIST[i] == 1 and LIST[ind] == 2:
                    p *= galben2(cuvant[i], i, ind)
                elif LIST[i] == 2 and LIST[ind] == 1:
                    p *= verde(cuvant[i], i)
                elif LIST[i] == 2 and LIST[ind] == 2:
                    p *= verde(cuvant[i], i)

            else:
                if LIST[i] == 0:
                    p *= gri(cuvant[i])
                elif LIST[i] == 1:
                    p *= galben(cuvant[i], i)
                else: 
                    p *= verde(cuvant[i], i)

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


#calculam probabilitatea de aparitie a fiecarei litere pe fiecare pozitie
P = {k:[0, 0, 0, 0, 0] for k in LIT}
for i in range(len(L)):
    for j in range(5):
        P[L[i][j]][j] += 1

emax = 0
cuvmax = ""
for i in L:
    e = entropie(i)
    if e > emax:
        emax = e
        cuvmax = i
print(cuvmax)
print(emax)
