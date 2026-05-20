# Exerice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = {} #Je déclare mon dictionnaire
my_dict[keys[0]] = values[0] #Dans chaque clé du dictionnaire, j'ajoute la valeur de l'index de key qui sera la nouvelle clé
my_dict[keys[1]] = values[1] #Je fais pareil pour la valeur de chaque clé du dictionnaire, je remplace par la valeur de chaque index de value
my_dict[keys[2]] = values[2]

print(my_dict)

# Exercice 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
continuer = "oui"

while continuer == "oui" : #J'initialise ma boucle et il s'arrête lorsque la variable continuer change de valeur
    nom = input("Entrez votre nom : ")
    age = input("Entrez votre age : ")

    family[nom] = int(age) #J'ajoute chaque personne dans le dictionnaire family avec le nom comme clé et age comme valeur

    continuer = input("Voulez vous continuer ? oui/non : ")

cout_total = 0

for key, value in family.items() : #On parcour le dictionnaire
    if value < 3 : #Si l'age est inférieure à 3 ans, la personne ne paye rien 
        cout_total += 0 
    if 3 <= value <= 12 : #Par contre si la personne à entre 3 et 12 il paye 10$
        cout_total += 10 #on incrétme le prix total par le prix que la personne devait payer
    if value >12 : #ensuite si on fait de même si la personne à plus de 12 ans vec des prix différents
        cout_total += 15

for key, value in family.items() : # on fait ici un recap des personnes qui doivent payer et leurs factures
    if value < 0 :
        print(f'{key} ne paye rien')
    if 3 <= value <= 12 :
        print(f'{key}, vous payez 10$')
    if value >12 :
       print(f"{key}, vous payez 15$")

print(f"Vous payez au total {cout_total} $")

#Exerice 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US": ["pink", "green"]
        }
}

brand["number_stores"] = 2 #on écrase l'ancienne valeur de number_stores pour le remplacer par 2 

print("Les clients de zara payent plusieurs types de vêtements comme : ")
for cloth in brand['type_of_clothes'] : #On affiche les types de vêtement que zara vend
    print(f"les vêtements {cloth}, ", end='')

brand["country_creation"] = "Spain" #on ajoute une nouvelle clé et une nouvelle valeur à brand 

brand["international_competitors"].append("Desigual") #on ajoute une nouvelle valeur dans le tableau contenant international_competitors

del brand["creation_date"] #on supprime la clé creation_date

print(f"Le dernier élément de international_competitors est {brand['international_competitors'][-1]}") # on affiche le dernier élément de la liste de international_competitors

print("Les principaux couleurs aux US sont : ")
print("Les clients de zara payent plusieurs types de vêtements comme : ")
for color in brand["major_color"]["US"] : #on parcourt les couleurs de la liste de US
    print(f"le/la couleur {color}, ", end='')

print(f"\n Il y a {len(brand)} clés") #On affiche le nombre de clé

print(f"Les clés sont :")

for key, value in brand.items() : #On énumère les clés
    print(f"{key}, ", end='')

other_dict = {
    "more_on_zara" :"",
    "creation_date" :"",
    "number_stores" : ""
}

for key, value in other_dict.items() : #on ajoute le tableau other_dict à brand
    brand[key] = value

print(brand)

# Exercice 4
def describe_city(city, country = "Inconnue"): #cette fonction prend 2 paramètres, city obligatoire et country optionnel avec une valeur par défaut de Inconnu
    print(f"{city} est dans {country}")

describe_city("Abidjan", "Côte d'Ivoire") #On appelle la fonction describe_city en lui donnant certains attributs
describe_city("Paris", "France")

#Exerice 5 
import random

def my_function(nombre) : #on déclare une fonction qui va permettre de voir si l'entrée de l'utilisateur est pareil à celle généré
    if 1 <nombre>100: # Si le nombre entré n'est pas compris entre 1 et 100, on sort de boucle
        return
    aleatoire = random.randint(1, 100) #On valeur aléatoire entre 1 et 100 est généré

    if nombre == aleatoire :
        print("Les deux nombres sont identiques")
    else :
        print(f"Les deux nombres ne sont pas identiques.\n Votre nombre est {nombre} et le nombre aléatoire est {aleatoire}") 

my_function(50) #J'appelle ma fonction

# Exerice 6
def make_shirt(size = "large", text= "J'adore python") : #cette fonction décrit un tee-shirt et sa taille
    print(f'The size of the shirt is {size} and the text is {text}.')

make_shirt("large")
make_shirt("medium")
make_shirt(text="Je suis intéressé par ce teeshirt")

# Exerice 7
import random
def get_random_temp(mois): #Cette fonction génère un nombre aléatoire entre -10 et 40 en fonction du mois

    if mois >=3 and mois <=5 : 
        return random.randint(15,29) #le gegré est compris entre 15 et 29 si le mois se trouve entre 3 et 5
    elif mois >=6 and mois <=8 :
        return random.randint(30,40) #le gegré est compris entre 30 et 40 si le mois se trouve entre 6 et 8
    elif mois >= 9 and mois <= 11 :
        return random.randint(6,14) #le gegré est compris entre 6 et 14 si le mois se trouve entre 9 et 11
    elif mois == 12 or mois == 1 or  mois ==2 :
        return random.randint(-10,5)
    else :
        print(f"Le mois {mois} n'existe pas")

def main() :
    mois = input("Veuillez choisir un moi entre 1 et 12 : ")
    mois = int(mois)

    temp = get_random_temp(mois)

    if -10 < temp < 5 : #dans ces condition, en fonction du dégré, on affiche un message
        print(f"{temp} dégré, Brrr, il fait un froid de canard ! Mets des vêtements supplémentaires aujourd'hui")
    if 6 <= temp <14 :
        print(f'{temp} dégré, Il fait assez froid ! N`\'oublie pas ton manteau.')
    if 15 <= temp <= 29 :
        print(f'{temp} dégré, Beau temps')
    if 30 <= temp <= 40 :
        print(f'{temp} dégré, Il fait vraiment chaud ! Reste au frais.')


main()

#Exerice 8

prix = 10 #prix de départ de la pizza
ingredients = []
while True : #cette va servir à récuperer toute les entrées de l'utilisateur
    ingredient = input("Entrez un ingrdient ou 'quit' pour sortir : ")

    if ingredient == 'quit' : #si l'entrée est quit, on sort de la fonction
        break
    ingredients.append(ingredient) #on ajoute chaque entrée saisi à la liste ingredients

for i in ingredients : #pour la commande, on ajoute le prix de la pizza et on le somme avec les prix des ingrédients
    prix += 2.5
print(f"Votre pizza ainsi que les ingrédient coute : {prix} $")