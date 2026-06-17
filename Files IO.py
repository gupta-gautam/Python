f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("demo.txt", "a")
f.write("\nThen I will move to Spring boot")
f.close()

f = open("demo.txt", "r+")
f.write("HII")
f.close()

with open("demo.txt", "w") as f:
    data = f.write("hello I am \n Learning python")
    print(data)


# For Deleting a File

# import os
# os.remove("demo.txt")

def check():
    word = "Learning"
    Data = True
    line = 1
    with open("demo.txt", "r") as f:
        while Data:
            Data = f.readline()
            if (word in Data):
                print(line)
                return
            line += 1

    return -1

check()