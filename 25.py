def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

print()

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
print()

print()

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print("2 ^ 5 =", power(2, 5))

print()

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))

print()

def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

word = input("Enter a word: ")
print("Reversed:", reverse_string(word))
