for i in range(1, 11):
    print(i)

print()

for i in range(10, 0, -1):
    print(i)

print()

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum =", sum)

print()

n = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
