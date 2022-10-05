class Jeu:
    
    def __init__(self):
        self.type = ""
        self.nom = ""
        self.prix = 0

    def __str__(self) -> str:
        return f"{self.type}, {self.nom}, {self.prix}"

class JeuCartes(Jeu):

    def __init__(self):
        super().__init__()
        self.type = "Cartes"
        self.pochette = None
    
    def achat(self):
        couleur_pochette = input("Quel couleur pour la pochette? ")
        self.pochette = PochettePlastique(couleur_pochette)

class CartesClassique(JeuCartes):

    def __init__(self):
        super().__init__()
        self.nom = "Cartes classique"
        self.prix = 10

class JokRUmmy(JeuCartes):

    def __init__(self):
        super().__init__()
        self.nom = "Jok-r-ummy"
        self.prix = 20

class Uno(JeuCartes):

    def __init__(self):
        super().__init__()
        self.nom = "Uno"
        self.prix = 10

class JeuStategie(Jeu):

    def __init__(self):
        super().__init__()
        self.type = "Statégie"

class Echecs(JeuStategie):

    def __init__(self):
        super().__init__()
        self.nom = "Échecs"
        self.prix = 50

class Dames(JeuStategie):

    def __init__(self):
        super().__init__()
        self.nom = "Dames"
        self.prix = 30

class Backgammon(JeuStategie):

    def __init__(self):
        super().__init__()
        self.nom = "Backgammon"
        self.prix = 30

class JeuRole(Jeu):
    
    def __init__(self):
        super().__init__()
        self.type = "Rôle"
        self.documentation = ""

class LoupGarou(JeuRole):

    def __init__(self):
        super().__init__()
        self.nom = "Loup-Garou"
        self.prix = 15
        self.documentation = "https://www.regledujeu.fr/loup-garou-regle/"

class DonjonDragon(JeuRole):

    def __init__(self):
        super().__init__()
        self.nom = "Donjon & Dragon"
        self.prix = 45
        self.documentation = "https://donjonetdragon.fr/wp-content/uploads/2022/03/Donjon-et-dragon-PDF-re%CC%80gles.pdf"

class JeuMemoire(Jeu):

    def __init__(self):
        super().__init__()
        self.type = "Mémoire"

class MemoireEnfant(JeuMemoire):

    def __init__(self):
        super().__init__()
        self.nom = "Mémoire Licornes - enfants"
        self.prix = 15

class MemoireTelecospique(JeuMemoire):

    def __init__(self):
        super().__init__()
        self.nom = "Mémoire télécospique"
        self.prix = 35

class JeuConnaissance(Jeu):

    def __init__(self):
        super().__init__()
        self.type = "Connaissance"

class GeniesenHerbes(JeuConnaissance):

    def __init__(self):
        super().__init__()
        self.nom = "Génies en herbe"
        self.prix = 40

class DefisNature(JeuConnaissance):

    def __init__(self):
        super().__init__()
        self.nom = "Défis Nature"
        self.prix = 20

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

class LogicielMagasin:
    
    def __init__(self):
        self.inventaire = []
        self.inventaire_quantite = {}
        self.telecharger_bd()
        self.quantite_inventaire()
    
    def definitions(self):
        return {
            "Cartes classique" : CartesClassique,
            "Jok-r-ummy" : JokRUmmy,
            "Uno" : Uno,
            "Échecs" : Echecs,
            "Dames" : Dames,
            "Backgammon" : Backgammon,
            "Loup-Garou" : LoupGarou,
            "Donjon & Dragon" : DonjonDragon,
            "Mémoire Licornes - enfants" : MemoireEnfant,
            "Mémoire télécospique" : MemoireTelecospique,
            "Génies en herbe" : GeniesenHerbes,
            "Défis Nature" : DefisNature
        }
    
    def __str__(self) -> str:
        inventaire_str = ""
        for quantite, jeu in self.inventaire_quantite.items():
            inventaire_str += (f"{str(jeu.nom)}:{quantite}\n")
        return inventaire_str
    
    def telecharger_bd(self):
        f = open("data.txt", "r", encoding="utf-8")
        lignes = f.readlines()
        for ligne in lignes:
            ligne = ligne.split(":")
            nom = ligne[0]
            quantite = int(ligne[1])
            dico_jeu = self.definitions()
            for nom_cle in dico_jeu.keys():
                if nom == nom_cle:
                    self.inventaire.append(dico_jeu[nom_cle]())
        f.close()
    
    def quantite_inventaire(self):
        for jeu in self.inventaire:
            if jeu in self.inventaire_quantite:
                self.inventaire_quantite[jeu] += 1
            else:
                self.inventaire_quantite[jeu] = 1
    
    def afficher_jeux(self):
        for jeu in self.inventaire:
            print(str(jeu))


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
                print(self)
            elif choix == "4":
                quitting = True
    