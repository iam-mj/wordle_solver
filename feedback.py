
def feed(guess, word, List):
    
    user_sol = "00000"

    LF = {k:word.count(k) for k in word} #dictionar de frecventa pt literele cuvantului random
    LC = {k:0 for k in word}

    if guess in List and len(guess) == 5: 
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