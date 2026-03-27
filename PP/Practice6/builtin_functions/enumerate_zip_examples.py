"""
Practice 6: Built-in Functions - enumerate, zip, and other utilities
"""

print("=" * 70)
print("ENUMERATE, ZIP, AND OTHER BUILT-IN FUNCTIONS")
print("=" * 70 + "\n")

# Example 1: enumerate() - loop with index
print("1. enumerate() - loop with index:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print("\n2. enumerate() with custom start:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  #{index}: {fruit}")

# Example 3: zip() - combine multiple lists
print("\n3. zip() - combine lists:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# Example 4: zip() with different lengths
print("\n4. zip() stops at shortest list:")
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c"]
result = list(zip(list1, list2))
print(f"  {result}")

# Example 5: len(), sum(), min(), max()
print("\n5. Aggregate functions:")
numbers = [10, 5, 8, 15, 3, 12]
print(f"Numbers: {numbers}")
print(f"  Length: {len(numbers)}")
print(f"  Sum: {sum(numbers)}")
print(f"  Min: {min(numbers)}")
print(f"  Max: {max(numbers)}")

# Example 6: sorted()
print("\n6. sorted() - sort without modifying original:")
unsorted = [5, 2, 8, 1, 9]
sorted_list = sorted(unsorted)
print(f"Original: {unsorted}")
print(f"Sorted: {sorted_list}")

# Example 7: Type conversion functions
print("\n7. Type conversions:")
print(f"  int('42'): {int('42')}")
print(f"  float('3.14'): {float('3.14')}")
print(f"  str(100): '{str(100)}'")
print(f"  list('hello'): {list('hello')}")
print(f"  tuple([1,2,3]): {tuple([1,2,3])}")

print("\n" + "=" * 70 + "\n")