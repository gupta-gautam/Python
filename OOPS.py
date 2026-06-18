class Student:
    college ="BPIT"
    name = "any" #class attr
    def __init__(self, name, marks):
        self.name = name # obj attr > class attr
        self.marks = marks
        print("adding new student in Database")

    def hello(self):
        print("hello student",self.name)


s1 = Student("Karan", 97)
print(s1)
print(s1.name, s1.marks)
s1.hello()

s2 = Student("Arjun", 98)
print(s2.name, s2.marks)
print(s2.college)

print(Student.college)