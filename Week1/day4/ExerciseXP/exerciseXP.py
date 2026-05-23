#Exerice 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#Step 1: Create the Siamese Class
class Siamese (Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
    def color(self, color_cat):
        return f'{color_cat}'

#Step 2: Create a List of Cat Instances
all_cats = [Bengal("Miou",4),Chartreux("Miaouu",3),Siamese("Mio",4)]
print(all_cats[2].color("red"))

#Step 3: Create a Pets Instance
sara_pets = Pets(all_cats)
sara_pets.walk()

# Exerice 2
class Dog:
    def __init__(self, name, age, weight):
        # ... code to initialize attributes ...
        self.name = name
        self.age = age
        self.weight = weight


    def bark(self):
        # ... code to return bark message ...
        print(f'{self.name} aboie')

    def run_speed(self):
        # ... code to return run speed ...
        return (self.weight/self.age)*2
    

    def fight(self, other_dog):
        # ... code to determine and return winner ...
        puissance_dog1 = self.run_speed() * self.weight
        puissance_dog2 = other_dog.run_speed() * other_dog.weight

        if(puissance_dog1 > puissance_dog2) :
            return f'{self.name} bat {other_dog.name}'
        elif (puissance_dog1 < puissance_dog2):
            return f'{other_dog.name} bat {self.name}'
        else:
            return f'Les deux sont égaux'

# Step 2: Create dog instances
#... your code here
dog1 = Dog("Bouffi", 6,175)
dog2 = Dog("rantanplan",8,150)
dog3 = Dog("jose",2,140)
# Step 3: Test dog methods

dog1.bark()
print(dog2.run_speed())
print(dog1.fight(dog2))

# Exerice 3 
import random

from dog import Dog #appel de la classe Dog

class PetDog(Dog): #initialisation de la classe PetDog qui hérite de Dog
    def __init__(self, name, age, weight,trained = False): #La classe enfant utilise ses propres constructeurs
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self): #Cette methode renvoie qu'un chien abois
        print(self.bark())
        self.trained = True

    def play(self, *args): #Ici, on récupère tous les informations sur le chien grâce a *args (on peut passer passer plusieurs chien en attribut sans avoir à les ajouter comme paramètres)
        dog_name = [self.name] 

        for dog in args : #Vu que args est une liste de chien avec leurs caractéristiques, on le parcours pour récupérer les noms
            dog_name.append(dog.name)
        
        for dog in dog_name :
            print(f'{dog}',end=', ')

        print(f'all play together')

    def do_a_trick(self): #ici, si le chien à un trained de true on affiche un message aléatoire se trouver dans la liste trick
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog1 = PetDog("Jay", 4, 6)
my_dog2 = PetDog("Marise", 3, 8)
my_dog.train()
print(my_dog.trained)
my_dog.play(my_dog1,my_dog2)
my_dog.do_a_trick()

#Exerice 4
class Person :
    def __init__(self,first_name,age): #initialisation constructeur avec firstname et age comme paramètre
        self.first_name = first_name
        self.age = age
        self.last_name = ""
    
    def is_18(self): #On vérifie si l'age du membre est supérieure à ou égale à 18
        if self.age >=18 :
            return True
        else :
            return False

class Family:  #Classe qui va fait reference à tous les membres de la famille
    def __init__(self,lastname):
        self.lastname = lastname
        self.members = []
    
    def born(self, first_name, age): #Methode pour ajouter chaque personne à la famille
        person = Person(first_name,age)

        person.last_name = self.lastname

        self.members.append(person)
    
    def check_majority(self, first_name): #recherche d'un memebre de la famille ainsi que la vérification de son age
        for m in self.members :
            if m.first_name == first_name:
                if m.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else :
                    print("Sorry, you are not allowed to go out with your friends.")
    
    def family_presentation(self): #Présentation de la famille
        for m in self.members :
            print(f'FirstName : {m.first_name}')
            print(f'LastName : {m.last_name}')
            print(f'age : {m.age}')
            print('************************')
person1 = Family("Cyriac")
person1.born("Assan",24)
person1.born("Aman",21)
person1.check_majority("Assan")

person1.family_presentation()

