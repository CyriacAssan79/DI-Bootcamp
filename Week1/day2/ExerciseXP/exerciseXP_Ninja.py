#Exerice 1 

texte = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet, Tesla, Bugatti"
voiture = list(texte.split(',')) #Transformation de la chaine en liste
print(f"Il y a {len(voiture)} fabricants")

voiture = sorted(voiture) #Ranhement de la liste pas ordre alphabétique
voiture.reverse() #Inversement de la liste de Z à A

manufacturers_name = {}

for v  in voiture :
    manufacturers_name[v] = 0 # Ajout de chaque constructeur de vahicule au dictionnaire avec une valeur (utile pour vérfier la présence ou l'absence s'occurence)

for key, value in manufacturers_name.items() :
    if 'o' in key : #On vérifie s'il y a la lettre o dans chaque nom de constructeur, si oui la valeur devient 1 et si non la valeur reste 0 
        manufacturers_name[key] = 1
    else:
        manufacturers_name[key] = 0

nombre = 0
for key, value in manufacturers_name.items():
    if value == 1 : 
        nombre +=1 #On détermine ici le nombre de constructeur ou il y un 'o' dans leur nom
    
print(f"Il y a {nombre} qui ont la lettre 'o' dans leurs noms")

for key, value in manufacturers_name.items() :
    if 'i' in key : #On vérifie s'il y a la lettre y dans chaque nom de constructeur, si oui la valeur devient 1 et si non la valeur reste 0 
        manufacturers_name[key] = 1
    else :
        manufacturers_name[key] = 0

nombre = 0
for key, value in manufacturers_name.items():
    if value == 0 : #On détermine ici le nombre de constructeur ou il y un 'i' dans leur nom
        nombre +=1

print(f'Il y a {nombre} fabricants qui n\'ont pas lettre i')

new_list = list(["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"])
new_list = set(new_list) # On supprime les doublon dans la liste

for nl in new_list :
    print(f'{nl}, ',end='') #On affiche le nom des constructeur sur une ligne séparer par une virgule

print(f'\nIl y a {len(nl)} entreprises dans la liste')

#Exerice 2
def get_full_name(first_name,middle_name='', full_name =''):
    if middle_name == '' :
        full_name = first_name
        print(full_name)
    else: 
        full_name = first_name + ' ' + middle_name
        print(full_name)
    

get_full_name(first_name='Assan', middle_name='Cyriac')
