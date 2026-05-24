#Circle class
import math

class Circle :
    #Constructor initialization with parameter radius 
    def __init__(self,radius): 
        self.radius = radius


    @property
    def diameter(self):
        return self.radius*2 #return circle diameter
    
    @diameter.setter
    def diameter(self,value):
        self.radius = value / 2 #radius modification via the diameter
    
    @classmethod
    def create_circle(cls,diameter):
        return cls(diameter/2) #Create a new circle with diameter 
    
    def area(self):
        return math.pi*self.radius**2 #Calculation of circle area
    
    def __str__(self):
        return f'Circle(radius: {self.radius}, diameter: {self.diameter})' #Print the attributes of the circle
    
    def __add__(self, other):
        if isinstance(other,Circle) :
            return Circle(self.radius + other.radius) #Add two circles together and return a new circle with the new radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other,Circle):
            return self.radius > other.radius #Compare two circles to see which is bigger
        return NotImplemented
    
    def __eq__(self, value):
        if isinstance(value,Circle):
            return self.radius == value.radius # Compare two circles to check if they are equal
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other,Circle):
            return self.radius < other.radius #Store multiple circles in a list and sort them
        return NotImplemented

# Create cicrcle
circle1 = Circle(2)
circle2 = Circle(4)
circle3 = Circle.create_circle(6)

# Add
circle = circle1 + circle2

print(circle)

# Comparaison
print(circle1 < circle2)
print(circle1 == circle2)

# Sorted
my_list = [circle1, circle2, circle3]
my_list = sorted(my_list)

for circle in my_list:
    print(circle)

