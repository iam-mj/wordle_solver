import random

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
L = []
N = 11454 #numarul de cuvinte din baza de date

#adaugam cuvintele intr-o lista
for x in f:
    L.append(x.strip(" \n"))#eliminam ENTER-ul de la finalul sirurilor de caractere
f.close()

#alegem un cuvant random
n = random.randint(0, N - 1)
cuv = L[n]
print(cuv)

D = {k:cuv.count(k) for k in cuv}

user_sol = "00000"
ok = 0

while user_sol != "22222":
    
    D1 = {}
    D1 = D.copy()
    print(D1)
    
    #primim incercarea (de la guesser)
    if ok == 0:
        sol = input("dati prima incercare: ")
        ok = 1
    else:
        sol = input("dati urmatoarea incercare: ")

    D2 = {k : sol.count(k) for k in sol}
    print(f"D2 este {D2}")

    for i in range(5):
        if sol[i] == cuv[i]:
            user_sol = user_sol[:i] + "2" + user_sol[i + 1:]
            D1[sol[i]] -= 1
            D2[sol[i]] -= 1
        elif sol[i] not in cuv:
            user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
        else:
            user_sol = user_sol[:i] + "-" + user_sol[i + 1:]
    
    for i in range(5):
        if user_sol[i] == "-" and D1[sol[i]] != 0:
            user_sol = user_sol[:i] + "1" + user_sol[i + 1:]
            D1[sol[i]] -= 1
        elif user_sol[i] == "-":
            user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
    
    """
    LF = {k:cuv.count(k) for k in cuv} #dictionar de frecventa pt literele cuvantului random
    LC = {k:0 for k in cuv}

    #if
        for i in range(len(sol)):
            if sol[i] == cuv[i]:
                user_sol = user_sol[:i] + "2" + user_sol[i + 1:]
                LC[sol[i]] += 1
            elif sol[i] in cuv and LC[sol[i]] < LF[sol[i]]:
                user_sol = user_sol[:i] + "1" + user_sol[i + 1:]
                LC[sol[i]] += 1
            else:
                user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
    """
    #if sol in L and len(sol) == 5: 
        #dam feedback guesser-ului
    print(user_sol)

    #else:
     #   print("ERROR!")

