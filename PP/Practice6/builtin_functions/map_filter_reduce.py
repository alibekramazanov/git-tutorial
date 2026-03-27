"""
Practice 6: Built-in Functions - map, filter, reduce
"""

from functools import reduce

print("=" * 70)
print("MAP, FILTER, REDUCE EXAMPLES")
print("=" * 70 + "\n")

# Example 1: map() - apply function to all items
print("1. map() - square all numbers:")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Example 2: filter() - keep only items that match condition
print("\n2. filter() - keep even numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original: {numbers}")
print(f"Even numbers: {evens}")

# Example 3: reduce() - combine all items into single value
print("\n3. reduce() - sum all numbers:")
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Example 4: Practical example - process names
print("\n4. Practical example - process names:")
names = ["alice", "bob", "charlie"]
capitalized = list(map(str.capitalize, names))
print(f"Original: {names}")
print(f"Capitalized: {capitalized}")

# Example 5: Chain map and filter
print("\n5. Chain map and filter:")
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x > 10, map(lambda x: x**2, numbers)))
print(f"Original: {numbers}")
print(f"Squared and > 10: {result}")

print("\n" + "=" * 70 + "\n")