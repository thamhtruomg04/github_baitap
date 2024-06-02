class SimpleClass:
    i = 5
    def __init__(self):
        self.j = 7
    
    def PrintMe(self):
        print(self.j)

sim = SimpleClass()

print(sim.i)
sim.PrintMe()


sim.i = 500
sim.j= 700

print(sim.i)
sim.PrintMe()


class SimpleClass2:
    # constructor
    def __init__(self):
        self.name = "Thanh Truong"
    # method
    def hello(self):
        print("Hello " + self.name)

    # Static method
    @staticmethod
    def hi(name):
        print("Hi " + name)
simC = SimpleClass2()
simD = SimpleClass2()

simC.hello()
simD.hi("Minh Khang")

SimpleClass2.hi("Hoang Duc")