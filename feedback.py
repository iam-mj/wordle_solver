
def feed(guess, word, List, Dict):
    
    user_sol = "00000"

    D1 = {}
    D1 = Dict.copy()
    D2 = {k : guess.count(k) for k in guess}

    if guess in List and len(guess) == 5: 
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
    
        print(user_sol)