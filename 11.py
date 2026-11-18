s = input("Enter a string: ")

print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title case:", s.title())
print("First character:", s[0])
print("Last character:", s[-1])

print()

s = input("Enter a string: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count = count + 1
print("Number of vowels:", count)

print()

s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)

if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
