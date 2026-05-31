class Game:
    def __init__(self):
        # Création de la grille du jeu : chaque case vide contient trois espaces.
        self.grille = [
            ["   ", "   ", "   "],
            ["   ", "   ", "   "],
            ["   ", "   ", "   "]
        ]

    def montrer_grille(self):
        # Affiche la grille avec des séparateurs pour mieux visualiser le plateau.
        print()
        for i, ligne in enumerate(self.grille):
            print("|".join(ligne))
            if i < 2:
                print("---+---+---")
        print()

    def start(self):
        # Le joueur X commence toujours la partie.
        joueur = " X "

        # La partie continue tant qu'il reste au moins une case vide.
        while self.case_vide():
            self.montrer_grille()

            print(f"======= TOUR DU JOUEUR {joueur} =======")

            # Le joueur choisit une ligne et une colonne entre 0 et 2.
            ligne = int(input("Entrer le numéro de la ligne : "))
            colonne = int(input("Entrer le numéro de la colonne : "))

            # On vérifie que le coup est valide avant de le placer dans la grille.
            verify = self.verification(ligne, colonne, joueur)

            if verify:
                # Après chaque coup valide, on vérifie si le joueur vient de gagner.
                if self.gagnant(joueur):
                    self.montrer_grille()
                    print(f"Le joueur {joueur} a gagné !")
                    return

                # Changement de joueur : X devient O, et O devient X.
                joueur = " O " if joueur == " X " else " X "

        print("La partie est terminée.")

    def verification(self, ligne, colonne, joueur):
        # Vérifie que les coordonnées sont bien dans les limites de la grille.
        if ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2:
            print("Coordonnées invalides.")
            return False

        # Si la case est vide, on place le symbole du joueur.
        if self.grille[ligne][colonne] == "   ":
            self.grille[ligne][colonne] = joueur
            return True

        # Si la case contient déjà X ou O, le joueur doit rejouer.
        print("Cette case est déjà occupée.")
        return False

    def case_vide(self):
        # Parcourt la grille pour savoir s'il reste au moins une case vide.
        for ligne in self.grille:
            if "   " in ligne:
                return True

        return False

    def gagnant(self, joueur):
        # Vérifie toutes les possibilités de victoire pour le joueur actuel.

        # Lignes
        for ligne in self.grille:
            if ligne == [joueur, joueur, joueur]:
                return True

        # Colonnes
        for i in range(3):
            if (self.grille[0][i] == joueur and
                self.grille[1][i] == joueur and
                self.grille[2][i] == joueur):
                return True

        # Diagonale principale
        if (self.grille[0][0] == joueur and
            self.grille[1][1] == joueur and
            self.grille[2][2] == joueur):
            return True

        # Diagonale secondaire
        if (self.grille[0][2] == joueur and
            self.grille[1][1] == joueur and
            self.grille[2][0] == joueur):
            return True

        return False


game = Game()
game.start()
