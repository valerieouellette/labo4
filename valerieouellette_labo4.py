from datetime import datetime, timedelta
from random import randint


class Jeu:
    
    def __init__(self, inventaire):
        self.type = ""
        self.nom = ""
        self.prix = 0
        self.inventaire = inventaire

    def __str__(self) -> str:
        return f"Type: {self.type}, Nom: {self.nom}, Prix: {self.prix}$, Inventaire: {self.inventaire}"
    
    def achat(self):
        pass

class JeuCartes(Jeu):

    def __init__(self, inventaire):
        super().__init__(inventaire)
        self.type = "Cartes"
        self.pochette = None
    
    def achat(self, inventaire_magasin):
        choix = False
        while not choix:
            print("Quelle couleur voulez-vous pour la pochette?")
            print("1) Rouge \n2) Bleu")
            choix_couleur = input("Votre choix(1-2): ")
            if choix_couleur == "1":
                choix_couleur = "rouge"
                choix = True
            elif choix_couleur == "2":
                choix_couleur = "bleu"
                choix = True
            else:
                print("Choix invalide.")

        for article in inventaire_magasin:
            if article.nom == "Pochette plastique" and article.couleur == choix_couleur:
                if article.inventaire > 0:
                    article.inventaire -= 1
                else:
                    print("Malheureusement, il ne nous reste plus de pochette plastique.")


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
        self.nom = ""
        self.type = "Statégie"
    
    def achat(self):
        choix = input("Si vous voulez vous inscrire à un tournoi, tapez 'y': ")
        if choix == "y":
            tournoi = Tournoi.inscription_tournoi(self.nom)
            date_tournoi = tournoi.date.strftime("%d/%m/%Y") + " 19:00"
            print(f"La date du tournoi est: {date_tournoi}")
        else:
            print("Aucune inscription faite.")


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
    
    def achat(self):
        print(f"Ici le lien vers la documentation: {self.documentation}")

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
    
    def __init__(self, couleur, inventaire):
        self.nom = "Pochette plastique"
        self.couleur = couleur
        self.inventaire = inventaire
    
    def __str__(self) -> str:
        return f"Nom: {self.nom}, Couleur: {self.couleur}, Inventaire: {self.inventaire}"

class Tournoi:

    LISTE_TOURNOIS = []

    def __init__(self, nom, date):
        self.nom = nom
        self.date = date
        self.participants = []
    
    def __str__(self) -> str:
        return f"{self.nom}: {self.date}"
    
    @staticmethod
    def inscription_tournoi(nom_jeu):
        nom_participant = input("Entrez votre nom: ")
        courriel = input("Entrez votre courriel: ")

        liste_noms_tournois = []
        for tournoi in Tournoi.LISTE_TOURNOIS:
            liste_noms_tournois.append(tournoi.nom)
        
        if nom_jeu not in liste_noms_tournois:
            date = Tournoi.random_date()
            tournoi = Tournoi(nom_jeu, date)
            Tournoi.LISTE_TOURNOIS.append(tournoi)
            tournoi.participants.append((nom_participant, courriel))
            return tournoi
        else:
            for tournoi in Tournoi.LISTE_TOURNOIS:  
                if tournoi.nom == nom_jeu:
                    tournoi.participants.append((nom_participant, courriel))
                    return tournoi

    @staticmethod
    def random_date():
        today = datetime.now()
        nb_jour = randint(1,30)
        jour_tournoi = today + timedelta(hours=(24*nb_jour), minutes=0)
        return jour_tournoi

class LogicielMagasin:
    
    def __init__(self):
        self.inventaire = []
        self.dico_jeux = self.definitions()
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
            "Défis Nature" : DefisNature,
            "Pochette plastique" : PochettePlastique
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
            if nom == "Pochette plastique":
                couleur = ligne[1]
                quantite = int(ligne[2])
                self.inventaire.append(self.dico_jeux[nom](couleur, quantite))
            else:
                quantite = int(ligne[1])
                for nom_cle in self.dico_jeux.keys():
                    if nom == nom_cle:
                        self.inventaire.append(self.dico_jeux[nom_cle](quantite))
        f.close()
    
    def ecrire_bd(self):
        str_bd_jeu = ""
        for article in self.inventaire:
            if article.nom == "Pochette plastique":
                str_bd_jeu += f"{article.nom}:{article.couleur}:{article.inventaire}\n"
            else:
                str_bd_jeu += f"{article.nom}:{article.inventaire}\n"
        f = open("data.txt", "w", encoding="utf-8")
        f.write(str_bd_jeu)
        f.close()
    

    def vente(self):
        for numero, jeu in enumerate(self.inventaire):
            if jeu.nom != "Pochette plastique":
                print(f"{numero+1}) {jeu}")
        
        choix_vente = int(input(f"Article de la vente(1-{len(self.inventaire)-2}): "))
        quantite_vendu = int(input("Quantité vendu: "))

        jeu_vente = self.inventaire[choix_vente-1]
        if jeu_vente.inventaire >= quantite_vendu:
            jeu_vente.inventaire -= quantite_vendu
            if jeu_vente.type == "Cartes":
                jeu_vente.achat(self.inventaire)
            else:
                jeu_vente.achat()
            print("Vente réussie")
        else:
            print("Impossible, inventaire insuffisant")


    def retour(self):
        for numero, jeu in enumerate(self.inventaire):
            print(f"{numero+1}) {jeu}")
        
        choix_retour = int(input(f"Article à retourner(1-{len(self.inventaire)}): "))
        quantite_retour = int(input("Quantité retournée: "))

        jeu_retour = self.inventaire[choix_retour-1]
        jeu_retour.inventaire += quantite_retour
        print("Retour réussi")


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
