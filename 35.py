import itertools

# 1. itertools.chain: Flatten and combine sequences
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
combined = list(itertools.chain(list_a, list_b))
print("Chained sequences:", combined)

print()

# 2. itertools.accumulate: Running totals / prefix operations
numbers = [10, 20, 15, 30, 5]
running_sum = list(itertools.accumulate(numbers))
print("Original numbers:", numbers)
print("Running total:", running_sum)

running_max = list(itertools.accumulate(numbers, max))
print("Running max:", running_max)

print()

# 3. itertools.groupby: Group consecutive keys (sorted input)
inventory = [
    {"category": "Fruit", "item": "Apple"},
    {"category": "Fruit", "item": "Banana"},
    {"category": "Stationery", "item": "Notebook"},
    {"category": "Stationery", "item": "Pen"},
    {"category": "Vegetable", "item": "Carrot"},
]
print("Grouped inventory:")
for key, group in itertools.groupby(inventory, key=lambda x: x["category"]):
    items = [x["item"] for x in group]
    print(f"  [{key}]: {items}")

print()

# 4. itertools.combinations and permutations
colors = ["Red", "Green", "Blue"]
combinations_2 = list(itertools.combinations(colors, 2))
print("Pairs of colors (combinations):", combinations_2)

permutations_2 = list(itertools.permutations(colors, 2))
print("Arrangements of 2 colors (permutations):", len(permutations_2), "total")
