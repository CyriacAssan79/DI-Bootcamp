# Exerice 1
# class Circle :
#     def __init__(self,radius):
#         self.radius = radius
#         self.perimetre_cercle = 0
#         self.aire_cercle = 0
    
#     def perimetre (self):
#         self.perimetre_cercle = 2*self.radius*3.141
#         print(f"Le périmètre du cercle est {self.perimetre_cercle}")
        
    
#     def aire(self) :
#         self.aire_cercle = 3.141*self.radius**2
#         print(f"L'aire du cercle est {self.aire_cercle}") 
    
#     def affiche(self):
#         print(f"On a un cercle de rayon de {self.radius} où l'aire est {self.aire_cercle} et le périmètre est {self.perimetre_cercle}")

# circle = Circle(2)
# circle.perimetre()
# circle.aire()
# circle.affiche()

# Exercice 2
# import random
# class MyList :
#     def __init__(self,letter):
#         self.letter = letter
#         self.new_list = []
    
#     def inverse(self):
#         print(f"La liste inversé est {reversed(self.letter)}")
    
#     def ranger(self):
#         print(f"La nouvelle liste triée est {sorted(self.letter)}")
    
#     def newList(self):
#         for i in range(0,len(self.letter)):
#             self.new_list.append(random.randint(0,100))
        
#         print(f"La liste est : {self.new_list}")

# mylist = MyList(["Cyriac","Assan","test"])
# mylist.inverse()
# mylist.ranger()
# mylist.newList()

#Exerice 3
class MenuManager :
    def __init__(self,menu):
        self.menu = menu
    
    def add_item(self,name, price, spice, gluten) :
        plat = {
            "name" : name,
            "price" : price,
            "spice" : spice,
            "gluten" : gluten
        }

        self.menu.append(plat)

    def update_item(self,name, price, spice, gluten) :
        for m in self.menu :
            if m["name"] == name :
                m['price'] = price
                m['spice'] = spice
                m['gluten'] = gluten
                print(f"Menu {name} mis à jour")


    def remove_item(self,name) :
        self.menu = [m for m in self.menu if m['name'] !=name ]


    def afficher(self) :
        print(f"La liste des menus est : ")
        for menu in self.menu :
            print("************************")
            print(f"Titre : {menu["name"]}")
            print(f"Prix : {menu["price"]} FCFA")
            print(f"Niveau d'épice : {menu["spice"]}")
            if menu["gluten"] ==True:
                print("Glutenn : Avec gluten")
            else :
                print('Gluten : Sans gluten')


menu_manager = MenuManager([])
menu_manager.add_item("garba",500,"B", True)
menu_manager.add_item("tchep",1000,"A", False)
menu_manager.afficher()
menu_manager.remove_item('garba')
menu_manager.afficher()
menu_manager.update_item("tchep",5000,"A", False)
menu_manager.afficher()