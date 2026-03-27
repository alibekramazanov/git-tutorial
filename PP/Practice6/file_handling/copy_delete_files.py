"""
Practice 6: File Handling - Copy and Delete Files
"""

import os
import shutil

print("=" * 70)
print("FILE COPY AND DELETE OPERATIONS")
print("=" * 70 + "\n")

# Create test file
with open("test.txt", "w") as f:
    f.write("Test file content\n")

# Example 1: Copy file
print("1. Copy file:")
shutil.copy("test.txt", "test_copy.txt")
print("✓ File copied: test.txt → test_copy.txt")

# Example 2: Backup file
print("\n2. Create backup:")
shutil.copy("test.txt", "test_backup.txt")
print("✓ Backup created: test_backup.txt")

# Example 3: Delete file
print("\n3. Delete file:")
os.remove("test_copy.txt")
print("✓ File deleted: test_copy.txt")

# Cleanup
os.remove("test.txt")
os.remove("test_backup.txt")

print("\n" + "=" * 70 + "\n")