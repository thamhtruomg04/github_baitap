class Animal:
    def __init__(self, animalTypeA,nameA, widthA, heightA, weightA ):
        self.animalType = animalTypeA 
        self.name = nameA
        self.width = widthA
        self.height = heightA
        self.weight = weightA 

    def makeVoice(self):
        print("Unknow voice")

    # in thong tin
    def printMe(self):
        print("animalType: {0}, name={1}, width={2}, height={3}, weight={4}".format(self.animalType, self.name, self.height, self.weight, self.width))


animal1 = Animal("Con nguoi", "Vu Thanh Truong", "165cm", "56kg", "15cm")
animal1.printMe()
animal1.makeVoice()

class Dog(Animal):
    def __init__(self, animalTypeA, nameA, widthA, heightA, weightA, isChampionA):
        super().__init__(animalTypeA, nameA, widthA, heightA, weightA)
        self.isChampion = isChampionA
    # override method
    def makeVoice(self):
        print("{0} : gau gau".format(self.name))

    def takeCareHome(self):
        print("{0}: zzzZZZ".format(self.name))

dog1 = Dog("Cho", "Tun", "50cm", "40cm", "10kg", True)
dog2 = Dog("Cho", "Mat", "150cm", "100cm", "50Kg", True)

dog1.makeVoice()
dog2.makeVoice()
dog1.takeCareHome()

dog1.printMe()
dog2.printMe()
dog2.takeCareHome()


class Meo(Animal):
    def __init__(self, animalTypeA, nameA, widthA, heightA, weightA, colorA):
        super().__init__(animalTypeA, nameA, widthA, heightA, weightA)
        self.color = colorA
    def makaVoice(self):
        print("{0} : meo meo".format(self.name))

    def catchMouch(self):
        print("{0}: catch a mouse".format(self.name))

cat1 = Meo("Meo","MiuMiu", "12cm", "13cm", "4kg", "Grey")
cat2 = Meo("Meo", "MatMeo", "12cm", "12cm", "4kg", "Blue")
cat1.makaVoice()
cat1.printMe()
cat1.catchMouch()

cat2.makaVoice()
cat2.printMe()
cat2.catchMouch()