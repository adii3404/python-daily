import math
import random
import datetime

print("Square root of 25:", math.isqrt(25))
print("Ceil of 4.2:", math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))
print("GCD of 48 and 18:", math.gcd(48, 18))
print("Factorial of 6:", math.factorial(6))

print()

print("Random integer (1 to 10):", random.randint(1, 10))
items = ["apple", "banana", "orange", "mango"]
print("Random choice:", random.choice(items))

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("Shuffled:", cards)

print()

now = datetime.datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Current year:", now.year)
print("Current day:", now.strftime("%A"))

custom_date = datetime.date(2026, 1, 1)
today = datetime.date.today()
diff = today - custom_date
print("Days since 2026-01-01:", diff.days)
