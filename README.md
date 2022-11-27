# Proiect_asc-WORDLE
Echipa formată din: *Verdeș Maria-Ioana(grupa 131)* și *Leahu Silvia-Ioana(grupa 131)* 

Primul program, jocul wordle, a fost implementat în trei variante diferite:
- prima, "wordle.py", dispune de o interfață construită cu ajutorul modulului TKINTER
- a doua varianta, "wordleNoGUI.py ",este o variantă simplificată a primului program, care returnează feedback-ul în terminal după următoarele reguli: 0-echivalentul culorii gri din joc, 1-galben, iar 2-verde
- ultima varintă este de fapt o funcție care returnează feedback-ul pe baza regulilor jocului și, doar aceasta a reușit să fie conectată cu "guesser.py"


Al doilea program s-a realizat în doua etape, a doua etapă fiind cea corectă și eficientă(*sperăm):

-**Prima** noastră **variantă** de a calcula entropia, incorectă însă, se află in fișierul "first_guesser.py".Ea se baza pe calcularea probabilității apariției fiecărei literă din alfabet, iar apoi, în functie de asta, a informației oferită de fiecare variantă și implicit, a entropiei.

-**A doua variantă**(cea corectă) se găsește în fișierul "guesser.py" și presupune crearea unei matrici de pattern-uri, cu ajutorul cărora se calculează entropiile. 
  
Primul cuvant, cel cu entropia maximă, de la care ar trebui să pornească programul, este calculat separat în programul "primul_cuvant.py" și furnizat ulterior direct ca prima   incercare in cadrul programului principal "guesser.py".
În fișierul "guesser.py",am creat 3 comenzi, în funcție de cerința "jucătorului", astfel:
 1. Pentru optiunea 1 programul alege pe rand fiecare cuvant din baza de date
    si determina numarul optim de incercari (si care ar fi acestea) pentru care 
    cuvantul este ghicit. Respectivele incercari sunt scrise pe cate o linie a 
    fisierului "solutii.txt", iar *numarul mediu de incercari* pentru ghicirea 
    tuturor cuvintelor **-4.376636982713462-**  este afisat in terminal la final 
 2. Pentru optiunea 2 programul alege un cuvant random din baza de date
    si afiseaza incercarile care duc la ghicirea sa in mod optim
 3. Pentru optiunea 3 programul permite utilizatorului sa testeze algoritmul 
    pentru un cuvant din baza de date introdus de acesta.
 
