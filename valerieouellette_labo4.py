class Jeu:
    
    def __init__(self):
        self.contenu = ""

class JeuCartes(Jeu):

    NOM = "cartes"

    def __init__(self):
        pass

class JeuStategie(Jeu):
    
    NOM = "stategie"

    def __init__(self):
        pass

class JeuRole(Jeu):
    
    NOM = "role"

    def __init__(self):
        pass

class JeuMemoire(Jeu):
    
    NOM = "memoire"

    def __init__(self):
        pass

class JeuDes(Jeu):
    
    NOM = "des"

    def __init__(self):
        pass

class PochettePlastique:
    
    def __init__(self, couleur):
        self.couleur = couleur

class Tournoi:

    def __init__(self):
        self.liste_tournois = []

class Documentation:

    def __init__(self):
        self.description = ""

class LogicielMagasin:
    
    def __init__(self):
        self.inventaire = []