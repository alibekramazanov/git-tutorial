"""
Practice 6: Directory Management - Create and List Directories
"""

import os

print("=" * 70)
print("DIRECTORY MANAGEMENT")
print("=" * 70 + "\n")

# Example 1: Create directory
print("1. Create directory:")
os.mkdir("test_dir")
print("✓ Created: test_dir")

# Example 2: Create nested directories
print("\n2. Create nested directories:")
os.makedirs("parent/child/grandchild", exist_ok=True)
print("✓ Created: parent/child/grandchild")

# Example 3: List directory contents
print("\n3. List current directory:")
items = os.listdir(".")
print(f"Items in current directory: {len(items)}")
for item in items[:5]:  # Show first 5
    print(f"  - {item}")

# Example 4: Get current working directory
print("\n4. Current working directory:")
cwd = os.getcwd()
print(f"  {cwd}")

# Example 5: Find files by extension
print("\n5. Find all .py files:")
for item in os.listdir("."):
    if item.endswith(".py"):
        print(f"  - {item}")

# Cleanup
os.rmdir("test_dir")
import shutil
shutil.rmtree("parent")

print("\n" + "=" * 70 + "\n")