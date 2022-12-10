class Pet:
    def __init__(self, name, type, tricks, noise): #added noise per the solutions video, added noise into parameters and below and added empty string: go to def noise 
        self.name = name
        self.type = type
        self.tricks = tricks 
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        self.health += 10 # not required 
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 10 # not required 
        return self

    def noise(self):
        print(self.noise) #passed in self.noise
        return self