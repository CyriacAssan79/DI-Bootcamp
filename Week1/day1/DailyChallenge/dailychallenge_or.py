jour = input("Entrez votre jour de naissance : ") #On récupère le jour de naissance de l'utilisateur
mois = input("Entrez votre mois de naissance : ") #On récupère son mois de naissance
annee = input("Entrez votre année de naissance : ") #On récupère son année de naissance


age = 2026 - int(annee) #on calcule son age

print(f"Vous êtes né le {jour} / {mois} / {annee} et vous avez {age} âge") #On affiche ses informations

bougie = str(age) #On stocke l'age dans la variable bougie, on veut chercher à déterminer le nombre de bougie

i_bougie = int(bougie[-1]) #On récupère le dernier chiffre de l'age
terminer = 0

nombre_i = "" #nombre_i va stocker nos i
while terminer < i_bougie : #On vérifie que terminer n'est pas pas égale sous supérieure à au dernier chiffre de l'age
    nombre_i += "i" #A chaque tour de boucle, on concatène
    terminer += 1 #On incrémente terminer pour éviter une boucle infinie

if ((int(annee)%4 == 0 and int(annee) % 100 != 0) or (int(annee) % 400 == 0)) : #On vérifie si l'année est bissextile
    for i in range(1,3) : #Si c'est le cas on affiche 2 gateau
        print(f"    ___{nombre_i}___   ") #On ajoute nos nombre de i
        print("   |:H:a:p:p:y:|  ")
        print(" __|___________|__")
        print("|^^^^^^^^^^^^^^^^^|")
        print("|:B:i:r:t:h:d:a:y:|")
        print("|                 |")
        print("~~~~~~~~~~~~~~~~~~~")
else :                        #On ajoute 1 seul gateau
    print(f"    ___{nombre_i}___   ")
    print("   |:H:a:p:p:y:|  ")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")
