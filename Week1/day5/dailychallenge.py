class Circle :
    def __init__(self,radius,diameter):
        self.radius = radius
        self.diameter = diameter
    
    def area(self):
        return 3.141*self.radius**2
    
    def __str__(self):
        return f'Circle area {self.area()}'
    
    def __add__(self, other):
        print (Circle(self.radius + other.radius, self.diameter + other.diameter))

    def __gt__(self, other):
        if isinstance(other,Circle):
            return self.radius > other.radius
        return NotImplemented
    
    def __eq__(self, value):
        if isinstance(value,Circle):
            return self.radius == value.radius and self.diameter == value.diameter
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other,Circle):
            return self.radius < other.radius
        return NotImplemented

circle1 = Circle(2,5)
circle2 = Circle(4,8)
circle3 = Circle(3,6)
circle = circle1 + circle2

print(circle1 < circle2)
print(circle1 == circle2)

my_liste = [circle1,circle2,circle3]
my_liste = sorted(my_liste)
for cicle in my_liste:
    print(cicle)

