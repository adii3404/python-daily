matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Original:")
for r in matrix:
    print(r)
print("Transposed:")
for r in transposed:
    print(r)

print()

names = ["rahul", "amit", "sneha", "pooja"]
marks = [85, 92, 78, 95]
passed_students = {name.title(): score for name, score in zip(names, marks) if score >= 80}
print("Passed students:", passed_students)

print()

divisible = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print("Divisible by 3 and 5:", divisible)

vowels = {char.lower() for char in "Programming in Python" if char.lower() in "aeiou"}
print("Unique vowels found:", vowels)
