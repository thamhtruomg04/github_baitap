'''
animal
    name

    eat()
    makeSound()
    sleep()

Dog
    eat()
    makeSound()
Cat
    eat()
    makeSound()
Bird
    eat()
    makeSound()
'''

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat():
        print("Unknow")

    def makeSound():
        print("Unknow")
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def eat(self):
        print("{0} An com".format(self.name))
    def makeSound(self):
        print("{0} zzzZZZ ".format(self.name))

cat1 = Cat("MiuMiu")
cat1.eat()
cat1.makeSound()
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def eat(self):
        print("{0} an bot".format(self.name))
    def makeSound(self):
        print("{0} meo meo".format(self.name))
dog1 = Dog("TunTun")
dog1.eat()
dog1.makeSound()


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("{0} an cam".format(self.name))
    def makeSound(self):
        print("{0} oooOOO".format(self.name))

cat1 = Cat("BirdDay")
cat1.eat()
cat1.makeSound()