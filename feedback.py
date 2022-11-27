"""
        Functia de feedback utilizeaza aceleasi reguli ca jocul Wordle,
    dar returneaza un string de lungime 5 format din 0, 1, si 2 bazat
    pe urmatoarele echivalente:
        0 = litera de pe pozitia respectiva este intoarsa cu un fundal 
            alb / gri
        1 = litera de pe pozitia respectiva este intoarsa cu un fundal
            galben
        2 = litera de pe pozitia respectiva este intoarsa cu un fundal 
            verde

"""
def feed(guess, word, List, Dict):
    
    user_sol = "00000"

    D1 = {}
    D1 = Dict.copy()
    D2 = {k : guess.count(k) for k in guess}

    for i in range(5):
        if guess[i] == word[i]:
            user_sol = user_sol[:i] + "2" + user_sol[i + 1:]
            D1[guess[i]] -= 1
            D2[guess[i]] -= 1
        elif guess[i] not in word:
            user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
        else:
            user_sol = user_sol[:i] + "-" + user_sol[i + 1:]
        
    for i in range(5):
        if user_sol[i] == "-" and D1[guess[i]] != 0:
            user_sol = user_sol[:i] + "1" + user_sol[i + 1:]
            D1[guess[i]] -= 1
        elif user_sol[i] == "-":
            user_sol = user_sol[:i] + "0" + user_sol[i + 1:]
    
    return user_sol