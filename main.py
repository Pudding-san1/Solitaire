import tkinter as tk
from tkinter import PhotoImage

fenetre = tk.Tk()
fenetre.geometry("1000x600")
fenetre.resizable(False, False)
fenetre.configure(bg = "bisque3")
fenetre.title("Solitaire")
fenetre.attributes('-topmost', 1)

class Pile:
    def __init__(self) -> None:
        self.p = self.creer_pile_vide()
        
    def creer_pile_vide(self) -> list:
        return []
    
    def est_vide(self) -> bool:
        if self.p == []:
            return True
        else:
            return False
        
    def empiler(self, elem) -> None:
        self.p.append(elem)
        
    def depiler(self) -> any:
        return self.p.pop()
    
    def sommet(self) -> any:
        return self.p[-1]
    
    def taille(self) -> int:
        return len(self.p)
    
class File:

    def __init__(self, file: list = None) -> None:
        if file != None:
            self.f = file
        else:
            self.f = self.creer_file_vide()
    
    def creer_file_vide(self) -> list:
        return []
    
    def est_vide(self) -> bool:
        if len(self.f) == 0:
            return True
        else:
            return False
        
    def enfiler(self, elem) -> None:
        self.f.append(elem)
    
    def defiler(self) -> any:
        return self.f.pop(0)
        
    def tete(self) -> any:
        return self.f[0]
        
    def taille(self) -> int:
        return len(self.f)

class Carte:
    def __init__(self, couleur:str, valeur:int, visible: bool, pile: Pile, x:int = None, y:int = None) -> None:
        self.couleur: str = couleur
        self.valeur: int = valeur
        self.visible: bool = visible # True si la carte est face visible, False si la carte est face cachée
        self.pile: Pile = pile # Pile à laquelle la carte appartient
        self.label = tk.Label(fenetre, borderwidth=0)
        self.x = x
        self.y = y

    def placer_carte(self, x: int = None, y: int = None) -> None:
        """ Change la position de la carte sur la fenêtre """
        if x == None and y == None:
            return
        elif x == None:
            self.label.place_configure(y=y)
            self.y = y
        elif y == None:
            self.label.place_configure(x=x)
            self.x = x
        else:
            self.label.place(x=x, y=y)
            self.x = x
            self.y = y

    def changer_visibilite_image(self, x: int = None, y: int = None) -> None:
        if self.visible == True:
            self.img = PhotoImage(file="cartes/face_cachee.png")
            self.visible = False
        else:
            self.img = PhotoImage(file="cartes/"+self.valeur+"_"+self.couleur+".gif")
            self.visible = True
        self.label.configure(image=self.img)
        self.placer_carte(x, y)

class PileInfos:
    """ Permet de stocker des informations sur une Pile de cartes : 
    - le numéro de la Pile si c'est une Pile du plateau de jeu, None sinon
    - la couleur si c'est une Pile de fondation, None sinon
    """
    def __init__(self, numero: int, couleur:str, pile: Pile, x: int) -> None:
        self.numero: int = numero 
        self.couleur: str = couleur 
        self.pile: Pile = pile
        self.x = x

