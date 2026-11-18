s = input("Enter a string: ")

print("Starts with 'He':", s.startswith("He"))
print("Ends with 'lo':", s.endswith("lo"))
print("Replace:", s.replace("l", "r"))
print("Strip:", s.strip())
print("Is alpha:", s.isalpha())
print("Is digit:", s.isdigit())

print()

s = input("Enter a string: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

for key in freq:
    print(key, ":", freq[key])

print()

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not an anagram")
