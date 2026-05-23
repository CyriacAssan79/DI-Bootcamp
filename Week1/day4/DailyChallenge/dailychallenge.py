import math

class Pagination: #Classe pour paginer entre les page
    def __init__(self,items = None, page_size = 10): # On définit les paramètres items et page_size qui seront initialisé par défaut s'il n'ont pas pas de valeur
        if items == None : #On vérifie si l'items existe ou non, s'il n'existe pas, on crée une nouvelle liste d'items
            self.items = []    
        else :
            self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_page = math.ceil(len(self.items)/page_size) #On détermine le nombre de page
    
    def get_visible_items(self) : #Pour une page donnée, non vérifie quelles sont les éléments qui doivent être afficher
        debut = self.current_idx * self.page_size
        fin = debut + self.page_size

        return self.items[debut:fin]
    
    def go_to_page(self, page_num) : #En fonction de la saisie de l'utilisateur, on va à la page demander, si la page n'existe pas on renvoi une erreur
        if page_num < 1 or page_num > self.total_page :
            return print('La page demander n\'existe pas')
        
        self.current_idx = page_num -1
    
    def first_page(self): #On bascule à la première page, c'est à dire à l'index 0
        self.current_idx = 0
        return self
    
    def last_page(self): #On va à la dernière page
        self.current_idx = self.total_page - 1
        return self

    def next_page(self) : #On va à la page suivante ou on incrémente l'index de la page courante de 1
        self.current_idx += 1 
        return self
    
    def previous_page(self) : #On revient à la page précédente et on affiche une erreur si la page demander est en dessous de 0
        if self.current_idx > 0:
            self.current_idx -= 1
        else :
            raise ValueError('Vous êtes déjà à la première page')
        return self

    def __str__(self): #__str__ est une méthode magique pour afficher les messages sans erreurs
        page_actuelle = self.get_visible_items()

        return '\n'.join(map(str,page_actuelle)) 
    

#Teste des méthodes de la classe Pagination
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())

p.last_page()
print(p.get_visible_items())

p.go_to_page(10)
print(p.current_idx + 1)

p.go_to_page(0)