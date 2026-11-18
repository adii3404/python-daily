ch = input("Enter a character: ")

if ch >= 'a' and ch <= 'z':
    print("Lowercase letter")
elif ch >= 'A' and ch <= 'Z':
    print("Uppercase letter")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special character")

bill = float(input("Enter bill amount: "))

if bill > 1000:
    discount = bill * 0.20
elif bill > 500:
    discount = bill * 0.10
else:
    discount = 0

print("Discount:", discount)
print("Final amount:", bill - discount)

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
