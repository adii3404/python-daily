nums = [64, 25, 12, 22, 11]

n = len(nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted:", nums)

print()

nums = [3, 7, 1, 9, 2, 5]
smallest = nums[0]
largest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest:", smallest)
print("Largest:", largest)

print()

nums = [1, 2, 3, 2, 4, 3, 5]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print("Unique:", unique)
