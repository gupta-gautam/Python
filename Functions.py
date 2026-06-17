fact = 1
n = 5
for i in range(1, n + 1):
    fact *= i

print(fact)


# Function

# Function Definition
def calc_sum(a, b):  # Parameters
    return a + b


sum = calc_sum(3, 5)  # Function call ; Arguments
print(sum)

cities = ["delhi", "mumbai", "pune", "goa"]
car = ["alto", "bmw", "mercedes"]


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
    print(usd, "usd =", inr, "inr")


converter(73)


# Recursion

def show(n):
    if (n == 0):
        return
    print(n)
    show(n - 1)


show(5)


def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def print_sum(c):
    if (c == 0):
        return 0
    return c + print_sum(c - 1)


print(print_sum(7))


def print_lists(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_lists(list, idx + 1)


fruits = ["mango", "guava", "orange", "litchi"]

print_lists(fruits)
