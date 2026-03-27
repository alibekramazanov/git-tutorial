"""
Practice 6: File Handling - Writing and Appending Files
"""

print("=" * 70)
print("FILE WRITING EXAMPLES")
print("=" * 70 + "\n")

# Example 1: Write mode (overwrites)
print("1. Write mode ('w'):")
with open("output.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
print("✓ File created")

# Example 2: Append mode (adds to end)
print("\n2. Append mode ('a'):")
with open("output.txt", "a") as f:
    f.write("Third line (appended)\n")
print("✓ Line appended")

# Verify content
with open("output.txt", "r") as f:
    print("Final content:")
    print(f.read())

# Example 3: Write multiple lines
print("\n3. Write multiple lines:")
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("multi.txt", "w") as f:
    f.writelines(lines)
print("✓ Multiple lines written")
with open("multi.txt", "r") as f:
    print(f.read())

# Cleanup
import os
os.remove("output.txt")
os.remove("multi.txt")

print("\n" + "=" * 70 + "\n")