"""
        Am ales sa generam o singura data matricea de pattern-uri si sa o scriem 
    in fisierul "matrice.txt" pentru a eficientiza considerabil timpul de executie.
    Citirea acesteia din fisier este esentiala algoritmului de calcul al entropiei.

"""

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
g = open("matrice2.txt", "x")
L = []
N = 11454 #numarul de cuvinte din baza de date
LIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

M = []

#determinam feedback-ul oferit de wordle atunci cand compara cuv si cuv2, 
#cuv reprezentand incercarea, iar cuv2 cuvantul care trebuie gasit 
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
    
    #consideram pattern-ul un numar in baza zece si ii adaugam in matrice echivalentul in baza 10
    nr = 0
    for i in range(4, -1, -1):
        nr += (3 ** (4 - i)) * (ord(user_sol[i]) - ord('0'))
    return nr 

#adaugam cuvintele intr-o lista
for x in f:
    L.append(x.strip(" \n"))#eliminam ENTER-ul de la finalul sirurilor de caractere
f.close()

#pastram pt fiecare cuvant de cate ori apare fiecare litera pt a calcula mai usor feedback-ul
DICT = {}
for cuv in L:
    DICT[cuv] = {k:cuv.count(k) for k in cuv}

#formam matricea de pattern-uri
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