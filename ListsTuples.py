# Lists

marks = [85, 44, 57, 89, 93]

student = ["Karan", 85, "Delhi"]

student[0] = "Arjun"
print(len(student))

# Lists Slicing

print(marks[1:4])

# List Methods

print(marks.append(4))
print(marks)
print(type(marks))

marks.sort()
print(marks)

marks.insert(1, 5)
print(marks)

marks.remove(44)
print(marks)

marks.pop(2)
print(marks)

# Tuples

tup = (34, 5, 6, 32, 88)

# tup[0] = 2  Not Allowed in Python

print(type(tup))
print(tup[2])

tuples = (1,)
print(tuples)
print(type(tuples))

huples = (1)
print(huples)
print(type(huples))

# Tuples Methods

print(tup.index(6))

print(tup.count(6))

lists = [1, 2, 1]

copy_list = lists.copy()

copy_list.reverse()
if (copy_list == lists):
    print("Palindrome")
else:
    print("Not Palindrome")
