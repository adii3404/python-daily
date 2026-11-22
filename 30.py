def count_up(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1

print("Count up to 5:")
for num in count_up(5):
    print(num, end=" ")
print()

print()

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci series:")
for num in fibonacci(10):
    print(num, end=" ")
print()

print()

def even_numbers(limit):
    i = 2
    while i <= limit:
        yield i
        i = i + 2

evens = list(even_numbers(20))
print("Even numbers:", evens)

print()

def odd_numbers(limit):
    i = 1
    while i <= limit:
        yield i
        i = i + 2

odds = list(odd_numbers(20))
print("Odd numbers:", odds)

print()

nums = [1, 2, 3, 4, 5]
squared_gen = (x * x for x in nums)
print("Squared:", list(squared_gen))

cubed_gen = (x * x * x for x in nums)
print("Cubed:", list(cubed_gen))

print()

class PowerOfTwo:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n = self.n + 1
        return result

print("Powers of 2:")
for val in PowerOfTwo(8):
    print(val, end=" ")
print()

print()

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        val = self.start
        self.start = self.start - 1
        return val

print("Countdown:")
for val in Countdown(5):
    print(val, end=" ")
print()
