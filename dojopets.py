from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self): #added this per solutions video 
        self.pet.noise()
        return self


rocko = Pet("rocko", "dog", "shakesPaw", "bark bark")
gino = Ninja("Gino", "Sorrisso","bones", "dog_food", rocko)
print(rocko.health)
print(rocko.energy)
print(gino.first_name)
print(rocko.name)
gino.walk()
print(f"You gained health: {rocko.health}")
print(f"You lost energy: {rocko.energy}")
print(rocko.noise)
#     # implement the following methods:
#     # walk() - walks the ninja's pet invoking the pet play() method
#     # feed() - feeds the ninja's pet invoking the pet eat() method
#     # bathe() - cleans the ninja's pet invoking the pet noise() method
