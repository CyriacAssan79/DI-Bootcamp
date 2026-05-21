#Defi 1
class Farm(): #on définie la classe
    def __init__(self,farm_name): #on initialise le constructeur avec des paramètres *self pour faire référence à l'objet et farm_name pour le nom de la ferme
        self.name = farm_name 
        self.animals = {}
    
    def add_animal (self, animal_type,count=1): #on va chercher à ajouter un nouvel animal dans le dictionnaire animals
        if animal_type in self.animals : #on vérifie si l'animal est présent, s'il est présent on met à jour le nombre
            self.animals[animal_type] += count 
        else : #s'il n'est pas présent on l'ajoute dans le dictionnaire et on met leur nombre *par défaut c'est 1 si aucune valeur n'est entrée
            self.animals[animal_type] = count 
        
        print(self.animals)
    
    def get_info(self) : #On affiche les infos sur la ferme et les animaux qui sont présent
        print(f"Nom de la ferme : {self.name}")
        print("Les animaux présents dans la ferme sont : ")

        for key,value in self.animals.items():
            print(f"{key} : {value}")
        
        

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()