#Defi 1

mot = input("Saisissez un mot : ")
my_dict = {}

for m in range(0,len(mot)) : #on parcourt tous les caractères du mot entrés grace à leur index
    if mot[m] in my_dict : #ensuite on vérifie si la valeur de l'index existe déjà dans le dictionnaire, si c'est le cas on ajoute cette nouvelle valeur à la valeur précédente de la clé
        my_dict[mot[m]].append(m)
    else : #sinon on enregistre une nouvele clé avec une nouvelle valeur
        my_dict[mot[m]] = [m]
        

print(my_dict)

#Défi 2 

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

wallet = "$300"
basket = [] #Portefeuille va contenir tout ce que j'ai 

wallet = int(wallet.replace('$','').replace(',','')) #on nettoie la chaine de charactere pour obtenir entier contenant mon budget

for key, value in items_purchase.items(): #on parcourt les éléments à acheter 
    prix = int(value.replace('$','').replace(',','')) #On supprime le $ et les virgules pour avoir un entier
    if wallet > prix : # on vérifier si le budget est supérieur à l'objet que je veux acheter
        basket.append(key) #Si c'est le cas on ajoute l'objet au portefeuille
    wallet -= prix #on retire l'argent dépense du portefeuille

if len(basket)== 0:
    print("Rien")
else :
    print(sorted(basket)) # on trie par ordre croissant
