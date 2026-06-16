fact = 1
n=5
for i in range(1,n+1):
    fact*=i


print(fact)

# Function

# Function Definition
def calc_sum(a,b): # Parameters
    return a+b

sum = calc_sum(3,5) # Function call ; Arguments
print(sum)


cities = ["delhi","mumbai","pune","goa"]
car = ["alto","bmw","mercedes"]

def calc_len(list):
    print(len(list))

calc_len(cities)
calc_len(car)

def print_list(list):
    for val in list:
        print(val, end=" ")

print_list(car)


def converter(usd):
    inr = usd * 94
    print(usd,"usd =",inr,"inr")

converter(73)