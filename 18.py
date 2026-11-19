t = (10, 20, 30, 40, 50)

print("Tuple:", t)
print("Length:", len(t))
print("First:", t[0])
print("Last:", t[-1])
print("Slice:", t[1:4])

print("Max:", max(t))
print("Min:", min(t))
print("Sum:", sum(t))

print()

t2 = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", t2.count(2))
print("Index of 4:", t2.index(4))

print()

t3 = (1, 2, 3)
t4 = (4, 5, 6)
t5 = t3 + t4
print("Merged:", t5)

a, b, c = t3
print("Unpacked:", a, b, c)

nums = [1, 2, 3]
t6 = tuple(nums)
print("List to Tuple:", t6)

t7 = (10, 20, 30)
l = list(t7)
print("Tuple to List:", l)
