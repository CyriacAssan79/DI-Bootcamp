# Exercice 1
print("Hello world \n" * 5) #Ici nous multiplions la phrase par 5 avec un caractère de retour ligne pour ne pas que les phrases soient collées

# Exercice 2 
nombre1 = 99 #nombre1 stocke la valeur 99
nombre2 = 8 #nombre2 stocke la valeur 99
exposant = nombre1**3 #exposant est le resultat de 99 exposant 3
resultat = exposant * nombre2 #on multiplie exposant par nombre2 pour trouver le resultat final
print(f"La multiplication de {exposant} par {nombre2} = {resultat}") #On affiche ensuite le resultat avec un petit message

# Exercice 3

5 < 3 #False
3 == 3 #True
3 == "3" #False
"3" > 3 #False
"Hello" == "hello" #False

# Exercice 4
computer_brand = "DELL"
print(f"I have a {computer_brand} computer.")

#Exercice 5

name = "Assan Cyriac" 
age = 24
shoe_size = 41
info = f"Je m'appelle {name}, j'ai {age} ans, et j'ai une pointure de {41}" #info contient toute mes informations avec name, age et pointure grace aux f-strings
print(info)

# Exercice 6
a = 2
b = 4

if a > b :   #On vérifie si 2 > 4, si c'est le cas, on met hello Word
    print ("Hello World")

# Exercice 7
nombre = input('Entrez un nombre : ')
nombre = int(nombre)

if (nombre % 2 == 0) : # On vérifie si le reste de la division est 0
    print(f"Le nombre {nombre} est un nombre pair") #Si c'est le cas on met pair
else :
    print(f"Le nombre {nombre} est un nombre impair") #Si non on met impair


# Exerice 8

mon_nom = "Assan"
nom_utilisateur = input("Entrez votre nom : ")
nom_utilisateur = nom_utilisateur


if mon_nom.lower() == nom_utilisateur.lower() :
    print("Nous avons le même nom")
else :
    print("Nous avons des noms différents")

# Exerice 9

taille = input ("Entrez votre taille (cm) : ")

taille = int(taille)

if taille > 145 : 
    print("Vous êtes assez grands pour monter à cheval")
else :
    print("Vous devez encore grandir pour monter à cheval")