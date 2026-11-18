nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [x for x in nums if x % 2 == 0]
print("Even:", even)

odd = [x for x in nums if x % 2 != 0]
print("Odd:", odd)

squares = [x * x for x in nums]
print("Squares:", squares)

print()

nums = [1, 2, 3, 4, 5]
rev = nums[::-1]
print("Reversed:", rev)

print()

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("Merged:", merged)

print()

nums = [1, 2, 3, 4, 5]
n = int(input("Enter number to search: "))
found = False
for i in range(len(nums)):
    if nums[i] == n:
        print("Found at index:", i)
        found = True
        break
if not found:
    print("Not found")
