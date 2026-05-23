#Partie II

from game import Game


# Menu principale du jeu, ce message s'affiche quand l'utilisateur entre dans le jeu
def get_user_menu_choice():
    print("**** Bienvenue dans PPC **** \nVeuillez choisir une option : ")
    print("1 - Jouer une nouvelle partie ")
    print("2 - Afficher les scores ")
    print("3 - Quitter ")

    user_choice = input('Choisissez : ') #Il entre son choix et on le retourne
    return user_choice

#La fonction affiche un message de fin, à la fin de la partie ou l'orsque l'utilisateur clique sur "Afficher les scores"
def print_results(results) :
    print('*********** RESULTATS ************** :')
    
    for key,value in results.items() : #On parcours le dictionnaire resultats pour récupérer le nombre de victoire, defaite et match nul
        print(f'Nombres de {key} : {value}')
    print('Mercie pour votre participation')

#Fonction principale du jeu
def main ():
    #Au debut, toutes les clés sont à zero
    results = {
        "victoire": 0,
        "defaite": 0,
        "match_nul": 0
    }

    while True:

        #On récurer la choix de l'utilisateur pour savoir s'il veut jouer, voir ses resultats ou quitté
        user_choice = get_user_menu_choice()

        # jouer 
        if user_choice == "1":

            game = Game()

            result = game.play()

            # on sauvegarde le résultat
            results[result] += 1

        # afficher scores
        elif user_choice == "2":

            print_results(results)

        # quitter
        elif user_choice == "3" or user_choice.lower() == "q":

            print_results(results)
            break

        else:
            print("Choix invalide")
    
main()