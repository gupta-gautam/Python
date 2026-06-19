class Student:
    college = "BPIT"
    name = "any"  # class attr

    def __init__(self, name, marks):
        self.name = name  # obj attr > class attr
        self.marks = marks
        print("adding new student in Database")

    def hello(self):
        print("hello student", self.name)

    @staticmethod
    def welcome():
        print("welcome student")


s1 = Student("Karan", 97)
print(s1)
s1.name = "Rajat"
print(s1.name, s1.marks)
s1.hello()

s1.welcome()

s2 = Student("Arjun", 98)
print(s2.name, s2.marks)
print(s2.college)

print(Student.college)


class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

        # Debit Method

    def debit(self, amount):
        self.bal -= amount
        print("Rs", amount, "was debited")
        print("total balance =", self.get_balance())

        # credit method

    def credit(self, amount):
        self.bal += amount
        print("Rs", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.bal


acc1 = Account(10000, 12345)
acc1.debit(2000)
acc1.credit(10000)
acc1.credit(3000)
