student = {"name": "Aditya", "age": 20, "marks": 85}

print("Name:", student["name"])
print("Age:", student.get("age"))
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

student["grade"] = "A"
print("After adding grade:", student)

student["marks"] = 90
print("After updating marks:", student)

del student["age"]
print("After deleting age:", student)

print()

marks = {"math": 90, "science": 85, "english": 78, "hindi": 92}

total = 0
for subject in marks:
    total = total + marks[subject]

print("Total:", total)
print("Average:", total / len(marks))

print()

s = input("Enter a string: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

for key in freq:
    print(key, "->", freq[key])
