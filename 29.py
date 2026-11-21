def greet(func):
    def wrapper(name):
        print("Hello", name)
        func(name)
        print("Have a nice day")
    return wrapper

@greet
def say_name(name):
    print("Your name is", name)

say_name("Aditya")

print()

def repeat(times):
    def decorator(func):
        def wrapper(*args):
            for i in range(times):
                func(*args)
        return wrapper
    return decorator

@repeat(3)
def hello(name):
    print("Hi", name)

hello("Rohan")

print()

import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print("Time taken:", round(end - start, 4), "seconds")
        return result
    return wrapper

@timer
def slow_add(a, b):
    total = 0
    for i in range(1000000):
        total = total + 1
    return a + b

print("Result:", slow_add(10, 20))
