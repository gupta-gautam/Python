# While Loops

#Qs1
n = 2
i=1
while i <=10 :
    print(n * i)
    i+=1

i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1


print("end")


nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0

while i < len(nums):
    if nums[i] == x:
        print("found", i)
        break
    else:
        print("not found")
    i += 1

# Continue
i = 0
while i<=5 :
    if(i ==3):
        i+=1
        continue
    print(i)
    i+=1


# For Loops

num = [1,2,3,4,5]
x=4
idx = 0
for val in num :
    if (val == x):
        print("found",idx)
        break
    else:
        print("not found")
        idx+=1


# Range
for el in range(1,6,2):
    print(el)


sum = 0
m = 7
for c in range(1,m+1):
    sum+=c
    print(sum)