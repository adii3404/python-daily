s = input("Enter a string: ")

print("Slice [0:5]:", s[0:5])
print("Slice [2:]:", s[2:])
print("Slice [:4]:", s[:4])
print("Slice [-3:]:", s[-3:])
print("Step [::2]:", s[::2])
print("Reverse [::-1]:", s[::-1])

print()

s = input("Enter a string: ")
word = input("Enter word to find: ")

if word in s:
    print("Found at index:", s.index(word))
else:
    print("Not found")

print()

s = input("Enter a sentence: ")
words = s.split(" ")
print("Words:", words)
print("Word count:", len(words))
print("Joined back:", "-".join(words))
