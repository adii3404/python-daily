def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

print("Add:", add(10, 20))
print("Subtract:", subtract(30, 10))
print("Multiply:", multiply(5, 4))

print()

def is_even(n):
    if n % 2 == 0:
        return True
    return False

num = int(input("Enter a number: "))
if is_even(num):
    print("Even")
else:
    print("Odd")

print()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))

print()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime")
else:
    print("Not Prime")
