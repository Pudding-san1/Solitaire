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
    def __init__(self):
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
        self.f.pop(0)
        
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
    def __init__(self):

        self.pioche = File()
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
        pass

    def changer_carte_de_pile(self):
        pass

    def verifier_validite_deplacement(self):
        pass

    def verifier_victoire(self):
        pass

    def devoiler_carte_dessus(self):
        pass

    def piocher(self):
        pass

    def rempiler_pioche(self):
        pass