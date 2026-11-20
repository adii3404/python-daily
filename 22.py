f = open("sample.txt", "w")
f.write("Hello World\n")
f.write("This is Python\n")
f.write("File handling is easy\n")
f.close()

f = open("sample.txt", "r")
data = f.read()
print("Full file:")
print(data)
f.close()

f = open("sample.txt", "r")
print("Line by line:")
for line in f:
    print(line, end="")
f.close()

print()

f = open("sample.txt", "a")
f.write("This line is appended\n")
f.close()

f = open("sample.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))
for i in range(len(lines)):
    print("Line", i + 1, ":", lines[i], end="")
f.close()

import os
os.remove("sample.txt")
print("\nFile deleted")
