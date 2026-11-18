username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

day = input("Enter day: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

num = int(input("Enter a number: "))

if not num % 2 == 0:
    print("Odd number")
else:
    print("Even number")

age = int(input("Enter age: "))
has_license = input("Do you have a license (yes/no): ")

if age >= 18 and has_license == "yes":
    print("You can drive")
elif age >= 18 and has_license == "no":
    print("Get a license first")
else:
    print("You are too young to drive")
