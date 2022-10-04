class Jeu:

    NOM = ""
    
    def __init__(self):
        self.prix = 0
        self.description = ""

    def __str__(self) -> str:
        return f"{Jeu.NOM}, {self.description}, {self.prix}"

class JeuCartes(Jeu):

    NOM = "cartes"

    def __init__(self):
        super().__init__()
        self.prix = 10
        self.description = "Jeu de 54 cartes classique"
        self.pochette = PochettePlastique()
    
    def achat(self):
        couleur_pochette = input("Quel couleur pour la pochette? ")
        self.pochette.couleur = couleur_pochette

class JokRUmmy(JeuCartes):

    NOM = "jok-r-ummy"

    def __init__(self):
        super().__init__()
        self.prix = 20
        self.description = "Nouvelle édition"

class JeuStategie(Jeu):
    
    NOM = "stategie"

    def __init__(self):
        super().__init__()

class Echecs(JeuStategie):

    NOM = "echecs"

    def __init__(self):
        super().__init__()
        self.prix = 50
        self.description = "Jeu d'échecs en bois"

class Monopoly(JeuStategie):

    NOM = "monopoly"

    def __init__(self):
        super().__init__()
        self.prix = 30
        self.description = "Jeu Monopoly Monde"

class JeuRole(Jeu):
    
    NOM = "role"

    def __init__(self):
        super().__init__()

class LoupsGarous(JeuRole):

    NOM = "loups-garous"

    def __init__(self):
        super().__init__()
        self.prix = 15
        self.description = "Édition spécial"

class DonjonDragon(JeuRole):

    NOM = "donjon-dragon"

    def __init__(self):
        super().__init__()
        self.prix = 20
        self.description = "Jeu classique de donjon et dragon"

class JeuMemoire(Jeu):
    
    NOM = "memoire"

    def __init__(self):
        super().__init__()
        self.prix = 15
        self.description = "Jeu de mémoire pour les 8 ans et plus"

class JeuDes(Jeu):
    
    NOM = "des"

    def __init__(self):
        super().__init__()
        self.prix = 10
        self.description = "Ensemble de dés à jouer"

class PochettePlastique:
    
    def __init__(self, couleur):
        self.couleur = couleur

class Tournoi:

    LISTE_TOURNOIS = []

    def __init__(self, nom, date):
        self.nom = nom
        self.date = date
        self.participants = []
    
    def __str__(self) -> str:
        return f"{self.nom}: {self.date}"
    
    @staticmethod
    def inscription_tournoi():
        nom = input("Entrez votre nom: ")
        courriel = input("Entrez votre courriel: ")
        if len(Tournoi.LISTE_TOURNOIS) == 0:
            tournoi = Tournoi()
            Tournoi.LISTE_TOURNOIS.append(tournoi)
            tournoi.participants.append((nom, courriel))
        else:
            pass


class Documentation:

    def __init__(self):
        self.description = ""

class LogicielMagasin:
    
    def __init__(self):
        self.inventaire = []
        self.inventaire_quantite = {}
        self.telecharger_bd()
        self.quantite_inventaire()
    
    def __str__(self) -> str:
        str_inventaire = ""
        for jeu in self.inventaire:
            str_inventaire += str(jeu) + "\n"
    
    def telecharger_bd(self):
        f = open("data.txt", "r", encoding="utf-8")
        lignes = f.readlines()
        for ligne in lignes:
            ligne = ligne.split(",")
            nom = ligne[0]
            if nom == "cartes":
                self.inventaire.append(JeuCartes())
            elif nom == "stategie":
                self.inventaire.append(JeuStategie())
            elif nom == "role":
                self.inventaire.append(JeuRole())
            elif nom == "memoire":
                self.inventaire.append(JeuMemoire())
            elif nom == "des":
                self.inventaire.append(JeuDes())
        f.close()
    
    def quantite_inventaire(self):
        for jeu in self.inventaire:
            if jeu in self.inventaire_quantite:
                self.inventaire_quantite[jeu] += 1
            else:
                self.inventaire_quantite[jeu] = 1
    
    def afficher_inventaire(self):
        for quantite, jeu in self.inventaire_quantite.items():
            print(f"{quantite} {str(jeu)}")


    def menu(self):
        menu = {}
        menu[1] = "Effectuer une vente."
        menu[2] = "Effectuer un retour."
        menu[3] = "Afficher l'inventaire."
        menu[4] = "Quitter"

        quitting = False
        while not quitting:
            for numero, option in menu.items():
                print(f"{numero}) {option}")
            
            choix = input("Votre choix: ")
            if choix == "1":
                pass
            elif choix == "2":
                pass
            elif choix == "3":
                self.afficher_inventaire()
            elif choix == "4":
                quitting = True
    