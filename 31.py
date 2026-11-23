import re

text = "My phone number is 9876543210 and email is aditya@gmail.com"

phone = re.findall(r"\d{10}", text)
print("Phone:", phone)

email = re.findall(r"\S+@\S+", text)
print("Email:", email)

print()

text = "Hello World Hello Python Hello Code"
result = re.sub("Hello", "Hi", text)
print("After replace:", result)

result2 = re.sub("Hello", "Hi", text, count=1)
print("Replace first only:", result2)

print()

pattern = r"^\d{4}-\d{2}-\d{2}$"
dates = ["2024-01-15", "15-01-2024", "2024/01/15", "2024-12-31"]

for d in dates:
    if re.match(pattern, d):
        print(d, "-> Valid date format")
    else:
        print(d, "-> Invalid date format")

print()

text = "apple banana cherry apple date banana apple"
words = re.findall(r"\b\w+\b", text)
print("Words:", words)
print("Word count:", len(words))

freq = {}
for w in words:
    if w in freq:
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1

for key in freq:
    print(key, "->", freq[key])

print()

password = input("Enter password: ")
if len(password) < 8:
    print("Too short")
elif not re.search(r"[A-Z]", password):
    print("Need uppercase letter")
elif not re.search(r"[a-z]", password):
    print("Need lowercase letter")
elif not re.search(r"\d", password):
    print("Need a digit")
else:
    print("Strong password")
