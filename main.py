import tkinter as tk
from tkinter import PhotoImage

fenetre = tk.Tk()
fenetre.geometry("1000x600")
fenetre.resizable(False, False)
fenetre.configure(bg = "bisque3")
fenetre.title("Solitaire")

class Pile:
    def __init__(self):
        self.p = self.creer_pile_vide()
        
    def creer_pile_vide(self):
        return []
    
    def est_vide(self):
        if self.p == []:
            return True
        else:
            return False
        
    def empiler(self, elem):
        self.p.append(elem)
        
    def depiler(self):
        return self.p.pop()
    
    def sommet(self):
        return self.p[-1]
    
    def taille(self):
        return len(self.p)
    
class File:
    def __init__(self, file = None):
        if file != None:
            self.f = file
        else:
            self.f = self.creer_file_vide()
    
    def creer_file_vide(self):
        return []
    
    def est_vide(self):
        if len(self.f) == 0:
            return True
        else:
            return False
        
    def enfiler(self, elem):
        self.f.append(elem)
    
    def defiler(self):
        return self.f.pop(0)
        
    def tete(self):
        return self.f[0]
        
    def taille(self):
        return len(self.f)

class Carte:
    def __init__(self, couleur, valeur, visible, pile):
        self.couleur = couleur
        self.valeur = valeur
        self.visible = visible # True si la carte est face visible, False si la carte est face cachée
        self.pile = pile # Pile à laquelle la carte appartient

    def afficher_carte(self, x, y):
        global fenetre
        carte_file = "cartes/"+self.valeur+"_"+self.couleur+".gif"
        self.img = PhotoImage(file=carte_file)
        label = tk.Label(fenetre, image = self.img, borderwidth=0)
        label.place(x=x, y=y)

class PileInfos:
    """ Permet de stocker des informations sur une Pile de cartes : 
    - le numéro de la Pile si c'est une Pile du plateau de jeu, None sinon
    - la couleur si c'est une Pile de fondation, None sinon
    """
    def __init__(self, numero, couleur, pile):
        self.numero = numero 
        self.couleur = couleur 
        self.pile = pile

class Jeu:
    def __init__(self, pioche = None):
        self.pioche = File(pioche)
        self.pioche_cartes_sorties = Pile()
        self.carte_cliquee = None # carte qui a été cliquée par le joueur, None si pas de carte cliquée ou déplacement terminé
        self.pile_deplacement = None # Pile temporaire pour stocker les cartes déplacées, None si pas de déplacement en cours
        # création des 7 piles de jeu (qui sont sur le plateau de jeu)
        self.pile_jeu1 = PileInfos(1, None, Pile())
        self.pile_jeu2 = PileInfos(2, None, Pile())
        self.pile_jeu3 = PileInfos(3, None, Pile())
        self.pile_jeu4 = PileInfos(4, None, Pile())
        self.pile_jeu5 = PileInfos(5, None, Pile())
        self.pile_jeu6 = PileInfos(6, None, Pile())
        self.pile_jeu7 = PileInfos(7, None, Pile())
        # création des 4 piles de fondation
        self.pile_couleur_coeur = PileInfos(None, 'coeur', Pile())
        self.pile_couleur_carreau = PileInfos(None, 'carreau', Pile())
        self.pile_couleur_trefle = PileInfos(None, 'trefle', Pile())
        self.pile_couleur_pique = PileInfos(None, 'pique', Pile())
    
    def initialiser_jeu(self):
        # création des cartes
        self.cartes = []
        for couleur in ['coeur', 'carreau', 'trefle', 'pique']:
            for valeur in ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']:
                carte = Carte(couleur, valeur, False, None)
                self.cartes.append(carte)

    def changer_carte_de_pile(self):
        pass

    def verifier_validite_deplacement(self):
        pass

    def verifier_victoire(self):
        pass

    def devoiler_carte_dessus(self):
        pass

    def piocher(self):
        if self.pioche.est_vide():
            self.renfiler_pioche()
        for _ in range(3):
            if self.pioche.est_vide():
                break
            carte = self.pioche.defiler()
            self.pioche_cartes_sorties.empiler(carte)

    def renfiler_pioche(self):
        if self.pioche_cartes_sorties.est_vide():
            return
        else:
            pile_intermediaire = Pile()
            for _ in range(self.pioche_cartes_sorties.taille()):
                carte = self.pioche_cartes_sorties.depiler()
                pile_intermediaire.empiler(carte)
            for _ in range(pile_intermediaire.taille()):
                carte = pile_intermediaire.depiler()
                self.pioche.enfiler(carte)

# vérifier fonctionnement de la pioche
"""jeu = Jeu([3, 1, 5, 8, 9, 14, 23, 12])
for i in range(5):
    jeu.piocher()
    print(jeu.pioche_cartes_sorties.p)"""

# vérifier fonctionnement de l'affichage d'une carte
"""jeu = Jeu()
jeu.initialiser_jeu()
jeu.cartes[0].afficher_carte(100, 100)"""

fenetre.mainloop()