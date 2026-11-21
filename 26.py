nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [x * x for x in nums]
print("Squares:", squares)

evens = [x for x in nums if x % 2 == 0]
print("Evens:", evens)

odds = [x for x in nums if x % 2 != 0]
print("Odds:", odds)

print()

words = ["hello", "world", "python", "code"]
upper = [w.upper() for w in words]
print("Uppercase:", upper)

lengths = [len(w) for w in words]
print("Lengths:", lengths)

print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print("Flattened:", flat)

print()

pairs = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print("Pairs:", pairs)

print()

sentence = input("Enter a sentence: ")
vowels = [ch for ch in sentence if ch.lower() in "aeiou"]
print("Vowels:", vowels)
print("Count:", len(vowels))
