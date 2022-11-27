"""
        Pentru optiunea 1 programul alege pe rand fiecare cuvant din baza de date
    si determina numarul optim de incercari (si care ar fi acestea) pentru care 
    cuvantul este ghicit. Respectivele incercari sunt scrise pe cate o linie a 
    fisierului "solutii.txt", iar numarul mediu de incercari pentru ghicirea 
    tuturor cuvintelor - 4.3766... - este afisat in terminal la final 
        Pentru optiunea 2 programul alege un cuvant random din baza de date
    si afiseaza incercarile care duc la ghicirea sa in mod optim
        Pentru optiunea 3 programul permite utilizatorului sa testeze algoritmul 
    pentru un cuvant din baza de date introdus de acesta

        Dureaza aproximativ un minut citirea matricii de pattern-uri indiferent 
    de optiunea aleasa si primeste feedback-ul specific jocului de wordle prin 
    functia feed din fisierul "feedback.py"

"""
import math
import random
from feedback import feed

f = open("cuvinte.txt", "r")
mat = open("matrice.txt", "r")
L = []
N = 11454 #numarul de cuvinte din baza de date
LIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def entropie(poz, ok, Dict, valL):
    ENTROPIE = 0
    patterns = [0] * 243
    for j in range(len(L)):
        if ok != True:#daca nu calculam entropia primei incercari
            if j in Dict.keys(): #verifici daca cuvantul este in dictionarul valorilor valide
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

#citim matricea de pattern-uri
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

    D = {k:cuv.count(k) for k in cuv} #dictionarul cu frecventa literelor din cuvantul care trebuie ghicit

    ok = True #verificam daca facem entropia pentru prima incercare, necesar pentru a eficientiza putin timpul
    ok2 = True #verfiicam daca realizam lista de cuvinte valide dupa prima incercare
    valL = L #lista de cuvinte valide
    Dict = {} #dictionarul de cuvinte valide 

    while len(valL) > 1:

        if ok != True:
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

        #stim deja ca primul cuvant este TAREI asa ca il alegem direct pentru a castiga timp
        else:
            cuvmax = "TAREI"
            for i in range(len(L)):
                if L[i] == "TAREI":
                    pozmax = i
            emax = entropie(pozmax, ok, Dict, valL)
            ok = False
        
        #luam in calcul noua incercare
        SOLUTIE += cuvmax + " "
        incercari += 1
        
        #cerem feedback de la wordle
        fd = feed(cuvmax, cuv, L, D)

        if fd != "22222": #reactualizam lista de cuvinte valide doar daca nu am gasit inca cuvantul
            #transformam feedback-ul intr-un int
            nr = 0
            for i in range(4, -1, -1):
                nr += (3 ** (4 - i)) * (ord(fd[i]) - ord('0'))

            Dict_aux = {}
            #actualizam lista si dictionarul de cuvinte valide
            valL = []
            for i in range(len(M[pozmax])):
                if ok2 != True:
                    if i in Dict.keys() and M[pozmax][i] == nr:
                        valL.append(L[i])
                        Dict_aux[i] = 1
                else:
                    if M[pozmax][i] == nr:
                        valL.append(L[i])
                        Dict_aux[i] = 1
            ok2 = False
            Dict = Dict_aux.copy()

        else:#daca am gasit cuvantul cand inca aveam mai multe valori valide
            SOLUTIE += "\n"
            break

    else:#daca gasim cuvantul fiindca am ramas cu o singura optiune valida
        SOLUTIE += valL[0] + "\n"
        incercari += 1

    if optiune == 1:
        g.write(SOLUTIE) 
        return incercari
        
    else:
        print(SOLUTIE[:len(SOLUTIE)])#nu afisam si ENTER-UL

#alegeti ce optiune sa execute algoritmul
optiune = int(input("Pentru a genera fisierul solutii.txt si numarul mediu de incercari alegeti 1, pentru a afisa rezolvarea pentru un cuvant aleatoriu alegeti 2, pentru a afisare rezolvarea pentru un cuvant ales de dumneavoastra alegeti 3: \n"))

#genereaza
if optiune == 1:
    g = open("solutii.txt", "x")
    
    #calculam media
    MEDIE = 0
    for i in range(N):
        MEDIE += rezolv_wordle(L[i])

    print(MEDIE / N)
    g.close()

elif optiune == 2:
    #alegem un cuvant random
    n = random.randint(0, N - 1)
    cuv_random = L[n]
    
    rezolv_wordle(cuv_random)

elif optiune == 3:
    cuv_ales = input("Dati cuvantul de 5 litere din baza de date care sa fie ghicit: ")
    
    if len(cuv_ales) != 5 or cuv_ales not in L:
        print("Eroare =( \n")
    
    else:
        rezolv_wordle(cuv_ales)

else:
    print("Optiune invalida! Incercati din nou. \n")
