'''
#single
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
    def print_info(self):
        print(f'{self.name}')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f"{self.name} says woof"

dog = Dog('Buddy')
print(dog.speak())

#Multiple
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Mammal(Animal):
    def speak(self):
        pass

class Dog(Mammal):
    def speak(self):
        return f"{self.name} says woof"

dog = Dog('Buddy')
print(dog.speak())

#Heirachical
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"

dog = Dog('Buddy')
cat = Cat('Whiskers')

print(dog.speak())
print(cat.speak())
'''
#Multiple
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Mammal(Animal):
    def speak(self):
        pass

class Dog(Mammal):
    def speak(self):
        return f"{self.name} says woof"
class Cat(Mammal):
    def speak(self):
        return f"{self.name} says meow"

dog = Dog('Buddy')
cat = Cat('Whiskers')

print(dog.speak())
print(cat.speak())