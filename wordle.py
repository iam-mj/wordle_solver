import random
import tkinter as tk

LC = []

f = open("D:\Programare\Python\proiect_asc\cuvinte.txt", "r")
L = []
N = 11454 #numarul de cuvinte din baza de date

#adaugam cuvintele intr-o lista
for x in f:
    L.append(x.strip(" \n"))#eliminam ENTER-ul de la finalul sirurilor de caractere
f.close()

#alegem un cuvant random
n = random.randint(0, N - 1)
#cuv = L[n]
cuv = "TARTA"
print(cuv)

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        #dimenisiuni si titlu fereastra
        self.root.title("Wordle")

        #titlu 
        self.label = tk.Label(self.root, 
                              text = "Let's play Wordle!", 
                              font = ('Calibri', 16)
                            )
        self.label.pack(padx = 10, pady = 10)

        #descriere textbox
        self.description = tk.Label(
                                    self.root, 
                                    text = "Choose a 5-letter word:", 
                                    font = ('Calibri', 14)
                                    )
        self.description.pack(padx = 10, pady = 15)

        #textbox
        self.textbox = tk.Entry(self.root, font = ('Calibri', 14))
        self.textbox.pack(padx = 10, pady = 10)

        self.button = tk.Button(
                                self.root, 
                                text = "ENTER", 
                                command = lambda: [
                                                    self.button.destroy(),
                                                    self.create(self.textbox.get(), 1), 
                                                    self.textbox.destroy()
                                                ]
                                )
        self.button.pack(pady = 10)

        self.root.mainloop()

    def create(self, message, k):
        #show the feedback
        
        self.num = 0#how many letters the player got right
        LF = {k:cuv.count(k) for k in cuv} #dictionar de frecventa pt literele cuvantului random
        LC = {k:0 for k in cuv}

        if len(message) == 5: 

            self.frame = tk.Frame(self.root)
            self.frame.pack()

            for i in range(len(message)):
                if message[i] == cuv[i]:
                    self.button = tk.Button(self.frame, text = message[i], bg = 'green')
                    self.button.pack(side = tk.LEFT, pady = 2)
                    self.num += 1
                    LC[cuv[i]] += 1
                elif message[i] in cuv and LC[cuv[i]] != LF[cuv[i]]:
                    self.button = tk.Button(self.frame, text = message[i], bg = 'yellow')
                    self.button.pack(side = tk.LEFT, pady = 2)
                    LC[cuv[i]] += 1
                else:
                    self.button = tk.Button(self.frame, text = message[i], bg = 'white')
                    self.button.pack(side = tk.LEFT, pady = 2)

        else: #if the word given by the user is not in the DB
            self.lbl = tk.Label(
                            self.root,
                            text = "ERROR!",
                            fg = "red",
                            font = ('Calibri', 14)
                            )
            self.lbl.pack(padx = 10, pady = 10)

        if self.num != 5:
                
            if k == 1:

                #create the new entry
                self.next = tk.Entry(self.root, font = ('Calibri', 14))
                self.next.pack(padx = 10, pady = 10)

                self.btn = tk.Button(
                                    self.root, 
                                    text = "ENTER", 
                                    command = lambda: [
                                                        self.btn.destroy(),
                                                        self.create(self.next.get(), 2), 
                                                        self.next.destroy()
                                                        ]
                                    )
                self.btn.pack(pady = 10)

            else: 

                self.nextnext = tk.Entry(self.root, font = ('Calibri', 14))
                self.nextnext.pack(padx = 10, pady = 10)

                self.btn = tk.Button(
                                    self.root, 
                                    text = "ENTER", 
                                    command = lambda: [
                                                        self.btn.destroy(),
                                                        self.create(self.nextnext.get(), 1), 
                                                        self.nextnext.destroy()
                                                        ]
                                    )
                self.btn.pack(pady = 10)
            
        else:
            self.description.destroy()
                
            self.win = tk.Label(
                                self.root,
                                text = "YOU WON!",
                                bg = "purple"
                                )
            self.win.pack(pady = 10)


MyGUI()