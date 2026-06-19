class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real, "i +", self.img)

    def __add__(self, num2):  # Dunder Function :- logic define ho jata isse
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


num1 = Complex(1, 4)
num1.show()

num2 = Complex(4, 6)
num2.show()

num3 = num1 + num2
num3.show()


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role = ", self.role)
        print("dept =", self.dept)
        print("salary=", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")


eng1 = Engineer("Elon Musk", 40)
eng1.showDetails()

e1 = Employee("accountant", "Finance", "60,000")
e1.showDetails()


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)
