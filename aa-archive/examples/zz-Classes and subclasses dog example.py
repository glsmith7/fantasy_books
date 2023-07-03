class Dog(object):

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.legs = 4

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound="Woof"):
        return f"{self.name} says {sound}"
    
class JackRussellTerrier(Dog):

    def __init__ (self,name,age):
        super().__init__(name, age) # inherit from super class
        
        self.legs=2 # set specific for subclass
        
    def speak(self, sound="Arf!"):
        return f"{self.name} says {sound}"

boris=Dog("Boris",3)
miles=JackRussellTerrier("Miles",5)

print (boris)
print (miles)

print (boris.speak())
print (miles.speak())
print (boris.legs)
print (miles.legs)

print (boris.species)
print (miles.species)







