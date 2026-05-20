#Exerice 1

3 <= 3 < 9 #True
3 == 3 == 3 # True
bool(0) #False
bool(5 == "5") #False
bool(4 == 4) == bool("4" == "4") #True
bool(bool(None)) #False

x = (1 == True) # en python 1 est égale à True et 0 est égale à false, donc ici c'est on comparait 1 == 1 ou True == 1 
y = (1 == False) # idem ici, on compare 1 == 0 ou True == False, ce qui donne false 
a = True + 4 #Vu que true == 1, on peut directement le remplacer ici, ce qui va faire 1 + 4 = 5
b = False + 10 # False = 0, donc 0 + 10 = 10

print("x is", x) #True
print("y is", y) #Flase
print("a:", a) #5
print("b:", b) #10

#Exercice 2

total_lettre = 0
continuer = "oui"

while continuer == "oui" :
    phrase = input("Entrez une phrase : ")

    for ph in phrase :
        if ph == "A" :
            total_lettre +=1

    if total_lettre == 0 :
        print("Felicitation, vous avez écrit une phrase sans 'A' ")
    else :
        print("Votre phrase contient la lettre A")
    
    continuer = input("Voulez continuer ? : oui/non \n")


print(f"La lettre A apparait {total_lettre} fois, dans toutes les phrases renseignées")

# Exerice 3
paragraphe = '''
En entrant dans la pièce, le regard est immédiatement attiré par le tableau central, qu'il soit 
traditionnel ou numérique, surplombant le bureau du professeur. Face à lui, les tables et chaises 
des élèves sont disposées en rangées classiques ou en îlots collaboratifs, selon la méthode pédagogique 
privilégiée. Les murs sont généralement recouverts d'affiches éducatives, de cartes géographiques ou de
travaux d'élèves qui ajoutent de la couleur à la pièce. De grandes fenêtres percent souvent l'un des 
côtés, offrant un éclairage naturel indispensable pour éviter la fatigue visuelle. 
Enfin, des armoires de rangement bien ordonnées permettent d'accueillir le matériel collectif, les 
manuels et les fournitures, tandis qu'au fond, un espace peut être dédié à la documentation ou à des
projets spécifiques.
'''

nombre_charactere = 0
nombre_phrase = 0
nombre_mot = 0
for charactere in paragraphe : #On parcours tout le paragraphe (charactère par charatère)
    if charactere != " " :     #Si le charactère choisi est différente d'un espace, on compte le charactère
        nombre_charactere += 1
print(f'Ce paragraphe contient {nombre_charactere} caractères (sans les espaces)')

for character in paragraphe :
    if character == "." : #lorsqu'on parcours le paragraphe, on incrémente le nombre de phrase seulement si on trouve un point
        nombre_phrase += 1
print(f'Ce paragraphe contient {nombre_phrase} phrases')

for character in paragraphe :
    if character == " ": #lorsqu'on parcours le paragraphe, si on trouve un espace lors du parcours, on incrémente le nombre de mot
        nombre_mot += 1
print(f'Ce paragraphe contient {nombre_mot} mots')

mot_unique = set(paragraphe.split()) #ici, set() nous permet de convertir le paragraphe en ensemble ou les mots doubles seront fusionnés et split() sépare les phrases en des mots en s'il y a présence d'espace
nombre_mot_unique = len(mot_unique) ##on compte le nombre de mot contenue dans l'ensemble mot_unique
print(f"Le nombre de mot unique est de {nombre_mot_unique} mots") #on affiche le resultat