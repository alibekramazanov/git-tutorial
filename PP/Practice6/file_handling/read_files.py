"""
Practice 6: File Handling - Reading Files
"""

print("=" * 70)
print("FILE READING EXAMPLES")
print("=" * 70 + "\n")

# Create sample file
with open("sample.txt", "w") as f:
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python File Handling\n")
    f.write("Line 3: This is a test\n")

# Example 1: Read entire file
print("1. Read entire file:")
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# Example 2: Read line by line
print("\n2. Read line by line:")
with open("sample.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

# Example 3: Read all lines as list
print("\n3. Read all lines as list:")
with open("sample.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        print(f"  {i}. {line.strip()}")

# Cleanup
import os
os.remove("sample.txt")

print("\n" + "=" * 70 + "\n")