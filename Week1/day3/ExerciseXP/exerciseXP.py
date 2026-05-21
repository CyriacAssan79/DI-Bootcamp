# Exerice 1
class Cat:
    def __init__(self, cat_name, cat_age): #initialisation du constructeur ainsi ainsi que des valeur que la classe va avoir
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Paul", 1)
cat2 = Cat("Marie", 3)
cat3 = Cat("Jane", 1)
chat = {              #chat est un objet contenant le nom du chat comme clé et age comme valeur
    cat1.name:cat1.age,
    cat2.name:cat2.age,
    cat3.name:cat3.age,
}


# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3): # On recherche le plus vieux chat
    old_cat = cat1 #on prend le premier chat comme valeur de départ

    if cat2.age > old_cat.age : old_cat = cat2 # on vérifier si l'age du premier chat est supérieur à l'age du deuxième, si c'est le cas on passe à la conduite suivante
    elif cat3.age > old_cat.age : old_cat = cat3 #on fait ainsi pareil ici aussi
    return  old_cat

# Step 3: Print the oldest cat's details
old_cat = find_oldest_cat (cat1,cat2,cat3) #on appel la fonction

print(f'Le plus vieux chat est {old_cat.name} et il a {old_cat.age} ans')


# Exerice 2 : 
class Dog():
    def __init__ (self,name,height) :
        self.name = name
        self.height = height
    
    def bark(self):
        return f"{self.name} fait ouaf"
    
    def jump(self):
        return f"{self.name} saute {self.height*2} cm de haut !"

davids_dog = Dog("Paul",20)
sarahs_dog = Dog("Marie",10)

print(sarahs_dog.bark())
print(sarahs_dog.jump())

print(davids_dog.bark())
print(davids_dog.jump())

if sarahs_dog.height > davids_dog.height :
    print("Le chien de sarah est plus grand")
else :
    print("Le chien de david est plus grand")

# Exerice 3 :

class Song() :
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for lyric in self.lyrics : 
            print(lyric,end=' ')

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Exerice 4
class Zoo ():
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.clean_animal = {}
    
    def add_animal (self,new_animal) : #on ajoute un animal à la liste de celle qui était déjà présente
        if new_animal in self.animals :
            print("L'animal est déjà présent dans la liste!")
        else :
            self.animals.append(new_animal)
            
    
    def get_animals(self): #on récupère la liste de tous les animaux
        print("Liste de  tous les animaux présents dans le zoo")
        for anim in self.animals :
            print(anim)
    
    def sell_animal(self, animal_sold) : #on vérifie si l'animal est présente dans la liste, s'il est présent on le supprime  
        for anim in self.animals :
            if animal_sold == anim :
                self.animals.remove(animal_sold)
            else :
                print("L'animal n'existe pas")
    
    def sort_animals(self): #on groupe les les animaux en fonction de leur première lettre
        sorted_animals = sorted(self.animals)

        for animal in sorted_animals:
            first_letter = animal[0]

            if first_letter not in self.clean_animal:
                self.clean_animal[first_letter] = []

            self.clean_animal[first_letter].append(animal)

        print(self.clean_animal)
    
    def get_groups(self) : #On récère l'objet contenant les animaux
        for key,value in self.clean_animal.items() :
            print(f"{key} : {value}")
        

    # Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()

