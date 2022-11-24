from multiprocessing import Process
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

def feed(guess, word, List):
    
    user_sol = "00000"

    LF = {k:word.count(k) for k in word} #dictionar de frecventa pt literele cuvantului random
    LC = {k:0 for k in word}

    for i in range(len(guess)):
        if guess[i] == word[i]:
            user_sol = user_sol[:i] + "2" + user_sol[i + 1:]
            LC[guess[i]] += 1
        elif guess[i] in word and LC[guess[i]] < LF[guess[i]]:
            user_sol = user_sol[:i] + "1" + user_sol[i + 1:]
            LC[guess[i]] += 1
        else:
            user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
    
    print(user_sol)

sol = input("Dati solutia: ")

if __name__ == '__main__': #i have no idea what this means
    p1 = Process(target = feed, args = (sol, cuv, L))
    p1.start()
    p1.join()

    """
    I AM SOOOO CONFUSED AND DONE ㅠㅠㅠㅠㅠㅠㅠㅠㅠ
    WHY DOES THIS FREEZE :(((((
    """

    print("DONE")