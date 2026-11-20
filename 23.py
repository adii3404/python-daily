try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

print()

try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError:
    print("Index out of range")

print()

try:
    f = open("nofile.txt", "r")
except FileNotFoundError:
    print("File does not exist")

print()

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Division:", a / b)
except Exception as e:
    print("Error:", e)
finally:
    print("Program finished")

print()

age = int(input("Enter age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
else:
    print("Your age is", age)
