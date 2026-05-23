#Partie I

import random

#Class Game pour la logique du jeu 
class Game :
    def __init__(self):
        pass

    def get_user_item(self):
        continuer = "oui"

        #On boucle ici pour récupérer le choix de l'utilisateur et on vérifie qu'il que son choix écrit n'est pas différent de pierre, fueuille ou ciseaux
        while continuer == "oui" :
            user_select = input("Ecrivez entre pierre, feuille et ciseaux : ")
            if user_select =="pierre" or user_select =="feuille" or user_select == "ciseaux" :
                return user_select
            
    #On récupère le choix de l'odinateur et on le retourne
    def get_computer_item(self): 
        items = ["pierre","feuille","ciseaux"]
        computer_select = random.choice(items)
        return computer_select

    #On construit ici la logique du jeu logique, à quelle moment l'utlisateur gagne, perd ou fait match nul
    def get_game_result(self, user_item, computer_item) :
        if user_item == computer_item :
            return 'match_nul'
        elif user_item == "pierre" and computer_item == "ciseaux":
            return 'victoire'
        elif user_item == "pierre" and computer_item == "feuille":
            return 'defaite'
        elif user_item == "feuille" and computer_item == "pierre":
            return 'victoire'
        elif user_item == "feuille" and computer_item == "ciseaux":
            return 'defaite'
        elif user_item == "ciseaux" and computer_item == "pierre":
            return 'defaite'
        elif user_item == "ciseaux" and computer_item == "feuille":
            return 'victoire'

    #On renvoie le resultat de la partie: victoire, défaite ou match null
    def play(self): 
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()

        result = self.get_game_result(user_choice,computer_choice)

        if result == 'match_nul':
            print(f'Vous avez choisi {user_choice}. L’ordinateur a choisi {computer_choice}. Vous avez fait match nul ! ')
            return result
        if result == 'defaite' :
            print(f'Vous avez choisi {user_choice}. L’ordinateur a choisi {computer_choice}. Vous avez perdu')
            return result
        if result == 'victoire' :
            print(f'Vous avez choisi {user_choice}. L’ordinateur a choisi {computer_choice}. Vous avez gagné')
            return result
        