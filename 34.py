from collections import Counter, defaultdict, deque, namedtuple

# 1. Counter: Frequency analysis
text = "apple banana apple cherry banana apple mango orange banana"
words = text.split()
counter = Counter(words)
print("Word frequencies:", counter)
print("Top 2 most common:", counter.most_common(2))

print()

# 2. defaultdict: Grouping records by department
employees = [
    ("Engineering", "Aditya"),
    ("Design", "Sara"),
    ("Engineering", "Vikram"),
    ("Marketing", "Pooja"),
    ("Design", "Kabir"),
]
dept_members = defaultdict(list)
for dept, name in employees:
    dept_members[dept].append(name)

print("Department rosters:")
for dept, members in dept_members.items():
    print(f"  {dept}: {', '.join(members)}")

print()

# 3. deque: Double-ended queue for efficient sliding window / task queue
tasks = deque(["Task 1", "Task 2", "Task 3"])
tasks.append("Task 4")        # Add to right
tasks.appendleft("Urgent Task 0") # Add to left
print("Task queue:", list(tasks))
print("Processed first:", tasks.popleft())
print("Processed last:", tasks.pop())
print("Remaining tasks:", list(tasks))

print()

# 4. namedtuple: Lightweight readable data objects
Student = namedtuple("Student", ["roll_no", "name", "gpa"])
s1 = Student(101, "Aditya Bhandari", 9.4)
s2 = Student(102, "Rohan Sharma", 8.8)
print("Student 1:", s1.name, "| Roll:", s1.roll_no, "| GPA:", s1.gpa)
print("Student 2 representation:", s2)
