"""
Practice 6: Directory Management - Move Files Between Directories
"""

import os
import shutil

print("=" * 70)
print("MOVE FILES BETWEEN DIRECTORIES")
print("=" * 70 + "\n")

# Setup
os.makedirs("source_dir", exist_ok=True)
os.makedirs("dest_dir", exist_ok=True)

# Create test files in source
for i in range(1, 4):
    with open(f"source_dir/file{i}.txt", "w") as f:
        f.write(f"File {i} content\n")

print("Setup: Created source_dir with 3 files\n")

# Example 1: Move single file
print("1. Move single file:")
shutil.move("source_dir/file1.txt", "dest_dir/file1.txt")
print("✓ Moved: file1.txt")

# Example 2: Copy file to another directory
print("\n2. Copy file to directory:")
shutil.copy("source_dir/file2.txt", "dest_dir/")
print("✓ Copied: file2.txt")

# Example 3: List files in directories
print("\n3. Directory contents:")
print(f"source_dir: {os.listdir('source_dir')}")
print(f"dest_dir: {os.listdir('dest_dir')}")

# Cleanup
shutil.rmtree("source_dir")
shutil.rmtree("dest_dir")

print("\n" + "=" * 70 + "\n")