class Dog:
    def __init__(self, name, age, weight):
        # ... code to initialize attributes ...
        self.name = name
        self.age = age
        self.weight = weight


    def bark(self):
        # ... code to return bark message ...
        return f'{self.name} aboie'

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