class Jeu:
    def __init__(self, pioche: list = None):
        self.pioche: File = File(pioche)
        self.pioche_cartes_sorties: Pile = Pile()
        self.carte_cliquee = None # carte qui a été cliquée par le joueur, None si pas de carte cliquée ou déplacement terminé
        self.pile_deplacement = None # Pile temporaire pour stocker les cartes déplacées, None si pas de déplacement en cours
        # création des 7 piles de jeu (qui sont sur le plateau de jeu)
        self.pile_jeu1 = PileInfos(1, None, Pile(), 10)
        self.pile_jeu2 = PileInfos(2, None, Pile(), 150)
        self.pile_jeu3 = PileInfos(3, None, Pile(), 290)
        self.pile_jeu4 = PileInfos(4, None, Pile(), 430)
        self.pile_jeu5 = PileInfos(5, None, Pile(), 570)
        self.pile_jeu6 = PileInfos(6, None, Pile(), 710)
        self.pile_jeu7 = PileInfos(7, None, Pile(), 850)
        self.liste_pile = [self.pile_jeu1, self.pile_jeu2, self.pile_jeu3, self.pile_jeu4, self.pile_jeu5, self.pile_jeu6, self.pile_jeu7]
        # création des 4 piles de fondation
        """self.pile_couleur_coeur: PileInfos = PileInfos(None, 'coeur', Pile())
        self.pile_couleur_carreau: PileInfos = PileInfos(None, 'carreau', Pile())
        self.pile_couleur_trefle: PileInfos = PileInfos(None, 'trefle', Pile())
        self.pile_couleur_pique: PileInfos = PileInfos(None, 'pique', Pile())"""
    
    def initialiser_jeu(self) -> None:
        # création des cartes
        self.cartes = []
        for couleur in ['coeur', 'carreau', 'trefle', 'pique']:
            for valeur in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
                carte = Carte(couleur, valeur, False, None)
                self.cartes.append(carte)

    def changer_carte_de_pile(self):
        pass

    def determiner_carte_cliquee(self, event):
        x = event.x_root - fenetre.winfo_rootx()
        y = event.y_root - fenetre.winfo_rooty()
        coordonnees = (x, y)
        pile_cliquee = None
        carte_cliquee = None
        for pile in self.liste_pile:
            if pile.pile.est_vide():
                continue
            sommet = pile.pile.sommet()
            label = sommet.label
            x0 = label.winfo_x()
            x1 = x0 + label.winfo_width()
            if x0 < coordonnees[0] < x1:
                pile_cliquee = pile.pile
                break

        if pile_cliquee == None:
            pile_cliquee = self.pioche_cartes_sorties # si ce n'est aucune des piles de jeu, c'est forcément une carte de celles sorties de la pioche

        pile_intermediaire = Pile()
        for _ in range(pile_cliquee.taille()):
            carte = pile_cliquee.sommet()
            label = carte.label
            if pile_cliquee != self.pioche_cartes_sorties:
                coor0 = label.winfo_y()
                coor1 = coor0 + label.winfo_height()
                coor_clic = coordonnees[1]
            else:
                coor0 = label.winfo_x()
                coor1 = coor0 + label.winfo_height()
                coor_clic = coordonnees[0]
            if coor0 < coor_clic < coor1 and carte.visible:
                carte_cliquee = carte
                break
            else:
                pile_intermediaire.empiler(pile_cliquee.depiler())

        for _ in range(pile_intermediaire.taille()):
            pile_cliquee.empiler(pile_intermediaire.depiler())

        self.carte_cliquee = carte_cliquee
        if carte_cliquee != None:
            print("Carte cliquée :", carte_cliquee.couleur, carte_cliquee.valeur)
        return carte_cliquee

    def verifier_validite_deplacement(self):
        pass

    def verifier_victoire(self):
        pass

    def devoiler_carte_dessus(self):
        pass

    def piocher(self) -> None:
        if self.pioche.est_vide():
            self.renfiler_pioche()
        x = 10
        for _ in range(3):
            if self.pioche.est_vide():
                break
            carte = self.pioche.defiler()
            self.pioche_cartes_sorties.empiler(carte)
            carte.changer_visibilite_image(x, 10)
            x += 40

    def renfiler_pioche(self) -> None:
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

# vérifier fonctionnement de l'affichage des cartes
jeu = Jeu()
jeu.initialiser_jeu()
"""jeu.cartes[0].changer_visibilite_image(100, 100)
jeu.cartes[1].changer_visibilite_image(100, 140)
jeu.cartes[2].changer_visibilite_image(100, 180)
jeu.pile_jeu1.pile.empiler(jeu.cartes[0])
jeu.pile_jeu1.pile.empiler(jeu.cartes[1])
jeu.pile_jeu1.pile.empiler(jeu.cartes[2])"""
jeu.pioche.f = [jeu.cartes[i] for i in range(3, 10)]
jeu.piocher()

fenetre.bind("<Button-1>", lambda event: jeu.determiner_carte_cliquee(event))
fenetre.mainloop()