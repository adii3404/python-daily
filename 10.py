i = 1
while i <= 10:
    print(i)
    i = i + 1

print()

n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed:", rev)

print()

n = int(input("Enter a number: "))
count = 0
temp = n
while temp > 0:
    count = count + 1
    temp = temp // 10
print("Number of digits:", count)

print()

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial:", fact)
