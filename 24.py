square = lambda x: x * x
print("Square of 5:", square(5))

add = lambda a, b: a + b
print("Sum:", add(10, 20))

is_even = lambda n: n % 2 == 0
print("Is 4 even:", is_even(4))
print("Is 7 even:", is_even(7))

print()

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x * x, nums))
print("Squares:", squared)

doubled = list(map(lambda x: x * 2, nums))
print("Doubled:", doubled)

print()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)

greater = list(filter(lambda x: x > 5, nums))
print("Greater than 5:", greater)

print()

words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print("Sorted by length:", sorted_words)

students = [("Aditya", 85), ("Rohan", 92), ("Priya", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Sorted by marks:")
for name, marks in sorted_students:
    print(name, "->", marks)
