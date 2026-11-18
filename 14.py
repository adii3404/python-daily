nums = [10, 20, 30, 40, 50]

print("List:", nums)
print("Length:", len(nums))
print("First:", nums[0])
print("Last:", nums[-1])

nums.append(60)
print("After append:", nums)

nums.insert(2, 25)
print("After insert at 2:", nums)

nums.remove(30)
print("After remove 30:", nums)

popped = nums.pop()
print("Popped:", popped)
print("After pop:", nums)

print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))
