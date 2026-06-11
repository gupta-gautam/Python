# Indentation means proper spacing

marks = 92

if (marks >= 90):
    print("A")
elif (marks >= 80 and marks < 90):
    print("B")
elif (marks >= 70 and marks < 80):
    print("C")
else:
    print("D")

# Nesting

age = 34
if (age >= 18):
    if (age >= 80):
        print("can't drive")
    else:
        print("can drive")
else:
    print("can't drive")

a = int(input())
b = int(input())
c = int(input())

if (a >= b and a >= c):
    print(a)
elif (b >= c):
    print(b)
else:
    print(c)
