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
    if s:
        return s / (5 * N)
    else:
        return 1

def galben(lit, poz):
    s = 0
    for i in range(5):
        if i != poz:
            s += P[lit][i]
    if s:
        return s / (5 * N)
    else:
        return 1

def galben2(lit, poz1, poz2):
    s = 0
    for i in range(5):
        if i != poz1 and i != poz2:
            s += P[lit][i]
    if s:
        return s / (5 * N)
    else:
        return 1

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
        for i in range(5):

            if P[cuvant[i]][i] == 0:
                continue

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

while(len(L) > 1):
    
    #calculam probabilitatea de aparitie a fiecarei litere pe fiecare pozitie
    P = {k:[0, 0, 0, 0, 0] for k in LIT}
    for i in range(len(L)):
        for j in range(5):
            P[L[i][j]][j] += 1
    
    #calculam cuvantul cu cea mai mare entropie
    emax = 0
    cuvmax = ""
    for i in L:
        e = entropie(i)
        if e > emax:
            emax = e
            cuvmax = i

    #trimitem cuvantul cu entropia cea mai mare la wordle
    print(cuvmax) 
    print(emax)
    
    #primim feedback de la wordle
    fd = input("Dati feedback-ul: ")

    #construim un dictionar cu informatia sigura pe care ne-o ofera feedbackul
    D = {}
    for i in range(5):
        if fd[i] == "2":
            if cuvmax[i] in D:
                D[cuvmax[i]][0] += 1
                D[cuvmax[i]].append(i)
            else:
                D[cuvmax[i]] = [1]
                D[cuvmax[i]].append(i)
        elif fd[i] == "1":
            if cuvmax[i] in D:
                D[cuvmax[i]][0] += 1
                D[cuvmax[i]].append(-1)
            else:
                D[cuvmax[i]] = [1]
                D[cuvmax[i]].append(-1)
    
    #facem o noua lista, doar cu acele cuvinte care corespund feedback-ului
    auxL = []

    for cuvant in L:
        valid = 1

        for i in range(5):
            #daca are vreo litera pe care am testat-o deja si nu e
            if cuvant[i] in cuvmax and cuvant[i] not in D:
                valid = 0
                break

        for i in D.keys():
            
            if cuvmax == cuvant:
                valid = 0
                break

            litera = i
            if litera not in cuvant:
                valid = 0
                break
            else:
                #daca nu are litera de destule ori
                if D[litera][0] > cuvant.count(litera):  
                    valid = 0
                    break
                else:
                    for j in range(1, D[litera][0] + 1):
                        if D[litera][j] != -1 and cuvant[D[litera][j]] != litera:
                            valid = 0
                            break

        if valid == 1:
            auxL += [cuvant]

    L = auxL
    print(f"NewL are lungime {len(L)}")

print(f"Cuvantul cautat este {L[0]}")
 