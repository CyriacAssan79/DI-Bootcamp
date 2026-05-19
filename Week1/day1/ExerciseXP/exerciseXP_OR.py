# Exercice 1

# mois = input("Veuillez choisir un moi entre 1 et 12 : ")
# mois = int(mois)

# if mois >=3 and mois <=5 :
#     print("Spring")
# elif mois >=6 and mois <=8 :
#     print("Summer")
# elif mois >= 9 and mois <= 11 :
#     print("Autumn")
# elif mois == 12 or mois == 1 or  mois ==2 :
#     print("Winter")
# else :
#     print(f"Le mois {mois} n'existe pas")

# Exercice 2
# nombre = range(1,21)
# for nb in nombre:
#     print(nb)

# for nb in nombre:
#     if (nb % 2 ==0) :
#         print(nb)

# Exercice 3
# nom = "Assan"

# nom_utilisateur = input("Devinez mon nom : ")

# while nom_utilisateur.lower() != nom.lower() :
#     nom_utilisateur = input("Mauvais nom, essayez encore : ")

# Exerice 4

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# name_user = input("Entrez votre nom : ")

# for name in names :
#     if name == name_user :
#         print(f"L'index appartenant au nom est {names.index(name)}")
#         break;

# Exerice 5
total_nombre = []
# nombre1 = input("Entrez le premier nombre : ")
# nombre2 = input("Entrez le premier nombre : ")
# nombre3 = input("Entrez le premier nombre : ")

# total_nombre.append(int(nombre1))
# total_nombre.append(int(nombre2))
# total_nombre.append(int(nombre3))

# print(f"Le plus grand est {max(total_nombre)}")

#Exerice 6
import random

victoire = 0
defaite = 0

continuer = "Oui"

while continuer.lower() == "oui" :

    nombre_utilisateur = input("Choisissez un nombre entre 1 et 9 : ")
    nombre_utilisateur = int(nombre_utilisateur)

    while nombre_utilisateur < 1 or nombre_utilisateur > 9 :
        nombre_utilisateur = input(f"Le nombre {nombre_utilisateur} n'est pas dans l'intervalle de 1 à 9, réessayez : ")
        nombre_utilisateur = int(nombre_utilisateur)
    
    aleatoire = random.randint(1,9)
    print(f"Nombre tiré {aleatoire}")
    
    if nombre_utilisateur == aleatoire :
        victoire += 1
        print(f"Vous avez trouvé, vous avez gagné")
    else :
        defaite += 1
        print(f"Vous n'avez pas trouvé, vous avez perdu")

    continuer = input("Voulez-vous continuer ? (oui/non) : ")

print(f"Vous avez gagné {victoire} partie(s)")
print(f"Vous avez perdu {defaite} partie(s)")
