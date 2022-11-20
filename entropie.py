import random
import math

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
L = []
N = 11454 #numarul de cuvinte din baza de date
LIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gri(lit, poz):
    return 1 - galben(lit, poz) - verde(lit, poz)

def gri2(lit, poz, poz2 = -1, poz3 = -1):
    s = 0
    for i in range(5):
        if i != poz and i != poz2 and i != poz3:
            s += N - P[lit][i]
    return s / N

def gri3(lit, poz1, poz2):
    s = 0
    s += N - P[lit][poz1] + N - P[lit][poz2]
    return s / N

def galben(lit, poz, poz2 = -1, poz3 = -1, poz4 = -1):
    s = 0
    for i in range(5):
        if i != poz and i != poz2 and i != poz3 and i != poz4:
            s += P[lit][i]
    return s / N * (1 - P[lit][poz] / N)

"""
def galben2(lit, poz1, poz2):
    s = 0
    for i in range(5):
        if i != poz1 and i != poz2:
            s += P[lit][i]
    return s / N #* (1 - P[lit][poz1] / N - P[lit][poz2] / N)
"""

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

            if len(Dict[cuvant[i]]) == 2:

                ind = i 
                for j in Dict[cuvant[i]]: 
                    ind = ind ^ j #cealalta pozitie pe care se mai gaseste litera in cuvant

                if (LIST[ind] == 1 or LIST[ind] == 2) and LIST[i] == 0:
                    if LIST[ind] == 2:
                        p *= gri2(cuvant[i], ind)
                    else:
                        p *= gri3(cuvant[i], i, ind)

                elif (LIST[i] == 1 or LIST[i] == 2) and LIST[ind] == 0:
                    if LIST[i] == 1:
                        p *= galben(cuvant[i], i, ind)
                    else: 
                        p *= verde(cuvant[i], i)

                elif LIST[ind] == LIST[i]:
                    if LIST[i] == 0 and i < ind:
                        p *= gri(cuvant[i], i)
                    elif LIST[i] == 1 and i < ind:
                        p *= galben(cuvant[i], i, ind) 
                    else:
                        p *= verde(cuvant[i], i)

                elif LIST[i] == 2 and LIST[ind] == 1:
                    p *= verde(cuvant[i], i)

                else:
                    p *= galben(cuvant[i], i, ind) 

            else:
                if LIST[i] == 0:
                        p *= gri(cuvant[i], i)
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


#calculam probabilitatea de aparitie a fiecarei litere
P = {k:[0, 0, 0, 0, 0] for k in LIT}
num = 5 * N #numarul total de litere din fisier
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