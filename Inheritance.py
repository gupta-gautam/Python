class Car:
    color = "black"

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


# Parent ka type daalna tha child class mai Toyota mai
# Super() daalke acces krliya
# nhi toh aise hi likhta print krta error aata


class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()


car1 = ToyotaCar("fortuner", "electric")
print(car1.type)


# Class Methods :- sidha class attribute mai change krdiya name = "any" tha
# change krke rahul krdiya class methods se

class Person:
    name = "any"

    @classmethod
    def change(cls, name):
        cls.name = name


p1 = Person()
p1.change("Rahul")
print(p1.name)
print(Person.name)


# Property :-  alg se ye use kr rhe method as property

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property

    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)
