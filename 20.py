s1 = {10, 20, 30, 40, 50}

print("Set:", s1)
print("Length:", len(s1))

s1.add(60)
print("After add 60:", s1)

s1.remove(30)
print("After remove 30:", s1)

s1.discard(100)
print("After discard 100:", s1)

print()

s2 = {30, 40, 50, 60, 70}
s3 = {40, 50, 60, 70, 80}

print("Union:", s2 | s3)
print("Intersection:", s2 & s3)
print("Difference:", s2 - s3)
print("Symmetric Difference:", s2 ^ s3)

print()

nums = [1, 2, 3, 2, 4, 3, 5, 1, 6]
unique = list(set(nums))
print("Original:", nums)
print("Unique:", unique)

print()

a = {1, 2, 3, 4}
b = {1, 2, 3, 4, 5, 6}
print("Is subset:", a.issubset(b))
print("Is superset:", b.issuperset(a))
