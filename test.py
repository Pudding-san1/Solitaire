import tkinter as tk

class Jeu:
    def __init__(self):
        pass

    def carte_cliquee(self, event):
        print("Carte cliquée :", event.x, event.y)

fenetre = tk.Tk()
jeu = Jeu()

fenetre.bind("<Button-1>", lambda event: jeu.carte_cliquee(event))

fenetre.mainloop()