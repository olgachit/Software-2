'''
class Dog:
    pass
# We create a myDog object, constructor
mydog = Dog()

mydog.name = "Chicko"
mydog.age = 2
print(mydog.name, mydog.age)

yourdog = Dog()
yourdog.name = "mi"
yourdog.age = 3
print(yourdog.name, yourdog.age)
'''
class Dog:
    count=0
    def __init__(self, name, age, sound="yau yau"):
        self.name = name
        self.age = age
        Dog.count = Dog.count+1
        self.sound = sound
    def change_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def __str__(self):
        return f'{self.name} {self.age}'
    def gasp(self, times):
        for i in range(times):
           print(self.name, self.sound)
        return

mydog=Dog("chicko", 3)
yourdog=Dog("mi", 2)
hisdog=Dog("snowy", 20)
herdog=Dog("mikko", 19)
doglist=[mydog, yourdog, hisdog, herdog]
print(f"Dog's name: {mydog.name} is {mydog.age} years old")
mydog.change_name("mikko")
yourdog.change_name("hap")
print({mydog.name})
print(mydog.get_age())
print(str(mydog))
print(f"number of dogs created: {Dog.count}")
mydog.gasp(3)
# Go through the dogs object and print one by one
for dog in doglist:
    print(dog) # automatically invoke the __str__

class Nursing:
    def __init__(self):
        self.dogs = []

    def addDog(self, name):
        self.dogs.append(dog)
        print(f"the dog: {dog} is added")

    def getDog(self):
        for dog in self.dogs:
            print(dog.getName(), dog.getAge)

    def removeDog(self, name):
        self.dogs.remove(dog)

nursing1 = Nursing()
nursing2 = Nursing()
nursing1.addDog(mydog)
nursing2.addDog(hisdog)