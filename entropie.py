import random

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
L = []
N = 11454 #numarul de cuvinte din baza de date
LIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

print(P)

