#Defi 1

nombre = input('Entrez un nombre : ') # L'utilisateur entre un nombre
nombre = int(nombre) #Vu que la sortie est un string ou chaine de charactere, on le convertit en nombre
taille = input('Entrez une taille de liste : ') #Il définit la taille de la liste/tableau
taille = int(taille) #On convertit la taille aussi en nombre
tableau = []

terminer = 0 # On définit une variable qui va permettre à la boucle de savoir si elle doit s'arrêter ou continuer
nombre_depart = 0 # on définitune valeur de départ 0

while terminer < taille : #On dit à la machine tant que terminer n'est pas encore égale ou supérieure à la taille que l'utilsateur à rentrer, il continue son exécution
    nombre_depart += nombre # a chaque tour de boucle, on addition le nombre de départ précédent et le nombre que l'utilisateur à rentrer 
    tableau.append(nombre_depart) #On ajoute chaque somme obtenue au tableau
    terminer += 1 # On incrémente le nombre départ pour éviter une boucle infinit

print(tableau)

#Défi 2

mot = input('Entrez un mot : ') #On demande à l'utilisateur d'entrée un mot
resultat = "" # On déclare une variable vide qui va contenir le mot

for lettre in mot : #On parcours toutes les lettres du mot/phrase ecrites par l'utilisateur
    if resultat =="" or lettre != resultat[-1] : #On vérife si le resultat est vide ou si la lettre actuelle est différente de la lettre précédente
        resultat += lettre #Si la lettre actuelle est différente de la précédente, on concatène ces lettres dans une seul variable "resultat"

print(f"L'ancienne mot est : {mot} \n") #On affiche le mot ou la phrase précedente sans les lettres doubles qui se suivent
print(f"Le nouveau mot formatter est : {resultat}") #