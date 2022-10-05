class Jeu:
    
    def __init__(self, inventaire):
        self.type = ""
        self.nom = ""
        self.prix = 0
        self.inventaire = inventaire

    def __str__(self) -> str:
        return f"Type: {self.type}, Nom: {self.nom}, Prix: {self.prix}$, Inventaire: {self.inventaire}"

class JeuCartes(Jeu):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.type = "Cartes"
        self.pochette = None
    
    def achat(self):
        couleur_pochette = input("Quel couleur pour la pochette? ")
        self.pochette = PochettePlastique(couleur_pochette)

class CartesClassique(JeuCartes):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Cartes classique"
        self.prix = 10

class JokRUmmy(JeuCartes):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Jok-r-ummy"
        self.prix = 20

class Uno(JeuCartes):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Uno"
        self.prix = 10

class JeuStategie(Jeu):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.type = "Statégie"

class Echecs(JeuStategie):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Échecs"
        self.prix = 50

class Dames(JeuStategie):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Dames"
        self.prix = 30

class Backgammon(JeuStategie):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Backgammon"
        self.prix = 30

class JeuRole(Jeu):
    
    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.type = "Rôle"
        self.documentation = ""

class LoupGarou(JeuRole):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Loup-Garou"
        self.prix = 15
        self.documentation = "https://www.regledujeu.fr/loup-garou-regle/"

class DonjonDragon(JeuRole):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Donjon & Dragon"
        self.prix = 45
        self.documentation = "https://donjonetdragon.fr/wp-content/uploads/2022/03/Donjon-et-dragon-PDF-re%CC%80gles.pdf"

class JeuMemoire(Jeu):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.type = "Mémoire"

class MemoireEnfant(JeuMemoire):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Mémoire Licornes - enfants"
        self.prix = 15

class MemoireTelecospique(JeuMemoire):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Mémoire télécospique"
        self.prix = 35

class JeuConnaissance(Jeu):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.type = "Connaissance"

class GeniesenHerbes(JeuConnaissance):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.nom = "Génies en herbe"
        self.prix = 40

class DefisNature(JeuConnaissance):

    def __init__(self, inventaire):
        super().__init__(inventaire)
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
        self.telecharger_bd()
    
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
        for jeu in self.inventaire:
            inventaire_str += str(jeu) + "\n"
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
                    self.inventaire.append(dico_jeu[nom_cle](quantite))
        f.close()
    
    def ecrire_bd(self):
        str_bd_jeu = ""
        for jeu in self.inventaire:
            str_bd_jeu += f"{jeu.nom}:{jeu.inventaire}\n"
        f = open("data.txt", "w", encoding="utf-8")
        f.write(str_bd_jeu)
        f.close()
    

    def vente(self):
        for numero, jeu in enumerate(self.inventaire):
            print(f"{numero+1}) {jeu}")
        
        choix_vente = int(input(f"Article de la vente(1-{len(self.inventaire)}): "))
        quantite_vendu = int(input("Quantité vendu: "))

        jeu = self.inventaire[choix_vente-1]
        if jeu.inventaire >= quantite_vendu:
            jeu.inventaire -= quantite_vendu
            print("Vente réussie")
        else:
            print("Impossible, inventaire insuffisant")

    def retour(self):
        pass

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
                self.vente()
            elif choix == "2":
                self.retour()
            elif choix == "3":
                print(self)
            elif choix == "4":
                self.ecrire_bd()
                quitting = True

logiciel = LogicielMagasin()
logiciel.menu()