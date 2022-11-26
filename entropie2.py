import random
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

#alegem un cuvant random
n = random.randint(0, N - 1)
cuv = L[n]
print(cuv)

#citim matricea
M = []
cnt = 0
for linie in mat:
    if cnt < 11454:
        M.append([int(x.strip("\n")) for x in linie.split()])
        M[cnt].pop(0) #scoatem cnt-ul de pe fiecare linie din fisier
    print(cnt)
    cnt += 1

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
                print(i)
                e = entropie(i)
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
        emax = entropie(pozmax)
        ok = 0
    
    #trimitem cuvantul cu entropia cea mai mare la wordle
    print(cuvmax) 
    print(emax)

    #cerem feedback de la wordle
    fd = input("Dati feedback-ul: ")

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
    
    print(f"ValL are lungimea: {len(valL)}")

print(f"Cuvantul cautat este {valL[0]}")