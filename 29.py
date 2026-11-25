def log_activity(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function", func.__name__, "finished execution")
        return result
    return wrapper

@log_activity
def multiply(a, b):
    print("Computing product")
    return a * b

print("Result:", multiply(6, 7))

print()

def enforce_positive(func):
    def wrapper(n):
        if n < 0:
            print("Negative number not allowed")
            return 0
        return func(n)
    return wrapper

@enforce_positive
def print_root(n):
    return n ** 0.5

print("Square root:", print_root(16))
print("Square root of negative:", print_root(-9))

print()

def debug_args(func):
    def wrapper(*args):
        print("Arguments passed:", args)
        return func(*args)
    return wrapper

@debug_args
def full_name(first, last):
    return first + " " + last

print("Full name:", full_name("Aditya", "Bhandari"))
